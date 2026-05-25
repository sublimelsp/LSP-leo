from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import LspTextCommand
from LSP.plugin import OnPreStartContext
from LSP.plugin import Promise
from LSP.plugin import Request
from LSP.plugin import request_handler
from LSP.plugin import SessionViewProtocol
from LSP.plugin.core.protocol import Point
from LSP.plugin.core.views import range_to_region
from LSP.plugin.core.views import region_to_range
from LSP.plugin.core.views import text_document_identifier
from LSP.protocol import Range
from LSP.protocol import URI
from lsp_utils import NodeManager
from pathlib import Path
from sublime_lib import ResourcePath
from typing import Any
from typing import final
from typing import TypedDict
from typing_extensions import override
import sublime
import sublime_plugin


class ServerPoint(TypedDict):
    row: int
    column: int

class ServerRange(TypedDict):
    start: ServerPoint
    end: ServerPoint

class ColorizeParams(TypedDict):
    uri: URI
    scopes: dict[str, list[ServerRange]]


def plugin_loaded() -> None:
    LspLeoPlugin.register()


def plugin_unloaded() -> None:
    LspLeoPlugin.unregister()


@final
class LspLeoPlugin(LspPlugin):

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        NodeManager.on_pre_start_async(
            context,
            cls.plugin_storage_path,
            ResourcePath('Packages', package_name, 'language-server'),
            Path('server.js'),
            node_version_requirement='>=16',
            skip_npm_install=True,
        )

    @request_handler('ColoringService.colorize')
    def on_coloring_service_colorize(self, params: ColorizeParams) -> Promise[None]:
        session = self.weaksession()
        if not session:
            return Promise.resolve(None)

        def colorize(view: sublime.View | None) -> None:
            if view:
                # Get all views, including cloned ones (opened in Split View mode)
                for view in view.buffer().views():
                    syntax_coloring = SyntaxColoring()
                    syntax_coloring.view = view
                    syntax_coloring.colorize(params)

        return session.open_uri_async(params['uri']).then(colorize)

    @override
    def on_selection_modified_async(self, session_view: SessionViewProtocol) -> None:
        session = self.weaksession()
        if session:
            request = Request("ColoringService.colorize", {"uri": session_view.get_uri()})
            session.send_request_task(request)


class SyntaxColoringEventListener(sublime_plugin.EventListener):

    def on_clone_async(self, view: sublime.View):
        view.run_command('lsp_leo_handle_clone')


class LspLeoHandleCloneCommand(LspTextCommand):

    def run(self, edit: sublime.Edit, **kwargs: Any):
        sublime.set_timeout_async(self._run_async)

    def _run_async(self) -> Any:
        if session := self.session_by_name(self.session_name):
            # Get all views, including cloned ones (opened in Split View mode)
            # This hack helps to send ColorizeRequest for non cloned views
            # (for cloned views there is no listener in LSP for some reason)
            for view in self.view.buffer().views():
                request = Request("ColoringService.colorize", text_document_identifier(view))
                session.send_request_task(request)


class SyntaxColoring:
    view: sublime.View

    def colorize(self, params: ColorizeParams) -> None:
        settings = self.view.settings()
        color_scheme = settings.get("color_scheme")
        if color_scheme != "leo.sublime-color-scheme":
            return
        highlight_line = settings.get("highlight_line")
        for key, values in params["scopes"].items():
            if len(values):
                flags = sublime.DRAW_NO_OUTLINE
                regularScope = key
                highlightedScope = key.replace("server.leo", "highlight.server.leo")
                self.view.erase_regions(regularScope)
                self.view.erase_regions(highlightedScope)
                regularRegions = []
                highlightedRegions = []
                for item in values:
                    lsp_range = self.server_range_to_lsp(item)
                    region = range_to_region(lsp_range, self.view)
                    selected_row = self.view.sel()
                    cursorRegion = selected_row[0]
                    scope = regularScope
                    is_point = cursorRegion.begin() == cursorRegion.end()

                    if not is_point and selected_row.contains(region):
                        scope = highlightedScope

                    if is_point and highlight_line:
                        cursorRange = region_to_range(self.view, cursorRegion)
                        if lsp_range['start']['line'] == cursorRange['start']['line']:
                            scope = highlightedScope

                    if scope == regularScope:
                        regularRegions.append(region)
                    else:
                        highlightedRegions.append(region)

                self.view.add_regions(regularScope, regularRegions, scope=regularScope, flags=flags)
                self.view.add_regions(highlightedScope, highlightedRegions, scope=highlightedScope, flags=flags)

    def server_range_to_lsp(self, server_range: ServerRange) -> Range:
        return {
            'start': Point(server_range["start"]["row"], server_range["start"]["column"]).to_lsp(),
            'end': Point(server_range["end"]["row"], server_range["end"]["column"]).to_lsp()
        }
