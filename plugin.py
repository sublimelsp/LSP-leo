import os
import sublime
import sublime_plugin
from lsp_utils import NpmClientHandler
from LSP.plugin.core.registry import windows
from LSP.plugin.core.protocol import Range, Request
from LSP.plugin.core.views import range_to_region, region_to_range
from LSP.plugin.core.typing import Any, Callable, Dict, List, TypedDict
from LSP.plugin.core.url import view_to_uri
from lsp_utils import request_handler
from LSP.plugin import uri_to_filename


ServerPoint = TypedDict('ServerPoint', {
    'row': int,
    'column': int,
})
ServerRange = TypedDict('ServerRange', {
    'start': ServerPoint,
    'end': ServerPoint,
})
ColorizeRequest = TypedDict('ColorizeRequest', {
    'uri': str,
    'scopes': Dict[str, List[ServerRange]]
})


def plugin_loaded() -> None:
    LspLeoPlugin.setup()
    setup_leohover_settings()

def plugin_unloaded() -> None:
    LspLeoPlugin.cleanup()

def setup_leohover_settings() -> None:
    preferences_filename = 'Preferences.sublime-settings'
    preferences = sublime.load_settings(preferences_filename)
    value = preferences.get("mdpopups.sublime_user_lang_map")
    if not value:
        value = {}
    value["leohover"] = (('leohover',), ('LSP-leo/leoHover',))
    preferences.set("mdpopups.sublime_user_lang_map", value)
    sublime.save_settings(preferences_filename)

class LspLeoPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, 'server.js')
    skip_npm_install = True

    @request_handler('ColoringService.colorize')
    def on_coloring_service_colorize(self, request: ColorizeRequest, response: Callable[[Any], None]):
        filename = uri_to_filename(request['uri'])
        view = sublime.active_window().find_open_file(filename)

        if view:
            # Get all views, including cloned ones (opened in Split View mode)
            views = view.buffer().views()
            for v in views:
                syntax_coloring = SyntaxColoring(v)
                syntax_coloring.colorize(request)
        # Server doesn't require any specific response.
        response(None)

def send_colorize_request(view: sublime.View):
    listener = windows.listener_for_view(view)
    if listener:
        language = listener.get_language_id()
        if language == "leo":
            exists = bool(listener.session_async('hoverProvider'))
            if not exists:
                # if there is no listener need to wait for it
                print("No listener found!")
                return
            for session in listener.sessions_async():
                uri = view_to_uri(view)
                params = {"uri": uri}
                request = Request("ColoringService.colorize", params)
                session.send_request_async(request, lambda res: res, lambda res: res)

class SyntaxColoringViewListener(sublime_plugin.ViewEventListener):
    def on_selection_modified_async(self):
        send_colorize_request(self.view)

class SyntaxColoringEventListener(sublime_plugin.EventListener):
    def on_clone(self, view: sublime.View):
        filename = view.file_name()
        if not filename:
            return
        file_extension = os.path.splitext(filename)[1][1:]
        if not file_extension:
            return
        settings = sublime.load_settings("LSP-leo.sublime-settings")
        if not settings:
            return
        languages = settings.get("languages")
        if not isinstance(languages, list):
            return
        for language in languages:
            language_id = language.get("languageId")
            if isinstance(language_id, str) and language_id == file_extension:
                # Get all views, including cloned ones (opened in Split View mode)
                # This hack helps to send ColorizeRequest for non cloned views
                # (for cloned views there is no listener in LSP for some reason)
                views = view.buffer().views()
                for v in views:
                    send_colorize_request(v)
                break

class SyntaxColoring:
    def __init__(self, view: sublime.View) -> None:
        self.view = view

    def colorize(self, request: ColorizeRequest) -> None:
        settings = self.view.settings()
        color_scheme = settings.get("color_scheme")
        if color_scheme != "leo.sublime-color-scheme":
            return
        highlight_line = settings.get("highlight_line")
        for key, values in request["scopes"].items():
            if len(values):
                flags = sublime.DRAW_NO_OUTLINE
                regular_scope = key
                highlighted_scope = key.replace("server.leo", "highlight.server.leo")
                self.view.erase_regions(regular_scope)
                self.view.erase_regions(highlighted_scope)
                regular_regions = []
                highlighted_regions = []
                for item in values:
                    lsp_range = self.server_range_to_lsp(item)
                    region = range_to_region(lsp_range, self.view)
                    selected_row = self.view.sel()
                    cursor_region = selected_row[0]
                    scope = regular_scope
                    is_point = cursor_region.begin() == cursor_region.end()

                    if not is_point and selected_row.contains(region):
                        scope = highlighted_scope

                    if is_point and highlight_line:
                        cursor_range = region_to_range(self.view, cursor_region)
                        if lsp_range['start']['line'] == cursor_range['start']['line']:
                            scope = highlighted_scope

                    if scope == regular_scope:
                        regular_regions.append(region)
                    else:
                        highlighted_regions.append(region)

                self.view.add_regions(regular_scope, regular_regions, scope=regular_scope, flags=flags)
                self.view.add_regions(highlighted_scope, highlighted_regions, scope=highlighted_scope, flags=flags)


    def server_range_to_lsp(self, sever_range: ServerRange) -> Range:
        return {
            'start': {
                "line": sever_range["start"]["row"],
                "character": sever_range["start"]["column"]
            },
            'end': {
                "line": sever_range["end"]["row"],
                "character": sever_range["end"]["column"]
            }
        }
