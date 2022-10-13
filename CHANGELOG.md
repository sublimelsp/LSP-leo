# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keep a changelog] and this project adheres to [Semantic Versioning][semantic versioning].

## [0.8.35] - 2022-10-13

### Added
- Coloring to function name in declaration
- Coloring to finalize, increment, decrement function call

## [0.8.34] - 2022-10-12

### Fixed
- Fix release

## [0.8.33] - 2022-10-12

### Added
- A valid Leo project structure is diagnosed as an error

## [0.8.32] - 2022-10-07

### Added
- Diagnostic when there are two records with same names
- Diagnostic when the specified function type is not found circuit/record
- An error is not diagnosed when a variable of one type is assigned the value of a variable of another type
- Fix diagnostics when the intermediate or final result of an expression is out of range

### Changed
- Update colors for new tokens in leo files according to https://github.com/AleoHQ/ARCs/discussions/17

### Removed
- Diagnostic "failed to create const variable"

### Fixed
- The mismatch between the names of the function parameter and the variable in the input section is not an error
- Diagnostic error when adding scalars
- The color of a variable is displayed incorrectly if the variable name matches the function name
- Diagnostic error when the number of record members does not match the number of record members in the record initialization expression
- Diagnostic error when a circuit member is missing in the circuit initialization expression
- Diagnostic when there are two circuits with same names
- Diagnostic error of scalar type values
- Fix an error diagnostics when the function type is not specified
- Diagnostic error when the number of record members does not match the number of record members in the record initialization expression

## [0.8.31] - 2022-09-30

### Removed

### Fixed
- Highlighting of problematic nodes in the method call chain diagnostics
- Fix the error message when an integer type is not explicitly defined

## [0.8.30] - 2022-09-30

### Fixed
- During diagnostics for called unary and binary operations fixed problematic callee node highlighting
- Fix diagnostics for address comparison operations
- Diagnostic error when the 'if' condition is Self
- Fix error message when type of integer value in ternary expression does not match expected


## [0.8.29] - 2022-09-29

### Added
- Diagnostics for required record attributes
- Hover for record attributes

### Fixed
- Fix diagnostics of negative values of unsigned integer type

## [0.8.28] - 2022-09-28

### Added
- Diagnostics when a deprecated test function is used
- Added yellow color highlight to leo program inside leo files

### Changed
- Unary operation .sqrt renamed to .square_root

### Fixed
- Diagnostic error if the type is not specified after the colon when defining the variable type
- Diagnostics is incorrect if the code contains an address that does not meet the rules of the Leo grammar
- Add error diagnostics when an invalid character is entered after the operator sign

## [0.8.27] - 2022-09-27

### Added
- Remake import parser for new leo syntax
- Record and circuit names are not highlighted in red if they are defined in the input file

### Fixed
- Fixed diagnostic checking for duplicates in functions
- Incorrect diagnostic for programs without input section
- Fixed incorrect diagnosis of valid arguments of finalize functions
- Fixed diagnostic when loop iterator is visible outside of loop

## [0.8.26] - 2022-09-26

### Added
- Added support for address and string types for binary operations Neq and Eq

### Fixed
- Fixed diagnostics for called unary and binary operations
- The record type should be red

## [0.8.25] - 2022-09-23

### Changed

### Fixed
- Address type values should be highlighted in blue in .leo and .in files

## [0.8.24] - 2022-09-22

### Fixed
- Address type values should be highlighted in blue in .leo and .in files

## [0.8.23] - 2022-09-22

### Changed
- The async keyword should be highlighted in red

## [0.8.22] - 2022-09-22

### Added
- The async keyword should be highlighted in red.- 
- The address keyword is not highlighted in .aleo files

### Fixed
- Address type values should be highlighted in blue in .leo and .in files
- The import keyword should be highlighted in red

## [0.8.21] - 2022-09-20

### Added
- Implement diagnostics of the finalize function
- 
### Changed
- Changed theme name from Aleo to Leo

### Fixed
- Incorrect diagnostics of address value
- Unknown variable data type error should only be displayed for the variable, not for the expression
- For unsigned integers, the subtraction operation is diagnosed as an error
- Diagnostic error not found .in file when the program name does not match the folder name

## [0.8.20] - 2022-09-20

### Fixed
- Error on unknown data type of a call chain or function call should not sound like an unknown variable
- Diagnostic error if a global variable self.caller is used
- Diagnostic error when a function does not return any value

## [0.8.19] - 2022-09-19

### Changed
- Changed package name

## [0.8.18] - 2022-09-19

### Changed
- Changed register token color from purple to uncolored

### Fixed
- Diagnostic error when a variable is called the deprecated protected names 'as' or 'mut'
- Incorrect color for aleo token with number


## [0.8.17] - 2022-09-16

### Changed

### Fixed
- Fixed diagnostic of type mismatch in the expression for defining a variable by a literal value
- Fixed diagnostic of type mismatch in the expression of defining a variable by the value of the result of a function call
- Fixed type mismatch diagnostic in an expression that contains a function call

## [0.8.16] - 2022-09-15

### Changed
- On change active editor tab set aleo color scheme

### Fixed
- Diagnostics when defining a variable of type tuple: the circuit type is defined as a tuple

## [0.8.15] - 2022-09-14

### Added
- Added diagnostics of the parameters of methods of Core Binary operations and Algorithms

## [0.8.14] - 2022-09-13

### Added
- Added built-in primitive types as circuits with methods as entities: Address, Boolean, Field, Group, Integer, Scalar, String

### Fixed
- Multiline comments are not highlighted correctly if they are located in area of function arguments
- Fix types and registers highlight in aleo files

## [0.8.13] - 2022-09-09

### Added
- Implement type comparison diagnostics
- Add diagnostics of bit operations
- Added built-in circuits BHP, Pedersen and Poseidon

### Removed
- Remove redundant user settings

## [0.8.12] - 2022-09-08

### Added
- Syntax highlighting to files with .aleo extension

### Fixed
- Comments are not highlighted correctly if they are located in area of function arguments
- Implement error diagnostics when the input file provides additional inputs that is not expected in the 'main' function

## [0.8.11] - 2022-09-06

### Fixed
- Incorrect diagnostics if console.assert() function have more than one arguments

## [0.8.10] - 2022-09-02

### Fixed
- The loop iterator data type must have a declared type (and not just u32)
- Fix diagnostic error 'unknown variable' if variable is defined out of block

## [0.8.9] - 2022-09-01

### Fixed
- Incorrect diagnostic for records in input files
- Incorrect diagnostic for record property type
- Incorrect diagnostic for record inline definition
- Incorrect diagnostics for duplication variables definitions
- Incorrect diagnostics for missing declaration
- Diagnostic error if assert_eq and assert_neq functions have more than two arguments
- Diagnostic error when the mode of 'main' function parameter is different from the mode declared in the 'main' section of the input file
- The type of the loop conditional expressions must match the type of the iterator

### Security

## [0.8.8] - 2022-09-01

### Fixed
- Fixed CHANGELOG.md format

## [0.8.0] - 2021-08-13

### Added

- Support for [import RFC].
- Import of const variables.
- Rename "core" packages to "std".
- Update error messages.
- Add support for array without size.
- Add support for len method for arrays.
- Add support for type alias.
- Add support of stdlib prelude.
- Add support for constant circuit variable.
- Add diagnostic for deprecated 'mut self'.
- Leo RFC 009: Conversions with Bits and Bytes
- Add diagnostic for constant function parameters.
- Fixed Self type definitions diagnostic.
- Fixed diagnostic of importing all dependencies from stdlib.
- Fixed diagnostic of alias type sent as inline circuit parameter.
- Add diagnostic of const main function.
- Fixed diagnostic for missed return for all paths.
- Added diagnostic of non constant expressions in for statement.
- Fixed diagnostic of unnecessary return statements.
- Fixed diagnostic of alias type argument of main function.
- Fixed diagnostic of self parameter in constant methods.
- Fixed diagnostic of nested array access.
- Fixed diagnostic of assignment to const self.
- Added diagnostic for global const duplicates.
- Added diagnostic for duplicates global const and function parameter.
- Fixed diagnostic of char array function parameters.
- Fixed diagnostic of string return type.
- Added diagnostic to detect duplicated input variables in the main and constants sections.
- Fixed diagnostic of unknown type integer multiline array.
- Added diagnostic to detect the presence of "dead code".
- Added diagnostic of range array access when range start bigger then range end.
- Added diagnostic of expression assigned to array item.
- Added diagnostic of the argument type of the console.assert function.
- Add a function check for the mandatory return value and its type, as well as a check for const, constant, public modifiers.
- The number of arguments passed to the function should not exceed eight.
- Implement a diagnostics of @program annotation and diagnostics of parameters in .in file.
- Added a diagnostic message stating that the circuit functions are currently an unstable feature
- Added diagnostic when calling circuit method in the call chain
- Added diagnostic an error if the variable type is not specified
- Add a @program annotation before the main function in all examples
- Update code highlighting according to latest ABNF grammar
- Add diagnostics when the deprecated keyword const is used in input files.
- Update syntax highlighting
- Add Record parser
- Add Record existence diagnostics
- Add search Record
- Add diagnostics of an expression with an access to a variable that is defined in another block

### Fixed

- Duplicated definitions diagnostic.
- The error "failed to resolve function" is not diagnosed if a function import uses an alias.
- The ternary expression template must be without an if.
- Autocomplete does not work in the ternary expression.
- Autocomplete does not work correctly for the array method len().
- Add diagnostics for negative values of the unsigned integers.
- Error 'conflicting imports found' is not diagnosed.
- Go to Definition function should be open a window with a choice between navigating to a circuit property or to a variable.
- Go to Definition function does not work for circuit property and function parameters
- Diagnostics for non-const values of function/method calls.
- Mismatch of the arrays dimensions is not diagnosed as an error.
- Types are not parsed for expressions.
- Incorrect diagnostics of a circuit member when a chain calling of a circuit function.
- Constant values are not diagnosed as constants in function arguments.
- A variable in for loop after .. should be white.
- Show hover over a len() function.
- The mut keyword should be red when hovering over the self keyword.
- The len() function type is not defined correctly for nested array.
- Types of negative values of the circuit parameters are not diagnosed.
- Wrong type parsing for nested array access.
- Incorrect diagnostic of methods parameters in call chain.
- Diagnostic error when main function returns arrays.
- Incorrect hover highlight in linear regression example.
- The circuit member variable is not highlighted.
- Diagnostics error occurs when a function type is changed.
- Diagnostic error when arrays are constant arguments of function.
- Return type is not defined correctly when calling a circuit function or circuit parameter.
- Multiline value of 'string' variable is not highlighted correctly.
- An unresolved circuit reference is not diagnosed.
- The 'mut' keyword is not highlighted.
- Diagnostic error when the argument of circuit function is an array element.
- Tuple index should be blue.
- The "const" keyword should be red.
- The Console Log function is not highlighting in Data Types example.
- Autocomplete not working correctly when dot is entered in string value.
- Fix the len() function autocomplete.
- The type of the tuple elements is not defined correctly.
- Wrong diagnostics of return type of chain call.
- Tuple return type incorrect diagnostic of main function.
- Array elements of type "field" and "group" are not highlighted.
- The type of the array element is not diagnosed.
- Highlighting does not work correctly inside if statements.
- Wrong token coloring for circuit attribute with array type with tuple dimension.
- Incorrect highlighting of the first parameter for Self.
- Unnecessary spaces before the code in the Inputs section.
- Autocomplete does not work for the types of variable.
- The valid code of the access for an array element is diagnosed as an error.
- Wrong coloring of the circuit parameters.
- Variable color in ternary expression is not correctly.
- Fix the color of the char variables to yellow.
- Imports diagnostic is not correctly if there are duplicates of imports.
- The valid code is diagnosed as an error.
- Diagnostics does not work for the operators with a 'field' and an integers variables.
- Autocomplete of the 'const' keyword does not work in the global area of code.
- Diagnostics error when you defines the integer type in the ternary expression.
- Exceeding the maximum value of the integer is not diagnosed.
- Diagnostics error in an expressions with variables of 'group' type.
- Relation operators are not diagnosed correctly for a variables of the 'field' type.
- Autocomplete does not work for the static functions of the circuit.
- The condition type is not diagnosed in the if-else statement.
- Incorrect diagnostics for function with return statements.
- The error "expected const, found non-const value" for a function argument is not diagnosed.
- Diagnostic of already defined definitions.
- Fix incorrect const variables diagnostic.
- Update import path of core packages.
- References to global constants are not diagnosed correctly.
- Diagnostics does not work correctly if the tuple value is an array.
- Result type of the (==) operation is not defined correctly.
- The error is not diagnosed if the type of the function is not defined but it returns an integer type.
- Error 'unexpected type' is not diagnosed for the '+=' operator in the loop 'for'.
- A variable of the "field" type is diagnosed as a variable of the "integer" type.
- The member type of a multidimensional array is not defined correctly.
- Wrong diagnostics if the name of the in. file does not match with the name of the root folder of the project.
- Incorrect array diagnostics.
- Fix crashing server when incorrect circuit syntax.
- Fix not diagnosed unresolved variable reference in expression.
- Fix crashing server when incorrect variable identifier syntax.
- Diagnostic error when chained call a circuit function.
- Diagnostic error on method call on undefined variable.
- Diagnostic error when chained access a circuit attribute.
- Diagnostic error of circuit access modifiers.
- Fix diagnostics for unexpected circuit static constant members type.
- Missing diagnostics for the order of members in circuits.
- Missing diagnostics for duplicated static constant members in circuits.
- Wrong diagnostics for operation expressions using boolean expressions.
- Fix autocomplete for static circuit members.
- Wrong diagnostics when return type value of circuit member function is an array of Self.
- Wrong diagnostics for one-dimensional array tuple syntax.
- Fix completions with whitespaces for static circuit members.
- Diagnostic error when the keyword Self is used as circuit in the main function.
- Fix call chain parsing logic regarding access to array elements.
- An error is not diagnosed when the value of an integer function parameter is out of range of an integer.
- Error is not diagnosed when an integers sum is out of range.
- The duplicate name error is not diagnosed.
- Unresolved variable reference is not diagnosed.
- Crash on load with stdlib.
- Fixed diagnostic error when a function returns a tuple of implicit integers.
- Fixed input diagnostics of arrays with tuple syntax.
- Modify the description of the diagnostic error when argument types don't match the types in the input file
- Fix incorrect code coloring when there are multiple * characters in the code
- Up minimum version of vscode.
- The const keyword in the tooltip should be highlighted in red, when you hover over the 'self'
- Modify a hover of the diagnostic error when input main section not found-
- Modify a hover of the diagnostic error when input tuple size mismatch the expected size
- Modify a hover of the diagnostic error when input array dimension mismatch the expected dimension
- Modify the diagnostic error tooltip if the import failed
- Modify a hover of the diagnostic error when illegal assignment to immutable variable
- Incorrect diagnostics if the main function is missing
- Modify the error tooltip if the circuit member is called as a static constant
- Incorrect diagnostic when trying to modify a global constant
- Add an error code to the error tooltip if the test function input file cannot be found
- Fixed call chain diagnostics after Circuit inline expression and stdlib prelude classes.
- An error is not diagnosed when the integer expression in parentheses is out of range
- Fixed identifier diagnostics in Circuit variable expression.
- The error is not diagnosed if the alias type matches the global constant name
- Add diagnostics for the order between variables and constants in circuits
- The duplicate name error is not diagnosed
- Diagnostic errors of function parameter are duplicated if the function parameter is an array
- An error is not diagnosed if the type of the summand does not match the type of the expected sum
- The error is not diagnosed if the function name matches the global constant name
- A namespace conflict of global constant and circuit is not diagnosed as an error
- Correct the error tooltip if the import file is not found
- Change the error code in the message of the diagnostic error
- Add the error code to the message of the diagnostic error
- An unexpected array operation is not diagnosed if the character array is defined as a string
- Diagnostics error when there is unexpected array operation
- Comparing arrays of different lengths is not diagnosed as an error
- The import keyword is not colored after the comment
- Fixed an issue where an error was not diagnosed when calling a non-existent element of a nested array
- An error is not diagnosed when the integer expression in parentheses is out of range
- Comparing arrays of different lengths is not diagnosed as an error
- Correct the error tooltip and error highlighting if the constants section is not found
- Fixed a diagnose issue when the slice size of the array does not match the expected one
- main function cannot have annotations
- Diagnostic errors if types of integer values are defined implicitly in a tuple of tuples
- Incorrect determination of the length of a tuple when its elements end with a comma
- Fixed issue with diagnosing duplication of function input parameters
- Diagnostic error and incorrect error highlighting if the project code is invalid
- Fixed diagnostics of input file for several sections of the same name "main" and "constants"
- An "unexpected type" error is not diagnosed if you try to add/subtract arrays of different types
- "Unexpected array operation" error is not diagnosed if you try to add/subtract arrays defined as strings
- The error is not diagnosed and colors of circuit name and function name are displayed incorrectly if the circuit name matches the function name
- Fixed an issue when a type of variable is not defined correctly if it is an element of a multidimensional tuple
- Fix diagnostics if the type of the arrays sum result is explicitly defined and errors are not diagnosed
- Fix error messages when the type of the array sum result is defined explicitly
- Fix a variable tooltip if the variable is assigned an expression that has a function and an integer of undefined type
- Fix diagnostics and error messages if the type of the array sum result is defined explicitly and errors are not properly diagnosed
- An error is not diagnosed if a tuple member is assigned a value of another type
- An array element in the input file is not colored if the array consists of one integer
- An error is not diagnosed if a variable is assigned an unexpected array
- Add code to the error message if there are unexpected array operations (+, -, *, / )
- Diagnostic errors if the expression contains arrays of different length and one of the arrays is defined as a string
- An error is not diagnosed if negative index is used when slicing an array
- Diagnostic error when the code contains an expression with a function and an integer of undefined type
- Fix diagnostics when accessing tuple members
- Fix diagnostics when accessing tuple members of an undefined variable
- Fix diagnostics when accessing array members of an undefined variable
- Fix diagnostics when a 'return' command is enclosed in curly brackets
- Diagnostic error if the @test annotation is used with argument
- Fix expressions with () are not diagnosed as an error
- Fix diagnostics error code for "dead code"
- A tooltip of the undefined size array is not displayed correctly
- Expected assignment of return values for expression
- Remove registers section from examples
- Replace dash with underscore in project names
- Removed support for circuit methods
- Fix diagnostic messages when calling circuit member in the call chain
- Specify the integer type explicitly in all examples
- Fix diagnostic issue of immutability of the value of a variable
- Error is not diagnosed if the integer type is not specified explicitly
- Fix some diagnostic methods using deprecated keyword_or_identifier node
- Fix diagnostics when variable type does not match value type
- Fix circuit existence diagnostics
- Diagnostic error when defining a variable of scalar type
- Console functions should be colored purple
- Non-existing functions console.error and console.log should not be colored
- Fix error message when console.assert() function argument has wrong type
- The error is not diagnosed when the assert_eq and assert_neq functions have only one argument
- Fix diagnostics logic and messages for "dead code"
- The error is not diagnosed if the arguments of the assert_eq or assert_neq functions are of different types
- Diagnostic error if the assert, assert_eq, and assert_neq functions have no arguments
- Fix error diagnosis if the main function has no return operator
- Fix variable existence diagnostics error message
- Rewrite ErrorDiagnostic class
- Fix diagnostic errors when an expression does not have the expected assignment of return values

## [0.7.7] - 2021-08-13

### Added

- Input diagnostics of constants parameters

### Fixed

- Parse and diagnostic of math operations
- Boolean compare diagnostics
- Crash on group value validation
- Crash on return type scope parse
- Incorrect coloring of the values of group in the .leo and .in files
- Message of the input diagnostic is not correct
- An error of array definition is not diagnosed
- The expression type is not shown immediately after loading the project
- Wrong coloring of circuit type
- Incorrect highlight range for parameter input error
- A package import error is not diagnosed if the folder or file name contains an uppercase letter.

## [0.7.6] - 2021-08-06

### Added

- Defining the Self data type in a circuit member function signature.
- Show hovers over console functions.
- Self and self keywords diagnosed as an error if they used in global functions.
- Show hovers over identifier which follows after access array.
- Array index out of bounds diagnostic.
- Show hovers over identifier which follows after an access tuple and over an access tuple itself.
- Fixed diagnostic of items types in implicit inline array.
- Add annotation to Hover info over function identifier
- Completion for inputs
- Hover highlighting

## [0.7.5] - 2021-07-02

### Added

- Show Definitions of a Symbol.

### Fixed

- A duplicate of the test function is not diagnosed as an error.
- Error of diagnostics of the code with an emoji characters

### Changed

- Bugs url in market.
- Aleo Studio theme.

---

## [0.7.4] - 2021-06-22

### Changed

- Update parser to leo 1.5.2

---

## [0.7.3] - 2021-06-22

### Changed

- Aleo theme
- Extension name

---

## [0.7.2] - 2021-06-17

### Added

- Show hover over identifier of variables in constant_declaration.
- Display the path that corresponds to the node in import_declaration.
- Parentheses to methods/functions completion result.
- Hover for core.unstable.blake2s circuits.
- The const keyword of param to Hover info hover over function/method name identifier.
- Add mut/const keywords to Hover info when hovering over self keyword depending on mut/const self keyword in function_parameters.
- Show hovers over circuit variables.
- Show hover over identifier in statement_for.
- Show hover over identifier in keyword_or_identifier.
- Show hover over identifier in identifier_assignee
- Show hover over identifier in expression.
- Show hover over identifier of variables in statement declaration.
- Reduce iteration by hidden value node.
- Add imports and variables to the autocomplete list if a code is being entered in the middle of a line.
- Add autocomplete inside statement definitions.
- Show hover over identifier of circuit_variable_expression in expression_circuit_inline.
- Show hover over identifier of variable_declaration in circuit_declaration.
- Add mut/const keywords to Hover info when hovering over self keyword in function_parameters.
- Show hover over identifier in function_parameters.
- Show hover over method name identifier in circuit file definition.
- Show hover over function name identifier in file definition.

### Fixed

- The return type of circuit function is not defined.
- Incorrect definition of char array should be diagnosed and highlighted as an error.
- Function duplication is not highlighted as an error.
- The error "failed to resolve variable reference" is not diagnosed.
- Wait for WASM to finish loading.
- Fix error with replace of node in cache definitions.
- The absence of assignment of return values for expression is not diagnosed.
- Incorrect diagnostics of the if-else(ternary) expression.
- Fixed variable diagnostic when it is used as self array access index.
- The reference to the variable "self" in a static function is not diagnosed as an error.
- Incorrect diagnostics of creating a circuit through Self.

### Changed

- Update to leo 1.5.0.
- Reduce iteration by hidden value node.
- Update diagnostics for array expressions after 1.4.0 update.
- Update diagnostics for annotations after update to 1.4.0.
- Update diagnostics for address value after 1.4.0 update.
- Update Aleo Theme-color-theme

---

## [0.6.0] - 2021-05-05

### Added

- Show hover over function identifier in import definition.
- Show hover over self keyword in circuit member function.
- Show hover over type Self in circuit definition.
- Show hover over circuit identifier in circuit inline expression.
- Show hover over circuit identifier in variable definition.
- Show hover over type_circuit identifier in circuit_variable_definition.
- Show hover over type_circuit identifier in type array/tuple.
- The circuit function does not appear in the autocomplete list immediately.
- Show hover over circuit name identifier in file definition.
- Hover service: added case for a multi-line comment.
- Show hover over circuit identifier in import definition.
- Fixed arrays and tuples diagnostic.
- Show hovers over circuit variables.
- Show hovers over methods/functions.
- Add diagnostics and correct autocomplete for the deprecated 'let mut' keyword.
- Diagnostics of the code in which the integer type is not explicitly specified.
- Add diagnostic of statement definition type.
- Add assigned expression type diagnostic.
- Add integers without explicit type diagnostic.
- Add diagnostic/types of nested tuples.
- Add diagnostic of arrays with tuple syntax.
- Show hovers over methods/functions.
- Add diagnostic for operations with different types.
- Parse expression types.
- Expressions diagnostic.
- Parse tuples.
- Tuples types and diagnostic.
- Parse array type with tuple syntax.
- The Leo Language Server crashed language.
- Diagnostics of field data type.
- Implement filed diagnostics.
- Autocomplete error while typing @test annotation.
- Diagnostics of group data type.
- Add diagnostic of method calls without parentheses.
- Parse array types.
- Array data type parsing.
- Added diagnostics for address type.
- Add annotations and test function diagnostics.
- Added detailed diagnostics for integers and main diagnostics for other types.
- Check called function parameters number and types.
- Add array types diagnostic.
- Added diagnostics of mismatch between the number of expected and passed variables.
- Add diagnostic for duplicate variables.
- Add debounce for diagnostics and colorize requests.
- Added diagnostic of static/non static methods access.
- Parse imported functions/circuit methods return type.
- Remove "static" from protected list.
- Preselect major CompletionItems.
- Add Self circuit inline expression diagnostic.
- Add completions to circuit inline attributes for circuit inline initializer.
- Apply theme coloring.
- Add coloring to imported circuits/functions.
- Add command to receive plugin version and latest commit hash.
- Add support of import completion to multiple import syntax.
- Show core packages in import completions by default.
- Create import completion scope.
- Omit - from import completions after name of package if there no lib.leo file.
- Omit from import completion list current file.
- Add core blake2s package to import diagnostics and completions.
- Autocomplete imports.
- Completion item sort.
- Add completion scopes.
- Add @context parser and diagnostics.
- Check variable exists in scope. Check mutable variables. Check circuit variables and their members access.
- Colorize call of circuit method.
- Colorize function name in import.
- Colorize function name and circuit method name.
- Add circuit name colorize to imports.
- Colorize knows circuits names.
- Analyze variables.
- Diagnostic circuit inline initializer - checking the existence of circuit members.
- Add Aleo theme.
- Completion of functions/methods arguments.
- Check if called function exist.
- Added coloring for function alias in multiple import and for "as" keyword.
- Implement identifier diagnostic.
- Added diagnostics for positive numbers in array_dimensions.

### Fixed

- Incorrect diagnostics of multidimensional arrays.
- Fix the diagnostics of the number of function arguments.
- Incorrect diagnostics of multidimensional arrays.
- Fixed diagnostic of arrays inside Circuit statement definitions arguments.
- Fixed diagnostic of arrays inside function arguments.
- Invalid code is not diagnosed.
- The "missing return" error is not diagnosed and highlighted.
- Wrong diagnostic for array value arithmetic operations.
- Wrong diagnostics for nested circuits attributes.
- Wrong diagnostic for circuit name inside function.
- Wrong diagnostics of nested loop variables.
- Wrong diagnostics for parameters of mutable variable.
- Wrong diagnostics for variable defined with let keyword.
- Error on group assign expression to number.
- Error in circuit inline initialization with attribute identifier.
- Diagnostic of undefined function calls do not show correct error without parentheses.
- Fixed function arguments types diagnostic.
- Fixed diagnostic of incorrect static access syntax.
- Several identical suggestions appear in the autocomplete list when the import line is duplicated several times.
- Error highlighting remains after an error fixing.
- Fixed bugs with incorrect diagnostic of code that not parsed correctly.
- Exception on checking circuit existence in case of brackets not closed: Foo::new(
- Fixed bug with no errors when Self static access is incorrect, e.g.: Self:new();
- Fixed bug with range creating with negative number in position.
- Fixed Self static methods access.
- Fix a bug with "local folder" imports autocompletion.
- Fix completions for static methods.
- The word "static" should be highlighted as an error.
- Fix bug with static circuit member access autocomplete
- Fix bug with circuit members access autocomplete.
- Fixed Self circuit definition attributes coloring.
- Fix annotation diagnostics.
- Fixed issues with test functions calls. (Wrong diagnostic for test functions called inside test functions).
- Fix completion for circuits on definition statement.
- Wrong diagnostic for test functions called inside test functions.
- Nested project folders not parsed/diagnostic/completion.
- Completion of attributes and methods not working for uncompleted expression with expression on next line.
- Fix issues with loop index variable diagnostic.
- Fix colorize Foo::.
- FunctionParser.getFunctionAst fix throw exception.
- Colorize: issue in call of circuit method.
- Fix textmate rule for static methods.
- Colorize call of function.
- Fix colorize known circuit names.
- Fix import textmate rules.
- Fixed coloring for multiple import path when the name of import file includes a dash.
- Fixed circuit_name rule.
- Fix parsing functions statement definitions on errors.
- Wrong verification if there is no a ";" after a console function.

### Changed

- Update to leo 1.4.0.
- Add support for new leo grammar 1.2.3.
- Update to leo ast 1.2.2
- Update to tree-sitter 1.0.8
- Update Aleo Theme-color-theme
- Update to leo compiler 1.0.7
- Remove icon theme
- Update to leo parser to 1.0.4

---

## [0.3.0] - 2020-09-04

### Added

- Mutable to attributes.
- Package name diagnostics.
- Console functions diagnostics.
- Annotation diagnostics.
- Context to completion snippets.
- Circuit existence diagnostic.
- Parse workspace on IDE open event.

### Fixed

- Parser circuits and calls for new tree.
- Completion of self.
- self.x parsing.
- Functions parsing.
- Bug with imported circuits diagnostic.
- Import alias duplication in autocomplete.
- Imported files path on mac os.
- File - directory check in imports.
- Incorrect import parsing.
- Imports parser according to correct project structure.
- Imports parser.
- Fixed definition type data receiving.
- Fixed Completion service.
- Diagnostics for existing circuit.
- Diagnostics for not existing method.
- Diagnostics of empty address.
- Address value validation.
- Bug with numbers in circuit names.

### Changed

- Update autocomplete logic.
- Update tree sitter to leo.pest v1.0.3
- Update imports parser and autocompletion.

---

## [0.2.0] - 2020-08-02

### Added

- Diagnostics for pascal and snake case names.
- Functions / circuits documentation in autocomplete.
- Keyword completion.
- Basic statement definition completion.

### Fixed

- Static methods call in expressions/variable declarations/return statements.
- Issue with circuits methods duplication with aliases.
- Issue with autocomplete of second variable in expression (point.x + point.y).
- Issues with imports logic.

### Changed

- Regexp for PascalCase.

---

## [0.1.0] - 2020-07-20

### Added

- Circuits names to autocomplete.
- Import aliases to autocomplete.
- Completions for predefined functions.
- Imports parsing. Autocomplete functions/circuits from imported file.

### Fixed

- Autocomplete for statements return.
- Duplicated autocomplete from imported packages.

---

<!-- Links -->

[keep a changelog]: https://keepachangelog.com/
[semantic versioning]: https://semver.org/
[import rfc]: https://github.com/AleoHQ/leo/blob/master/docs/rfc/003-imports-stabilization.md

