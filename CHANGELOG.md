# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog][keep a changelog] and this project adheres to [Semantic Versioning][semantic versioning].

## [0.46.2] - 2025-12-18

### Added
- Add error diagnostics [ETYC0372043] when a local transition function is called from a transition function
- Add [ETYC0372171] error when a struct has only zero-sized members
- Add [ETYC0372031] error when mapping key or value is zero-sized
- Add error diagnostics [ETYC0372117] when the input type of the CheatCode::set_block_timestamp method is not `i64`
- Add error diagnostics [ETYC0372034] when `block.timestamp` is not in an async block or an async function

### Fixed
- Fix an error message [ETYC0372034] when vector methods are not in an async function or an async block
- Remove false error diagnostics [ETYC0372166] when an address is a storage type
- Remove false error diagnostics [ETYC0372009] and [ETYC0372014] when using the CheatCode::set_block_timestamp method
- Remove false error diagnostics [ETYC0372065] when `block.timestamp` is used
- Remove false diagnostics when Serialize core functions are used
- Remove false diagnostics when Deserialize core functions are used
- Remove false diagnostics of errors [ETYC0372009] and [ETYC0372014] for core ECDSA functions

## [0.46.1] - 2025-12-11

### Added
- Implement error diagnostics [EPAR0370049] when modules use reserved keywords as names
- Implement error diagnostics [EPAR0370049] when reserved keywords are used as folder names that contain modules
- Add error diagnostics [ETYC0372000] when a assignment target is a vector
- Add error diagnostics [ETYC0372004] when a none is assigned to a vector
- Implement diagnostics for Optional types
- Add Help Info to diagnostic messages [ETYC0372160]
- Implement new and remove deprecated diagnostics when calling an argument from a Future
- Implement new error diagnostics [ETYC0372015] when multiple members with the same name are declared in a struct
- Implement new error diagnostics [ETYC0372016] when a record variable with the same name is declared multiple times
- Add error diagnostics [ETYC0372170] when a function is defined with  only empty parameters
- Implement error diagnostics [EAST0372017] when the same name is defined multiple times in the program scope

### Changed
- Change [ETYC0372159] to [ETYC0372160] when optional wrap a record

### Fixed
- Remove false diagnostics when optionals are defined by expressions with unsuffixed literals
- Remove false error diagnostics [ETYC0372117] when optionals are defined by unary operators with unsuffixed literals

## [0.46.0] - 2025-12-04

### Added
- Add error diagnostics [ETYC0372117] when a variable of an optional type is assigned to a storage of the same type 
- Add error diagnostics [ETYC0372167] when an assignment in a definition operation is a storage vector
- Add diagnostics for error [ETYC0372005] when creating a non-existent local struct whose name matches the name of a struct in an external program and the external struct is not used

### Fixed
- Remove error diagnostics [ETYC0372117] when a signed integer with an implicit type annotation is assigned to a signed integer storage
- Remove error diagnostics [EPAR0370021] when using pop(), push(), clear(), and swap_remove() functions associated to a vector
- Remove error diagnostics [ETYC0372117] when a struct or record is wrapped in an optional
- Remove unnecessary error diagnostics [EAST0372015] when there are two structures with the same name and the external struct is not used

## [0.45.4] - 2025-11-28

### Added
- Implement error diagnostics [ETYC0372004] when the type of expression cannot be determined
- Implement error diagnostics [ETYC0372004] when the empty array type cannot be determined
- Implement [ETYC0372166] error for invalid storage types
- Implement [ETYC0372034] error `storage write` must be inside an async function block
- Add error diagnostics [ETYC0372158] when `none is passed to a function whose input is not optional
- Implement diagnostics for the error [ETYC0372004] when `none` calls the `unwrap` or `unwrap_or` method
- Add error diagnostics [ETYC0372117] when the type that calls the unwrap_or() method does not match the type that is passed to this method
- Implement diagnostics for the error [ETYC0372159] when a record is wrapped in an optional type

### Removed
- Remove deprecated error diagnostics [EPAR0370034] for empty arrays

### Fixed
- Fix error when expected and given same array type with zero length
- Remove error diagnostics [ETYC0372004] when implicit type annotations are used in Mapping functions
- Remove error diagnostics [ETYC0372034] when using set(), and get() functions associated to a vector
- Remove error diagnostics [ETYC0372117] when using set(), and get() functions associated to a vector
- Remove error diagnostics [ETYC0372034] when `storage access` using in an async block

## [0.45.3] - 2025-11-20

### Added
- Implement diagnostics for the error [ETYC0372161] when an optional type is used as the key or value in a mapping
- Implement diagnostics for the error [ETYC0372163] when constants have an optional type or a type that contains an optional
- Implement diagnostics for the error [ETYC0372164] when inputs are or contain an optional type
- Implement diagnostics for the error [ETYC0372165] when outputs of `transition`, `async transition`, or `function` are or contain optional types
- Add diagnostics for the error [ETYC0372119] when an optional type is compared to a non-optional type
- Add error diagnostics [ECMP0376014] when an array repeat count can not be determined at compile time
- Implement diagnostics for the error [ETYC0372162] when a record field is or contains an optional type
- Implement error diagnostics [ENV03711000] when reserved keywords are invalid record member names
- Implement error diagnostics [ETYC0372160] when the type address or signature is wrapped in an optional
- Implement diagnostics when tuple, signature, or Future are wrapped in an optional
- Implement error diagnostics [ETYC0372034] when `storage access` is outside an async function block
- Implement the [ECMP0376012] error diagnostic when a non-const expression is passed to an inline function as a const generic argument

### Removed
- Remove redundant error diagnostics [EPAR0370041] when there is no comma after a member declaration in a struct
- Remove redundant error diagnostics [EPAR0370005] when the output in the function signature is defined by a reserved keyword
- Remove duplicate [EPAR0370005] error message in assert function

### Fixed
- Remove false diagnostic [ETYC0372090] when accessing Future arguments returned from an external program
- Remove false diagnostic [ETYC0372090] when accessing members of a tuple that is returned by an async transition from an external program

## [0.45.2] - 2025-11-13

### Added
- Implement error diagnostics [ETYC0372169] when a transition or function has more than 16 output parameters
- Add error diagnostics [ETYC0372117] when a core 'self' function is assigned to a variable of a different type
- Implement diagnostics for the error [ETYC0372158] when none is assigned to a type that is not optional
- Implement diagnostics for the error [ETYC0372117] when methods unwrap or unwrap_or are used to a type that is not optional
- Implement diagnostics for CheatCode::set_signer() core function
- Implement error diagnostics [ETYC0372156] when CheatCode::set_signer is called with an invalid private key
- Add error diagnostics [ETYC0372117] when the core function CheatCode::set_signer() is called with a type other than string
- Implement error diagnostics [ETYC0372168] when a transition or function has more than 16 input parameters
- Add error diagnostics [ETYC0372005] when non-existent entities are called from non-existent modules

### Removed
- Remove error diagnostics [ELUN0379000] when a loop range is decreased
- Remove redundant error diagnostics [EPAR0370009] when a tuple of constants is defined

### Fixed
- Fix an error message [ENV03711001] when record members have "aleo" in their names
- Fix error diagnostics [ETYC0372117] when the types of array members do not match the expected ones

## [0.45.1] - 2025-11-07

### Added
- Entities from the module must be available in the main program

### Fixed
- Fix error message [ECMP0376004] when the program name does not match the name specified in program.json

## [0.45.0] - 2025-11-04

### Added
- Implement error diagnostics [ETYC0372077] for the new maximum allowed array length of 512
- Implement diagnostics in modules containing inline functions and structs

### Removed
-[lsp] Remove false diagnostics when an inline function has more than 16 input parameters

### Fixed
- Fix the error loading syntax file "leo.tmLanguage" in Sublime Text
- Fix highlight range for the error [ETYC0372060] when a struct contains a member with mode constant, private, or public
- Fix the error diagnostics code when programs, records, or record members have "aleo" in their names

## [0.44.4] - 2025-10-02

### Added

### Fixed
- Fix the highlight range for the error [ETYC0372156] when a program has two constructors
- Fix highlight range for the error [ETYC0372123] when a variable type is defined as a unit type ()
- Fix highlight range for the error [ETYC0372119] when different types are received for assert operations
- Fix highlight range for the error [ETYC0372123] when the unit type () appears as the array type in the function output signature
- Fix highlight range for the error [ETYC0372032] when an input to an async function is private or constant
- Fix highlight range for the error [ETYC0372038] when a returned value is a constant

## [0.44.3] - 2025-09-26

### Added
- Implement constructor parse support for project dependencies from Location.Network

### Removed
- Remove outdated diagnostics when .env file is missing in Leo project
- Remove redundant diagnostics when a struct expression has extra members
- Remove duplicate of error message [ETYC0372002] when assigning a value to a constant

### Fixed
- Fix highlighting range for error [ETYC0372115] when an array has a Future as an element type
- Fix highlighting range for error [ECMP0376007] when a constant is defined by a variable or an expression containing a variable
- Fix highlighting range for error [ETYC0372017] when trying to create a struct of an undefined type
- Fix highlighting range for error [ESAZ0374005] when defining Future as a tuple element
- Fix a highlighting range for the error [ETYC0372154]
- Fix highlighting range for error [ETYC0372117] when a Future argument type does not match an expected

## [0.44.2] - 2025-09-25

### Fixed

## [0.44.0] - 2025-09-11

### Added
- Implement diagnostics when a constructor returns a value
- Add diagnostics when Future arguments are accessed in assert functions inputs
- Add diagnostics when a Future is awaited twice
- Add diagnostics if a Future is not awaited in the order in which it was passed into the `async` function
- Implement diagnostics for accessing Future arguments
- Add a warning [WSAZ0374003] if a Future is awaited out of the order in which it was passed to the async function

### Removed
- Remove duplicates of error [ETYC0372045] when strings not supported in Leo are compared in a condition of the if statement

### Fixed
- Remove false diagnostics when accessing a Future contained in a tuple
- Remove false error diagnostics [ESAZ0374003] when a Future type is not explicitly defined
- Remove false diagnostics when accessing a future in tuple
- Fix diagnostics errors when accessing arguments of a Future in an async block
- Remove false diagnostics when an async block contains a Future defined outside the async block
- Error [ETYC0372117] is not diagnosed when a Future argument type does not match an expected
- Fix the highlighting of the error [ESAZ0374000] and the warning [WSAZ0374001]

## [0.43.3] - 2025-08-28

### Added
- Implement a new error message [ETYC0372059] for cyclic dependency between functions
- Implement diagnostics when an entity defined in the outer scope is re-assigned in conditional scope in an async block
- Implement a new error diagnostics [ETYC0372040] if the not allowed accesses to `self` are used 
- Add error diagnostics [ETYC0372104] if not all Futures are consumed in an async block
- Add error diagnostics [ETYC0372104] when a Future contained in a tuple is not consumed

### Fixed
- Remove redundant diagnostics when an async transition returns an async function and a Future is not specified in its output signature
- Remove false diagnostics if a global constant is assigned to a struct member with the same name when a struct instance is created 

## [0.43.2] - 2025-08-21

### Added
- Add error diagnostics [ETYC0372156] when an @admin, checksum, or noupgrade constructor is not empty
- Implement error diagnostics [ETYC0372156] when a custom constructor is empty
- Implement error diagnostics [ETYC0372156] when a program has more than one constructor
- Add diagnostics when a loop bound is defined as a function argument or an expression with a function argument
- Implement diagnostics when core Program functions are used in transitions
- Implement error diagnostics [EPAR0370005] when a constructor is not preceded by the asinc keyword
- Implement error diagnostics [ETYC0372042] when a function or transition is called from a constructor

### Fixed
- Fix diagnostics when in arguments of core Program functions in program IDs, there are spaces before or after the dot

## [0.43.1] - 2025-08-15

### Changed

## [0.43.0] - 2025-08-14

### Added
- Implement error diagnostics [ETYC0372147] when a self.signer, or self.caller is used in an async block
- Implement error diagnostics [ESAZ0374011] when an async block captures more than 16 variables
- Implement diagnostics for an @admin annotation
- Implement new message for the [ETYC0372042] error
- Implement diagnostics for self.id
- Implement diagnostics for self.checksum
- Implement diagnostics when an identifier contains a double underscore `__`
- Implement diagnostics for new core functions Program::checksum(), Program::edition(), Program::program_owner()
- Add error diagnostics [ETYC0372156] when a mapping specified in @checksum annotation does not exist
- Add error diagnostics [ETYC0372156] when a mapping in @checksum annotation is invalid
- Add error diagnostics [ETYC0372156] when an @admin annotation doesn`t have an 'address' key
- Add error diagnostics [ETYC0372156] when an address in @admin annotation is invalid

## [0.42.2] - 2025-08-07

### Added
- Implement diagnostics when a variable declared outside an async block is assigned inside an async block
- Add error [ETYC0372102] diagnostics when an external transition calls are appeared after the local async block
- Implement diagnostics when accessing an argument from a future produced by an `async` block
- Add error diagnostics [ETYC0372148] if an `async` block is inside a transition, function, or inline
- Implement diagnostics when an async block is inside a loop body
- Implement diagnostics when an `async` block is inside a  conditional block
- Implement error diagnostics when transition contains more than one async entity
- Implement diagnostics when an array size is defined by a variable
- Add error diagnostics [ETYC0372042] when an `inline` is called from an async block

### Fixed
- Fix diagnostics when an `async` block contains a `return` statement
- Remove false diagnostics when struct member types are arrays whose length are defined by generics and generics are defined by constants
- Remove false diagnostics when Future from network is passed to async function

## [0.42.1] - 2025-07-31

### Added
- Implement diagnostic generic const count mismatch
- Implement diagnostics when an array repeat count is zero
- Implement diagnostics when an array repeat count more than 32
- Implement diagnostics when an array repeat count is not a valid value
- Implement diagnostics for an async block
- Implement diagnostics when a type is defined by a struct from a network
- Implement new message for the [ETYC0372067] error
- Implement new message for the [ETYC0372088] error
- Add diagnostics of the [ETYC0372067] error when Mapping or Random functions are used inside an async transition with an async block

### Removed

### Fixed
- Fix the [ETYC0372017] error range when struct member type is defined by non-existent struct with generic constants
- Remove false diagnostics when block.height or Mapping functions are used in an async block
- Remove false diagnostics when an async transition returns an async block

## [0.42.0] - 2025-07-24

### Added
- Implement diagnostics when a struct member type is defined as array whose size is defined by a generic constant
- Implement diagnostics when struct  with a generic constant defines a member type of another struct
- Implement diagnostics when an inline function declared in an external program is called
- Implement diagnostics when a generic const parameter is a tuple, array, struct, or signature
- Implement diagnostics when the declared generic constant type does not match the generic constant type in the struct expression
- Add diagnostics for unexpected generic const arguments
- Implement support for project dependencies from Location.Network

### Fixed
- Fix diagnostics when struct with a generic constant defines a member type of another struct and program tree is broken
- Remove erroneous diagnostics when the program tree is broken
- Fix diagnostics when a struct member type is array whose size is defined by a generic constant and program tree is broken
- Remove false diagnostics when a function parameter type is defined by a struct with generic constant
- Remove false diagnostics for a constant that is a struct with generics
- Remove false diagnostics when an array is a member of a struct with a generic constant

## [0.41.1] - 2025-07-17

### Added
- Add diagnostics when a transition with generic constant parameters is called from another transition
- Add diagnostics when generic const parameter is reassigned in an inline function
- Implement diagnostics for structs with const generic parameters
- Implement diagnostics when there is an invalid call of a function with generic constant parameters
- Implement diagnostics for records declared with generic constant parameters
- Implement diagnostics when constructor is used as identifier

### Fixed
- Fix diagnostics when a boundary of the external loop is defined as expression with a constant
- Fix diagnostics of types returned by external async transition
- Remove false diagnostics when a constant is defined by a non-suffix literal
- Fix diagnostics when unsuffixed literal is an array index

## [0.41.0] - 2025-07-10

### Added
- Add diagnostics when an array length is defined by an unknown variable
- Implement diagnostics of project test files
- Implement diagnostics for the new array initialization syntax
- Implement diagnostics when the type of an implicit value cannot be determined
- Implement diagnostics when argument or generic constant of the  inline function is an unknown variable
- Implement diagnostics when inline functions with generic constant parameters have the same name
- Implement diagnostics for inline functions with generic constant parameters and invalid code
- Implement diagnostics when a regular function has generic const parameters
- Implement diagnostics when the number or types of generic constant arguments are wrong
- Add diagnostics when defining an array with a length greater than the maximum value of the u32 type

### Removed
- Remove unnecessary and erroneous diagnostics for asynchronous functions

### Fixed
- Fix diagnostics when accessing a generic constant parameter

## [0.40.1] - 2025-06-26

### Added
- Add diagnosis of error [EPAR0370044] when variable identifier is more than 31 bytes
- Implement diagnostics when infering types for unsuffixed literals in binary operators or methods

### Deprecated
- Remove deprecated diagnostics when array size is defined by integer literal

### Fixed
- Fix error diagnostic [ETYC0372117] for the second operand of the mod() method
- Fix error highlighting range [ETYC0372020]
- Fix error highlighting range [ETYC0372019]
- Fix diagnostics when the target of a binary method is not explicitly defined and the second operand is an unsuffixed literal

## [0.40.0] - 2025-06-19

### Added
- Add diagnostics for loop iterator range bounds
- Implement new diagnostics for deprecated statement console
- Implement a new highlighting range for multiline errors [ETYC0372015] and [ETYC0372016]
- Implement new error message [ETYC0372110] when not async transition returns Future
- Implement new error message [ETYC0372067] when a Mapping function is used in the not async function
- Implement diagnostics when implicit hexadecimal, octal, and binary literals are used to define fields, scalars, or groups
- Add error diagnostics [ETYC0372117] when operand types do not match expected ones
- Implement new diagnostics when an implicit value is assigned to a variable
- Implement diagnostics when the type of a variable in a loop condition and types of loop boundaries are not explicitly defined
- Implement diagnostics for generic functions
- Implement new diagnostics when an unsuffixed literal is an operand of a unary method

### Removed
- Remove false diagnostics when using Poseidon8::hash_to_u8
- Remove incorrect diagnostics when a variable is defined and re-assigned in a conditional scope in an async function
- Remove diagnostics error when a Future is awaited

### Fixed
- Fix the highlighting range for the [ETYC0372062] error when the number of mappings exceeds the maximum
- Fix error message [ETYC0372018] when accessing a non-existent structure member
- Fix diagnostics when a record name is a prefix of multiple other record names 
- Fix error highlighting range [EAST0372015] when there are different structs with the same name
- Fix error highlighting range [ETYC0372026]
- Diagnostics error if a loop condition variable is used inside a loop block and its type is not explicitly defined

## [0.39.2] - 2025-06-12

### Added
- Add diagnostics for loop iterator range bounds
- Implement new diagnostics for deprecated statement console
- Implement a new highlighting range for multiline errors [ETYC0372015] and [ETYC0372016]
- Implement a new highlighting range of the [WTYC0372002] warning

### Fixed
- Fix the highlighting range for the [ETYC0372036] error when a function does not return a value
- Fix diagnostics when struct, record and transition have the same name
- Fix the highlighting range for the [ETYC0372088] error when an async transition does not call an async function
- Fix the highlighting range for the [ETYC0372113] error when a function is defined with no parameters
- Fix the highlighting range for the [ETYC0372106] error when an async function returns a value

## [0.39.1] - 2025-06-06

### Fixed

## [0.39.0] - 2025-06-05

### Added
- Implement diagnostics when a record name is prefixed by another record name
- Implement diagnostics when a ternary conditional operator is used over an external type
- Implement diagnostics when assigning to an external type record or its member 
- Implement diagnostics when assigning to an external record, a tuple containing an external record, or an external record member
- Implement new diagnostics for invalid annotations
- Implement diagnostics for annotations with arguments

### Deprecated
- Remove deprecated diagnostic: Error [EPAR0370032]: console statements are not yet supported

### Removed
- Remove deprecated diagnostics when the loop condition variable type is not explicitly defined
- Remove diagnostics error when defining the external record

### Fixed
- Fix diagnostics when unary or binary operations with integer literals are failed at compile time
- Remove unnecessary and false diagnostics of error [ETYC0372117] when implicit values define array elements
- Implement new diagnostics when a tuple is assigned to not tuple types
- Remove redundant diagnostics when a negative index is used to access a tuple element

## [0.38.7] - 2025-05-29

### Added
- Implement diagnostics when the last argument of the verify function is a mapping or a tuple
- Add diagnostics for a [WTYC0372004] warning when `self.caller` is used as the owner of record
- Implement the error [ETYC0372126] diagnostic when a record is  instantiated in the context of an async function
- Implement diagnostics when a programs, records, or record members have "aleo" in their names
- Add error diagnostics [ETYC0372134] when the loop iterator range bounds are of mismatched types

### Changed
- Update the error [EPAR0370005] message if there is an unexpected string in the program scope

### Removed
- Remove deprecated diagnostics when the variable type is not explicitly defined

### Fixed
- Fix [ETYC0372000] error message
- Fix a highlighting range of the [ESAZ0374006] error
- Implement new diagnostics when async function is not assigned to a Future
- Remove a duplicate and fix a highlighting range of the [WSAZ0374000] warning
- Remove a duplicate and fix a highlighting range of the [ESAZ0374001] error

## [0.38.6] - 2025-05-22

### Added
- Implement arrays overwrite diagnostics
- Implement diagnostics when self.caller or self.signer is assigned to a variable that is not an address
- Implement new diagnostics when a mapping write fails
- Implement new diagnostics for redefining tuple members  

### Removed
- Remove duplicate error [ETYC0372117] if a variable in the conditions of a for statement is defined as a tuple
- Remove redundant diagnostics when defining a tuple with one element

### Fixed
- Fix diagnostics of the [EPAK0375038] error when the src source directory contains two files
- Remove duplicate the [ETYC0372117] error message when a mapping read fails

## [0.38.5] - 2025-05-15

### Removed
- Remove duplicate error messages [ETYC0372117] when constants with unexpected types define loop boundaries
  
### Fixed
- Fix error message [EPAR0370004] when literal value with minus sign
- Error [ETYC0372045] is not diagnosed when the type of a function or tuple element is defined as string
- Fix the [EPAK0375040] error message if a comma is missing in the program.json file

## [0.38.4] - 2025-05-08

### Added
- Add diagnostics if the function type is defined but it does not return a value

### Fixed
- Fix diagnostics when a locator refers to the program in which it is located
- Diagnostics errors if there is a double if-else ternary expression
- Fix diagnostics when assert_eq and assert_neq functions have arguments of different types
- Remove redundant diagnostics when the argument to the assert() function is not bool
- Fix a highlighting range of the [EPAR0370005] error
- Remove redundant diagnostics when an expression whose first member is a variable calls a method

## [0.38.3] - 2025-05-01

### Added
- Implement new diagnostics when async transition returns a type that mismatch the async transition output signature
- Add diagnostics when tuple is returned by imported function and tuple index is out of tuple range
- Implement diagnostics when functions defined in external programs are called
- Implement diagnostics when external transitions return records with the same names

### Fixed
- Error [ETYC0372003] is not diagnosed when the type returned by a transition of an external program does not match the expected type
- Fix diagnostics if an async transition returns a tuple in which the Future argument does not match the expected one

## [0.38.2] - 2025-04-16

### Added
- Implement a new highlight range for error [ETYC0372072] when the number of tuple elements does not match the expected
  
### Fixed
- Diagnostics for unary and binary methods do not work if they are together with operators in an expression
- Fix multi file LeoCompilerTestsDiagnostic
- Fix a highlighting range of the [ETYC0372083] error
- Fix diagnostics if a tuple member identifier starts with an unexpected character when defining a tuple

## [0.38.1] - 2025-04-10

### Changed

## [0.38.0] - 2025-04-09

### Added
- Implement diagnostics when an external transition call is made after a local async function call
- Implement diagnostics when the arms of a ternary conditional expression have different types
- Implement new diagnostics if a type of a left-hand side of a `DefinitionStatement` is a unit type ()
- Implement new diagnostics when calling an element from a non-existent nested array or from a variable that is not an array
- Implement new diagnostics when a tuple expression has no elements
- Implement new diagnostics when the unit type appears as an array type
- Implement diagnostics for a Future element that is not the last element in the tuple
- Implement new diagnostics for operators abs(), abs_wrapper(), double(), inv(), neg(), not(), square(), square_root(), to_x_coordinate(), to_x_coordinate()
- Add diagnostics for the type cast operator
- Implement new diagnostics for Mapping operations
- Add diagnostics when local and external programs have two struct definitions with the same name that do not match
- Implement new diagnostics when computing a Pedersen commitment up to a 64-bit input
- Implement new diagnostics when computing a Pedersen commitment up to a 128-bit input
- Implement new diagnostics when computing the Pedersen hash up to a 64-bit input
- Implement new diagnostics when computing the Pedersen hash up to a 128-bit input
- Implement new diagnostics when the value of a const declaration is defined by a variable
- Add diagnostic of the Error [ETYC0372117] if the expected operator result type is not supported by the operator
- Implement new diagnostics if there is an unsigned integer with minus sign
- Implement new diagnostics if a core constant call is associated with an invalid structure
- Implement new diagnostics when a struct member is called from an entity other than the structure
- Add Help Info to diagnostic messages [EPAR0370022]
- Implement new diagnostics when an array index is not an integer type
- Implement diagnostics when upper bound of loop is greater than or equal to array size
- Implement diagnostics when the array access index cannot be determined during compilation
- Implement new diagnostics if operands of a mul() operator are invalid
- Implement diagnostics when invalid types are received for the `*` operation
- Implement new and remove redundant diagnostics for operators /, %
- Implement new diagnostics for operator add()
- Implement new and remove redundant diagnostics for operators +, -, &, |
- Implement new diagnostics for eq() operator
- Implement new diagnostics for operators gt(), gte(), lt(), lte()
- Implement new and remove deprecated diagnostics for operators >>=, <<=
- Implement new and remove deprecated diagnostics for operators +=, -=, &=, |=
- Implement new diagnostics for global and local constants definition
- Implement new and remove deprecated diagnostics when unary or binary operations are failed at compile time
- Implement new diagnostics when defining constants
- Implement a new test execution approach
   
### Changed
- Change error code and error message when a loop bound constant type mismatch a loop bound variable type
- Change [ETYC0372005] text message for unknown struct or record
- Change the error code if the array type does not match the expected one
- Change error code when block.height is assigned to a variable whose type is not u32

### Removed
- Remove redundant diagnostics if an async transition calls a non-existent async function and his name matches the function name in the external program
- Remove unnecessary diagnostics when an async transition returns an async function and the output data type in the async transition signature is not defined
- Remove unnecessary diagnostics when an async function whose parameters are futures is not called by an async transition
- Remove deprecated diagnostics for loop bounds
- Remove duplicates of errors [ETYC0372117] if the expected result type of an operator is not supported by the operator
- Remove diagnostics errors when type u64 or i64 is passed to the Pedersen128 algorithm
- Remove diagnostics errors when core functions are function inputs
- Remove redundant diagnostics when the unit type is appeared as a struct member type or as a function argument type
- Remove deprecated when a variable from a conditional scope in an async function is reassigned
- Remove diagnostics of function argument types mismatch (error [ETYC0372117]) if the arguments amount is mismatched
- Remove unnecessary diagnostics when comparing string types (operator ==)
- Remove unnecessary diagnostics when a tuple index is out of range
- Remove duplicates of error [EPAR0370029] when a tuple expression contains only one element
- Remove deprecated warnings [WPAR0370001]

### Fixed
- Fix diagnostics of multiplication operations for groups
- Fix multiplication operator diagnostics if the first operand is an unsupported 'string'
- Fix the [ETYC0372003] message if the name of the external program is specified when the variable type definition
- Fix diagnostics for error [ETYC0372003] when a type in the main program is defined by a type from an external program
- Fix error message [ETYC0372014] when there is an invalid core function
- Fix diagnostics when array index is a non-integer literal or a mapping or a struct or a function
- Fix a Help Info of the [ETYC0372030] error if a struct member is a tuple with records
- Fix diagnostics when a struct and mapping or function argument or local variable or global constant have the same name
- Fix diagnostics for error [ETYC0372058] when there is a cyclic dependency between records and structs
- There is no diagnostics for error [ETYC0372017] when an array is defined whose type is not found in the current scope
- Fix a Help Info of the error [ETYC0372109]
- Constant should be white
- Diagnostics error if `group` type enclosed in parentheses when calling constant GEN
- Fix diagnostics when an array type is defined as a tuple with one element
- Fix a highlight range for error [ETYC0372017] when an array is defined whose type is not found in the current scope
- Help Info missing in error message [EAST0372015]
- Fix diagnostics when any identifier is used to access a tuple member
- Fix diagnostics if tuple elements are expressions with binary operators
- Fix diagnostics of the error [ETYC0372017] when a struct member is called but the structure type is not found in the current scope
- No diagnostics if an expression in parentheses is entered instead of a tuple when defining a tuple
- Fix diagnostics when a type casting operator is applied to a ternary if-else operator
- Fix a highlight range for error [ETYC0372036] when the function type is defined but it does not return a value

## [0.37.3] - 2025-02-06

### Added

## [0.37.2] - 2025-01-27

### Added

### Changed

## [0.37.1] - 2025-01-10

### Added
- Add diagnostics when an expression statement is not a function call but is an external call with tuple access
- Add error diagnostics [ETYC0372003] if the type of a variable does not match the type of the value assigned to the variable and returned by the transition from the external program

### Changed

### Fixed
- Fix diagnostics when the output of an async function is not assigned to anything
- Fix a highlight range for errors [ETYC0372042], [ETYC0372107], [ETYC0372101]

## [0.37.0] - 2025-01-08

### Added
- Implement diagnostics when struct, mapping, or array contains a future
- Add diagnostics when type of variable is defined by struct from imported file
- Implement diagnostics of CheatCode algorithm
- Implement diagnostics when a constant declaration is defined as a tuple with variables
- Implement diagnostics when a call to an async transition follows a call to a non-async transition, and the async call returns a `Future` that itself takes a `Future` as an input
- Implement diagnostics for looping inner iterators
- Add diagnostics for error [ETYC0372003] when a value of another type is passed to an asynchronous function instead of a Future
- Implement `Future` used improperly diagnostic [ESAZ0374005]
- Implement diagnostics when not async functions take a Future as a parameter
- Add [ETYC0372005] diagnostics for not defined Futures

### Changed
- Change a warning code if not all paths through the function await all futures
- Change the error code when any future is never awaited
- Change warning and error codes if future is awaited more than once

### Deprecated
- Rename deprecated [ETYC0372093]
- Rename deprecated [WTYC0372003]
- Rename deprecated [ETYC0372095]/[ETYC0372097]

### Removed
- Remove redundant error [ETYC0372003] when array have a Future as an element type
- Remove diagnostics errors if the variable type is defined by a structure defined in the imported program
- Remove redundant diagnostics if an async function parameter is a constant

### Fixed
- Fix [ETYC0372003] and [ETYC0372007] errors messages when they have boolean type
- Fix highlighting of comments after mapping
- Fix error range for function parameters
- The error is not diagnosed if the function does not have a block
- Fix diagnostics for error [ETYC0372003] when a type in the main program is defined by a type from an external program

## [0.36.1] - 2024-12-10

### Added
- Speed ​​up diagnostics by implementing this process in a background thread


## [0.36.0] - 2024-12-09

### Added

### Changed

### Fixed
- Fix diagnostics when a member of a non-existent tuple is called
- Fix diagnostics when the variable identifier is a number in the assignment operator

## [0.35.1] - 2024-11-21

### Added
- Add diagnostics if identifier name is longer than 31 bytes

### Fixed
- Fix an exception error that occurs while editing the code


## [0.35.0] - 2024-11-15

### Added
- Implement diagnostics when there is no comma after the member declaration in a structure or record (except the last)
- Implement highlighting of binary, octal, and hexadecimal literals
- Add diagnostics when hex, octal, or binary literals use for not integer types
- Implement new diagnostics when a function with no parameters is defined
- Add diagnostics when negative index in tuple member access expression
- Add diagnostics when binary, octal or hexadecimal numbers are used when accessing tuple members
- Add diagnostics when an integer contains a digit that is not valid for the corresponding radix
- Add diagnostics for negative values of unsigned integers in radix 2/8/16
- The Init&Create button should not be disabled when the project name matches the name of an already existing repository

### Removed
- Remove deprecated diagnostics when defining integers in radix 2, 8, and 16
- Remove a duplicate of the error [ETYC0372003]
- Remove duplicate error [ETYC0372005] when array index is unknown variable
- Remove redundant diagnostics when declaration of 'owner' member in a record is followed by a colon
- Remove deprecated diagnostics for empty async functions
- Remove a duplicate of the error [EPAR0370005]

### Fixed
- Fix the [ETYC0372007] error message when a subtraction operator uses types not supported by that operator
- Fix diagnostics when nested tuple type is not as expected
- Fix diagnostics when the variable name is self
- Fix range of the error [EPAR0370017] if a sign and digits of a negative implicit value are on different lines
- Fix diagnostics when binary, octal or hexadecimal numbers are used in for loop as upper bound
- Fix a message of the error [ETYC0372007] if it has a mapping
- Fix the error code when a transition function has a constant input
- Fix diagnostics when accessing elements of unknown arrays
- Fix a highlighting of the Error [ETYC0372106]
- Fix diagnostics when the variable or constant name is the same as the function name


## [0.34.0] - 2024-10-29

### Added
- Implement error diagnostics [ETYC0372036] if return statements are in the inside of conditional if-else statements

### Changed

### Fixed
- Errors [ETYC0372023] are not diagnosed if tuple members are defined as members of non-explicitly typed tuples
- Fix diagnostics when the function signature is a unit expression and the return statements are inside an if-else conditional statement
- Fix diagnostics when a struct is created inside a ternary operator 
- Fix a help message of the [ECLI0377033] error when there is no ENDPOINT variable in the .env file
- Errors [ETYC0372023] are not diagnosed when non-array type variables are defined as arrays with tuples not explicitly entered
- Remove redundant diagnostics if the tuple is implicitly typed and the tuple index is out of the tuple range
- Fix explicit return type fail
- Fix diagnostics when the first operand of a comparison operator is an unknown variable
- Remove false and redundant diagnostics if there is an unexpected string instead of the struct keyword when defining a structure
- Fix diagnostics if the mapping identifier is enclosed in parentheses when calling mapping functions
- Fix diagnostics when a tuple member type is defined as a tuple
- Fix diagnostics when tuples are defined by implicitly typed tuples
- Remove redundant diagnostics when you try to call a non-existent member of an implicitly typed tuple

### Security

## [0.33.0] - 2024-09-06

### Added
- Implement diagnostics of an unknown variable if it is a member of a struct that is a tuple member
- Add diagnostics if the NETWORK variable has a new valid value of canary

### Changed
- Change links on the packagecontrol page

### Fixed
- Fix the message of the Error [ETYC0372018]
- Fix a diagnostics of errors [EAST0372006] if there are standard and transition functions with the same names
- Fix diagnostics if an unknown variable is assigned to a struct member when a struct defining
- Fix diagnostics if tuple is not explicitly typed
- Remove Error [EPAK0375038] when a file in the src folder in a nested project has a non-leo extension
- Remove Error [EPAK0375020] when a file in the src folder in a nested project has a non-leo extension
- Fix diagnostics when there is no the program.json file in the project
- Fix diagnostics if there is a syntax error in program.json
- Fix diagnostics if there is an invalid type of a variable in the program.json file
- Fix diagnostics if external transition returns a tuple whose member is a record


## [0.32.1] - 2024-08-21

### Added
- Implement diagnostics when the structure has no members
- Add diagnostics of tuples with unknown variables
- Implement diagnostics if the .env file is missing the ENDPOINT variable
- Add diagnostics if variables defined as tuple members have the same names
- Implement syntax highlighting for all languages
    
### Changed

### Fixed
- Fix diagnostics when the return statement contains the mul() method but outputs are not defined in the function signature
- Fix diagnostics when the return statement contains a binary method but outputs are not defined in the function signature
- Fix the error message [ETYC0370005]
- Fix diagnostics when a tuple contains arrays with members of different types
- Fix highlighting of the error [ETYC0372019] when there is no the variable "owner" in the record
- Fix diagnostics when there is no equals sign after the variable name in the .env file
- Implement diagnostics if  network name in the .env file is invalid 
- Fix error message [EPAR0370005] when trying to cast a primitive type to an unexpected type
- Remove the diagnostics message duplicate of the error [EPAR0370017]
- Remove redundant and incorrect diagnostics when an async transition and the async function have the same names
- Fix diagnostics when an identifier starts with aleo1


## [0.32.0] - 2024-07-10

### Added
- Implement new codes for errors that occur when unit expressions are used in a variable or constant declaration
- Implement new error codes if an invalid group core constant is typed
- Implement the new error code when an array is empty
- Implement the new error code when the program has no transition function
- Implement the new error code when an array has more than 32 elements
- Implement the new error code when a variable of the string type is defined
- Implement new diagnostics when then is a variable name
- Implement diagnostics if an async function call block is empty
- Implement diagnostics when an async function returns a value
- Implement diagnostics if an input to an async function has an incorrect mode
- Implement diagnostics when mapping methods are used outside of an async function block
- Implement diagnostics when an async transition calls a non-existent function
- Implement diagnostics if an async transition does not call an async function
- Highlight async and Future in red
- Implement diagnostics for new syntax of the finalize
- Add diagnostics for a new finalize syntax when an async function has no parameters
- Implement diagnostics when a variable is re-assigned from a conditional scope to an outer scope in an async function
- Add diagnostics if an identifier is the `async` keyword
- Implement a new error code when tuple type or tuple expression contains another tuple
- Implement a new error code when a local transition function is called from another transition function
- Implement a new error code for cyclic dependency between structs
- Implement new diagnostics for the multiplication operator
- Add diagnostics when `self.signer` or `self.caller` are used in an async function call context
- Add diagnostics and change error code if tuples on the left-hand side of a `DefinitionStatement` contain literals
- Add diagnostics when ChaCha operation is used in a transition function
- Implement diagnostics when an async transition calls a not async function
- Highlight Future in red
- External mappings should be white
- Implement diagnostics when network.id is used as allowed accesses to `network` 
- Add diagnostics when the number of async function parameters mismatch the number of inputs when it is called
- Implement new diagnostics for operation `contains` on external mapping
- Add diagnostics when a loop body inside a transition function contains an async function call
- Implement diagnostics when the type returned by an async transition is what is expected but has extra spaces and trailing commas
- Add diagnostics if a variable of Future type is reassigned- 
- Add and fix diagnostics if the output of an async function is not assigned to a `Future` type
- Highlight a Future type like when hovering
- Add diagnostics when two local async functions are called inside an async transition
- Add diagnostics if Futures that are never awaited are used
- Add diagnostics when an async function's output is not assigned of type "Future"
- Add diagnostics when an async function is called in a conditional block
- Add diagnostics when a non-async transition returns a future
- Add diagnostics when not all futures are consumed
- Add diagnostics when an async call is made from a non-async transition
- Implement diagnostics when a transition returns an async transition and the transition type is defined as Future
- Add diagnostics when the await() function is called from an unknown variable 
- Implement diagnostics when a valid core function Future::await is called
- Implement new diagnostics when two args are passed to a valid core function Future::await
- Add diagnostics if a non-boolean record member is the if statement condition
- Add diagnostics if a literal or non-future variable is passed to an async function
- Add diagnostics when a future is awaited twice
- Implement diagnostics when dependencies in the program.json file equal null
- Add diagnostics if an async function returns a Future
- Add diagnostics when the async function type is not defined as Future
- Implement diagnostics for new syntax self.address and nonexistent.aleo
- Add diagnostics when a variable of type Future is reassigned
- Add diagnostics for assignment statements
- Add diagnostics when dividing unknown variables
- Add diagnostics when an async transition returns an async function whose input is an unknown variable
- Add diagnostics when an async function's input type does not match the type of its parameter
- Implement an async function paths counter to diagnostics the error [ETYC0372092]
- Add warning [WTYC0372000] if not all paths through the async function await all futures
- Add the warning [WTYC0372001] when a future is awaited twice
- Add diagnostics of the error [ETYC0372095] when an await call is not a valid
- Add error diagnostics [ETYC0372100] if more than two local async functions are called in an async transition function
- Add a warning if the maximum depth of conditional blocks is exceeded in an asynchronous function
- Add diagnostics when trying to access a non-existent argument from Future
- Implement diagnostics when output type in async transition signature is not a Future
- Implement access diagnostics to arguments of Future
- Add diagnostics when the future argument types in the return statement do not match the future argument types in the async transition signature
- Implement diagnostics when structures and signatures are compared
  
### Changed
- Change error code when the function return value is a constant
- Change error code when loop bound is variable
- Change error code when a struct or record contains another record
- Change the help information and add it to the diagnostic message
- Change the error code when the number of tuple elements is not as expected
- Change the error code when the number of mappings exceeds 31
- Change the error code and help info for operations `set` and `remove` on external mapping
- Update to leo 2.0.0.

### Deprecated

### Removed

### Fixed
- Fix diagnostics of binary operators types
- Fix the error code if a mapping's value or mapping's key is a record
- Fix diagnostics when a number is found instead of an identifier in external resource
- Fix diagnostics when an external mapping is enclosed in parentheses
- Fix diagnostics when a struct member is called from a Future like from a struct
- Fix diagnostics when .await() operation is used in an async transition
- Fix the [ETYC0372003] error message if a variable of Future type is reassigned
- Fix diagnostics when await() function is called from literal
- Fix diagnostics when the await() function is called from a non-Future variable
- Fix diagnostics if a full and universal formats of the Future type are used
- Fix diagnostics when a non-Future variable is passed to a valid Future::await core function
- Fix hovers for async transitions and async functions
- Fix diagnostics when an async function returns a value
- Fix diagnostics when there is an empty struct
- Fix autocompletion in the program scope according to the new syntax of async calls
- Remove diagnostics error [EPAR0370009] when an unexpected constant is called from block
- Error [ETYC0372089] is not diagnosed if the parameter type of an async function is Future, but another data type is passed to the function
- Fix diagnostics when external async transition type is Future and contains program name with slash
- Remove redundant diagnostics if an invalid target is an invalid array member
- Fix diagnostics when an assignment target is a unit expression
- Fix diagnostics of external calls to .leo programs that are not supported
- Fix the error code when an unexpected constant is called from block
- Remove redundant diagnostics when the async function type is not defined as Future
- Remove diagnostics errors [ETYC0372005] when there are keywords instead of variable identifiers
- Remove diagnostics error [EPAR0372009] when there are `=` instead of variable identifiers in variable definitions
- Fix a syntax highlighting in some examples
- Highlight the return keyword in red in the Basic Bank example
- Fix a type highlighting if it is a nested Future
- Fix highlighting of hover for core function await()
- Fix diagnostics when a Future is awaited in an async transition scope
- Fix diagnostics when a variable of type Future is reassigned with the *= operator
- Fix the highlight range of the error [ETYC0372053] 
- Fix diagnostics when self.caller or [id].aleo are passed to assert functions
- Fix diagnostics when identifier starts with sign1
- Fix diagnostics when an output type in the function signature is a unit expression
- Fix diagnostics when a struct is created inside a ternary operator
- Fix diagnostics when there is no semicolon at the end of a tuple member call
- Remove duplicate of the error [ETYC0372005] when await() is called from an unknown variable enclosed in parentheses
- Fix diagnostics when output type of an async transition contains a detailed form of future 
- Fix diagnostics when a tuple whose members are arrays is defined
- Fix function highlight when calling a function whose name is wrapped in parentheses
- Fix diagnostics if the function name is in parentheses when calling a function
- Remove redundant diagnostics when a tuple index goes out of range
- Remove diagnostics errors if async function`s parameters types are universal forms of futures
- Fix syntax highlighting if a transition ends with "return;"
- Fix syntax highlighting for members of a nested struct in the return operator
- Fix diagnostics if the input of an async function is a call to an external async transition
- Fix syntax highlighting after a comment with the word `return' at the end

### Security

## [0.31.6] - 2024-05-13

### Added
- Show hovers for external mappings
- Show hovers for locators of the external program

### Fixed
- Fix diagnostics when the "network" has an unexpected value in the dependency
- Fix diagnostics when a function and a function variable have the same name
- Fix the name of the variable that is not a member of the structure in the error message [ETYC0372018]
- Fix diagnostics when a mapping, a function parameter and a function variable have the same name
- Fix diagnostics when a struct and a transition variable have the same name
- Remove redundant diagnostics when there is a non-closed string
- Fix server exception: TypeError: Cannot read properties of undefined (reading 'text')


## [0.31.5] - 2024-05-07

### Added
- Implement diagnostics if mapping operations are used on external mapping
- Add diagnostics when there is a non-existent record member in the if statement condition
- Add diagnostics when an external program has no transition function
- Show hovers for external mappings
- Show hovers for functions and external transitions
- Implement diagnostics when a struct and a transition variable have the same name

### Fixed
- Remove duplicate error message [EPAR0370009] if there is a parenthesis instead of constant identifier


## [0.31.4] - 2024-04-30

### Added
- Add diagnostics if a struct member is an array/tuple of structures of undefined type
- Implement diagnostics when in an external program standard functions  have modes associated with their inputs and transitions have constant inputs
- Implement a syntax highlighting of the 'finalize' block call
- Add diagnostics when constant inputs of functions are re-assigned
- Implement diagnostics if an external mapping is used in the mapping methods
- Add diagnostics when the `set` operation uses an external mapping
- Implement diagnostics when a variable is reassigned from a conditional scope in a finalize block
- Error is not diagnosed if the if-else statement condition is a different types comparison
- Add diagnostics if a program scope is missing

### Removed
- Remove redundant diagnostics if an external type is a keyword when defining a constant
- Remove redundant diagnostics if non-existent mapping calls mapping functions
  
### Fixed
- Fix diagnostics if creating a struct defined in current and external programs
- Fix diagnostics if an external type is a keyword
- Fix diagnostics if there is a keyword instead of a valid external type
- Fix diagnostics if a program identifier is a keyword
- Fix the highlighting of function names in Split View mode in Sublime Text
- Fix diagnostics if the array size does not match the expected one
- Fix diagnostics if the array member type does not match the expected one
- The error occurs when trying to show hover in Sublime Text
- Fix diagnostics if struct and mapping have same names


## [0.31.3] - 2024-04-23

### Added
- Add diagnostics when there is an unknown function or an external unknown variable in an expression
- Add diagnostics if the condition of the if statement is an external mapping

### Fixed
- Fix the [ETYC0372003] error message if a variable type in the for statement condition is a record that is defined in an external program
- Fix color of identifiers of external functions
- Remove redundant diagnostics when functions defined in external programs take in records defined in external programs
- Fix diagnostics if the finalize function returns a tuple that is not explicitly defined
- Fix the color of a struct member if it is returned by a function
- Fix the syntax highlight after a mapping definition if a mapping value type is is defined as an external type
- Remove redundant diagnostics when the number of function inputs is greater than the number of parameters
- Fix the syntax highlight
- Diagnostics error when a record or struct definition in the current program matches the definition in an external program
- Fix diagnostics when a function returns a struct that is defined in the current and external programs
- Fix diagnostics if a transition of an external program calls a transition of another external program


## [0.31.2] - 2024-04-16

### Added
- Add a help message to the error [ETYC0372095] 
- Implement diagnostics when trying to call an external .leo program
- Add diagnostics if a variable type is not found in the current scope when defining a variable
- Implement diagnostics when an external inline function is called
- Add diagnostics when an input type of an external function does not match a parameter type
- Implement diagnostics when a mapping's key/value is an external record
- Add diagnostics if a finalize function returns a record
- Implement diagnostics when a finalize block takes in a record as input
- Implement diagnostics if the variable type in the for loop condition is defined as an external record  
- Implement diagnostics when struct or record contains external record

### Fixed
- Fix error message [ETYC0372007] if there is an invalid network identifier when calling an external transition
- Remove redundant false diagnostics if there is any keyword instead of a variable type when defining a variable
- Fix the error message [ETYC0372028] when standard function has modes associated with their inputs
- Fix diagnostics if the condition of the if statement is a type that is defined in an external program
- Fix diagnostics if the condition of the if statement is a record member that is defined in an external program
- Fix a message of the error [ETYC0372003] if an if operator condition is a record that is defined in an external program
  

## [0.31.1] - 2024-04-09

### Added
- Add diagnostics when an expected type does not match the type that an external transition returns

### Removed
- Remove ETYC0372007 diagnostic for invalid external call when statement has integer or field type
  
### Fixed
- Fix diagnostics if the record type definition in a root program does not match the definition in an external program
- Fix diagnostics in a postfix expression that contains an external resource when there are syntax errors


## [0.31.0] - 2024-04-05

### Added
- Add types diagnostics for multidimensional arrays
- Add diagnostics if tuple members are multiplications of groups
- Add diagnostics if binary methods are enclosed in parentheses
- Implement cyclic dependency of structs according to leo code
- Show a hover for block.height, self.caller, and self.signer commands
- Add diagnostics if the defined structure has more than 32 members
- Add diagnostics when a variable returned by a function and a structure have the same name
- Implement diagnostics if the network identifier is invalid in import file syntax
- Implement diagnostics when .aleo is entered after the struct/record keyword when defining a structure
- Implement diagnostics when an invalid external type is defined
- Implement diagnostics if a struct and function parameter have same names
- Implement diagnostics when a const and function parameter have the same names
- Implement diagnostics associated with `program.json`
- Add diagnostics if a function parameter is of tuple type with one element
- Add diagnostics for an empty struct 
- Implement diagnostics if program import is not found in program manifest `program.json` 
- Add diagnostics when there is a negative variable of the unsigned type in parentheses
- Remove diagnostics errors if function name matches the function parameter names
- Add more information to the error message [ETYC0372017]
- Add diagnostics when negative variables are array members
- Implement diagnostics when a non-existent external transition is called - WIP.
- Implement diagnostics if the value type of the fields in the program.json file is invalid
- Add diagnostics when a mapping name matches variable names or function parameter names
- Implement highlighting for the new syntax of external programs import
- Add Help Info to diagnostic messages
- Implement autocomplete for imports
- Implement autocomplete for keywords 'program' and 'import'
- Add diagnostics when a program scope name does not match the import program name
- Add diagnostics if the "location" property in the program.json is missed or has an unknown value
- Add diagnostics if there is a keyword 'as' instead of an identifier of the function input parameter
- Add diagnostics if the for loop condition contains the keyword "as" instead of a variable identifier
- Implement diagnostics if the identifier of a function, variable, structure, or structure member is the keyword 'aleo'
- Add diagnostics if there is an invalid network identifier when calling an external mapping
- Implement diagnostics when the imported transition is called
- Add diagnostics if there is any keyword instead of a variable type when defining a variable
- Add diagnostics when a function parameter type is defined by a non-existent external type
- Implement diagnostics if an external structure is defined
  
### Changed

### Removed
- Remove the warning that the function must have a Snake case name
- Remove diagnostics errors when a struct name matches function parameter names or variable names
- Remove redundant diagnostics if operand types don't match and the destination type is boolean
- Remove a redundant error if a "group" literal starts with an underscore
- Remove duplicate of the error [EPAR0370018] if invalid hexadecimal number is specified
- Remove diagnostics errors when referencing an external mapping


### Fixed
- Fix an autocomplete in the empty program scope
- Fix diagnostics when the array length has leading zeros
- The autocomplete dropdown does not appear after entering boolean or scalar values
- Fix diagnostics for unary methods abs(), abs_wrapped(), double(), inv(), not(), square(), square_root()
- Fix diagnostics for unary neg() method if operand type is not supported
- Fix diagnostics for unary methods to_x_coordinate() and to_y_coordinate()
- Fix diagnostics when a double colon `::` syntax is used for not core functions
- Fix autocompletion when accessing struct elements
- Fix diagnostics when one of the keywords "function", "let", "else", etc. is entered instead of a function parameter type
- Diagnostic errors when there are numbers at the beginning of the variable identifier
- Add diagnostics if an unknown type in the chain calls the neg() method
- Add diagnostics if there are binary and unary operations in the chain
- Fix errors range if the first members of the chain are enclosed in parentheses
- Fix diagnostics when a double colon `::` syntax is used with any helper or inline function
- Remove redundant error [ETYC0372006] when an unexpected string is passed to the core function instead of an expression
- Fix an underline of the [ETYC0372003] error when the type of a nested tuple member is not as expected
- Fix error code [ETYC0372085] to [ETYC0372087]
- Fix error code [ETYC0372084] to [ETYC0372086]
- Fix a range of the error [ETYC0372052]
- Fix a range of the error [ETYC0372072]
- Fix error code [ETYC0372087] to [ETYC0372089]
- Fix diagnostics when functions have a record as input and/or output
- Fix the diagnostics error when there are structs or records with same names
- Add diagnostics when an expression is passed into a helper or inline function
- Fix diagnostics when an unary method is called by the to_x/y_coordinate() method
- Fix diagnostics when the transition parameter is an array of unknown type
- Add diagnostics when there is an unknown operand in + or - operators
- Fix diagnostics when a program does not have transition functions
- Diagnostics related to `program.json` should be displayed only in the main.leo file of the root program
- Fix diagnostics when function parameter, struct or record members are of unit type "()"
- Add diagnostics if the 'const' keyword is entered instead the identifier of a struct or record member
- Add diagnostics when units are array members
- Fix diagnostics if the string 'static' is entered before the identifier of a structure member
- Add diagnostics when a transition returns a tuple and a member of this tuple is an expression
- Fix a range of the error [EPAR0370021]
- Fix diagnostics of program id value in the 'program' field of the program.json file
- Fix diagnostics if there is any keyword instead of struct member id when calling a struct member
- Fix diagnostics when structs have the same name
- Diagnostic error messages in Leo project files are not removed after deleting or renaming those files
- Fix function call detection inside ERROR node
- Autocompletion for imports does not work if a non-existent import is added to program.json
- Fix the error of the syntax file loading when opening Sublime Text
- Fix highlighting of comments
- Add diagnostics when there are two matching struct definitions with the same name
- Fix diagnostics when a program ID value in the 'program' field of the program.json file equals empty string
- Fix diagnostics if an invalid address literal has a capital letter
- Fix diagnostics if when defining an array, instead of the expected integer literal, there is a unit expression  or a string of letters and numbers in round or square brackets
- Add diagnostics if a binary method has no target and the first operand of the method is an unknown variable
- Add diagnostics if the specified parameter type of the finalize() function does not exist
- Fix diagnostics when the length of the returned tuple is not as expected
- Fix diagnostics for the deprecated keyword `increment`
- Fixed the problem of unordered handling of Language Server events, which led to memory leaks and exceptions
- Fix diagnostics when a project is missing an .env file
- Remove diagnostic error [ECMP0376006] when importing a program, if the .leo file of this program does not exist/incorrect, but the name of this program is present in the dependencies of the manifest file
- Fix diagnostics when an incorrect .leo file in the diagnostics refers to the main project manifest file
- Fix diagnostics if an array is an input of BHP or Poseidon algorithms
- Remove redundant error [ECMP0376006] when program is imported and program.json file is invalid (prop "program" is an object)
- Remove duplicate error [EPAR0370032]
- Add diagnostics when a function that returns nothing is assigned to a variable
- Fix diagnostics when parsing errored syntax containing LF/CRLF newlines
- Remove a duplicate of the error [EPAR0370005] if there is an underscore instead an integer literal when an array defining
- Fix diagnostics if there is no PRIVATE_KEY value in the .env file
- Fix diagnostics if a "group" literal starts with an underscore
- Fix Leo syntax highlighting in Sublime Text
- Remove redundant diagnostics if an invalid expression is returned or defined
- Implement diagnostics if the identifier of a constant is a Leo language type keyword
- Add diagnostics if the identifier of a structure, mapping, function, or function parameter is a 'signature' keyword
- Logical errors should not be diagnosed within an expression where there are syntactic errors
- Fix highlighting of a return variable if its name matches the type name
- Fix error message [EPAR0370035] and error message [EUTL03710014]
- Add diagnostics if there is no function before the finalize block
- Add diagnostics when the finalize function type does not exist in the current scope
- Remove a duplicate of the error [EPAR0370005]
- Fix diagnostics when a non-existent external mapping is called
- Fix diagnostics if a variable is called from an external program for which there is no import
- Fix diagnostics when referencing own mapping as an external one
- Fix diagnostics if there is an invalid network identifier when calling an external transition or function
- Fix diagnostics if an external entry specifies a type of transition parameter
- Fix diagnostics if an external transition is accessed without specifying an external program
- Fix diagnostics if an external record defines a transition type
- Fix diagnostic error message [ETYC0372017] when a variable type is defined by a non-existent external type
- Fixed issue comparing uri with upper/lower case of drive partition (when analyzing imports)
- Language server crashed when call not assigned external function


## [0.30.0] - 2023-12-25

### Added
- Implement diagnostics when a transition function is declared with an redundant return type and curly bracket
- Add diagnostics when the expression is preceded by an opening parenthesis
- Add diagnostics of Mapping expression errors
- Add diagnostics when a finalize function calls a transition function
- Add diagnostics when a function is called from a finalize of function or from a finalize of inline
- Implement diagnostics if the function's return type is declared as a tuple of unknown type
- Implement diagnostics when an array is a struct or record member
- Add diagnostics when 'self' calls non-existent signer() and caller() functions
- Implement diagnostics when an array index is a type cast
- Implement diagnostics when a member of a constant tuple is a type cast
- Add diagnostics when an array is explicitly declared as an array of tuples

### Removed
- Remove the warning that the structure must have a Pascal case name
  
### Fixed
- Fix diagnostics for chain of mul() methods with unsupported type operands
- Remove a redundant diagnostic error if a function parameter contains public, private or constant keyword instead of a colon
- Remove redundant diagnostics error when a struct calls an invalid core function
- Fix diagnostics when a single-element tuple is defined as an array elements type
- Fix diagnostics if members of a tuple are multiplications of groups and scalars
- Remove diagnostic errors if unexpected characters follow curly brace when defining a structure
- Fix diagnostics when there is no colon after the function parameter identifier
- Fix diagnostics when assigning a regular variable or literal to an array
- Fix diagnostics when assigning an array to a regular variable
- Remove a diagnostics error if an unexpected end-of-file is found
- Fix diagnostics if a value type is missing in the mapping statement
- Fix diagnostics when variables or literals of one type are cast to another type
- Add diagnostics when an unknown variable is passed to the "finalize" function
- Add diagnostics if the keyword "then" is missing when calling the "finalize" function
- Fix diagnostics when array members are unknown variables
- Fix diagnostics if input is passed to the "finalize" function without parentheses
- Remove the duplicate of the error [ETYC0372005] when a typecast of an unknown variable is operand of Leo statements
- Fix diagnostics when array members are casting types
- Fix diagnostics if the array length is followed by one of the reserved words
- Add diagnostics when a constant in the nested loop condition has an unexpected type
- Fix diagnostics if assert functions are preceded by an opening parenthesis
- Remove redundant diagnostics errors [ETYC0372003]


## [0.29.0] - 2023-12-08

### Added
- Implement the removal of symbols in the terminal on the playground
- Implement diagnostics of cyclic dependency of structs when struct members are struct arrays
- Add the advanced Token example to the playground
- Implement improved error diagnosis logic when the tree is broken
- Add diagnostics if the variable in the for loop condition is an array
- Add diagnostics if the tuple expression contains an unexpected string instead of a closing parenthesis
- Implement diagnostics when the right side of a variable assignment statement has an unexpected symbol instead of an expression 
- Implement diagnostics of cyclic dependency between functions when one function is called from the finalize of another function
- When loading the page, show the command corresponding to the current example in the terminal

### Fixed
- Fix diagnostics when a tuple whose members are tuple variables or tuple constants are assigned to a tuple
- Fix incorrect behavior and display in the terminal after resizing the browser window on the playground
- Remove a duplicate of the error message when an array element is an unknown variable
- Fix diagnostics errors when array type and array elements are defined by a unit expression
- Fix diagnostics for binary methods chaining
- Fix diagnostics when a constant of an outer for loop is used in a nested for loop
- Errors are not diagnosed if the first operand of a binary operator is enclosed in parentheses
- Fix diagnostics if a defined struct member is followed by a string of unexpected characters instead of a comma
- The cursor constantly jumps in the .env area on the playground
- Fix diagnostics when the syntax tree breaks and redundant errors occur if there is an unexpected non-semicolon string in the program area
- Fix diagnostics if there are underscores or leading zeros in the length of the array when defining an array
- Fix diagnostics when after the transition type an arbitrary string placed instead of the expected opening curly brace
- Fix diagnostics if the array element type is not as expected type
- Fix diagnostics if a tuple type contains an unexpected string instead of a closing parenthesis
- Remove redundant diagnostics for binary methods chaining
- Remove redundant diagnostic error when instead of a transition type we have a string with numbers at the beginning or with special characters anywhere
- Remove redundant diagnostic errors when a standard function is defined as a member of a struct
- Fix diagnostics if the program definition has unexpected symbols or numbers instead of a curly brace
- Remove redundant diagnostics if there is an unexpected numeric string with an underscore
- Remove redundant diagnostics if there is no semicolon at the end of the expression
- Remove redundant diagnostics errors if there are underscores or leading zeros in the length of the array
- Fix diagnostics in a chain of binary operators when the first operator in the chain is the operator '*' for group
- Fix an underline of the [EPAR0370009] error when there is an unexpected characters line at the beginning of the Leo expression
- Remove redundant diagnostics errors if an invalid expression contains a comparison sign
- Remove redundant diagnostics errors of function parameters types
- Fix diagnostics if the array type is placed in several lines
- Remove redundant diagnostics when referencing a tuple element without an index
- Critical error "TypeError: Cannot read properties of null" when hovering over a variable


## [0.28.0] - 2023-11-09

### Added
- Reorganize playground windows
- Add to the playground a CLI section that allows user to run bash commands and Leo transitions
- Add a hover over to a variable that is defined outside the for loop but is used inside the loop
- Implement array data type support for function inputs, return type and variables
- Implement the clear command for clearing the terminal screen on the playground
- Implement diagnostics for access to array elements
- Implement a help command to be output whenever an unsupported command is entered into the terminal emulator in the playground
- Add diagnostics when an assignment target is an array element
- Color the literal of the array length blue
- Show hover an array when array element accessing
- Implement support for array expression
- Implement comparing array items to type
- Add diagnostics for array items passed into function parameters
- Implement left and right cursor movement in the terminal on the playground using the left and right arrows
- Add diagnostics if a const variable from for loop condition is reassigned

### Changed
- Update advanced examples according to terminal functionality

### Removed
- Remove support for .in files
- Remove 'Inputs' and 'Run' ondoarding-description windows on the playground
- Remove Run dropdown from playground and Run buttons in leo code from playground and VS Code

### Fixed
- Fix diagnostics of binary methods types
- Fix types diagnostics of the binary method mul()
- Fix hovering over a for loop variable
- Fix parsing of parameters wrapped in quotation marks for leo commands on the playground
- Fix types diagnostics of binary methods eq(), and neq()
- Fix types diagnostics of binary method pow()
- Fix types diagnostics of binary methods shl(), shl_wrapped(), shr(), shr_wrapped(), pow_wrapped()
- Fix issue when multi-line command is displayed incorrectly in the playground terminal if it is pasted on the bottom line
- The Backspace button in the terminal on the playground does not work correctly if the command is inserted using the CTRL+V
- Fix diagnostics if the array is explicitly passed to the helper or inline function
- Fix diagnostics if arrays are used when structures, records or mappings are defined, created and used
- Fix diagnostics when the array is explicitly passed to the finalize function
- Fix diagnostics if the number of array elements exceeds 33
- The record keyword should be red when hovering over a record
- Show hovering over a for loop constant inside of the loop
- Fix diagnostics of array elements types
- Fix incorrect behavior when pressing backwards/forward/backspace keys if the command length is wider than the terminal area on the playground


## [0.27.0] - 2023-10-17

### Added
- Add diagnostic for mapping shadow
- Add diagnostic for function shadow 
- Implement diagnostics if the self.signer operand is used in a finalize context
- Add diagnostic for record shadow
- Add diagnostic for struct shadow
- Mismatch tuple length
- Implement the definition of the absence of a variable among constants
- Implement diagnostics [EPAR0370009] when constants are defined using tuple
- Implement diagnostics when reassigning constant
- Color the async keyword purple
- Color the const keyword red 
- Implement diagnostic for constant shadow
- Implement [ETYC0372062] diagnostic for constant
- Implement [ETYC0372023] diagnostic for constant
- Implement [ETYC0372080] diagnostic for constant
- Add diagnostics when the value of a const declaration is not a literal
- Implement constants diagnostics
- Show hover for global constants
- Implement diagnostics when the constant identifier is enclosed in parentheses when constant defining
- Add Tic Tac Toe example back to playground
- Color the 'self' and 'await' keywords purple
- Add a "const" item to the autocomplete dropdown

### Fixed
- Fix the [ETYC0372043] error message when there is not allowed access to 'self'
- Fix error code [ETYC0372078] to [ELUN0379000]
- Remove an unnecessary diagnostic error when comparing literals of the signature type
- Fix diagnostic of incorrect definition of function parameter mods
- Fix diagnostics of the signature comparison
- Fix error definition [ETYC0372049] to [ETYC0372081]
- Remove redundant diagnostics when comparison operators gt(), gte(), lt(), lte() contain two addresses
- Diagnostics errors when defining the type of the constant
- The color of the shr method must be green
- Fix an underline of the Error [ETYC0372054] when defining a constant
- Fix diagnostics if the member of the global tuple constant is called
- Fix error message when expected boolean type does not match input type
- Fix diagnostics when a variable is first used and then defined
- Fix diagnostics, hovers, and error messages if there are spaces between tuple member types when defining a tuple


## [0.26.0] - 2023-10-04

### Added
- Improve ui for deploy and execute dialog 
- Implement diagnostics of Keccak256, Keccak384, and Keccak512 algoritms
- Implement diagnostics of SHA3_256, SHA3_384, and SHA3_512 algoritms
- Add diagnostics if a mapping and a variable in the transition scope have the same name
- Tuples on the left-hand side of a `DefinitionStatement` can only contain identifiers

### Changed
- Update onborading flow
- Updated tooltips for deploy and execute dialogs

### Removed
- Remove unnecessary examples from playground
  
### Fixed
- Fix the "Report an issue" link on the playground
- Fix diagnostics when a mapping is assigned a value
- Remove a warning about the name of the pascal case for SHA3_ methods
- Fix diagnostics if there are mappings with the same name
- The hover over SHA3 and Keccak should be red
- Fix diagnostics if there are no address type operands in gt(), gte(), lt(), lte() operators, but there are operands of other unsupported types
- Fix diagnostics when the types of the first and second arguments don`t match in the comparison operators gt(), gte(), lt(), lte()
- Fix diagnostics if the entered destination type of operators gt(), gte(), lt(), lte() is not supported (is not boolean)
- Fix diagnostics of the maximum number of mappings if there are mappings with the same name
- Fix the [EPAR0370005] error message
- Fix diagnostics if target variable type is not supported by square_root() function
- Fix an issue that caused the server to run slowly by removing the previous unnecessary syntax tree that was overflowing memory
- Fix diagnostics if a transition returns a method of an expression in parentheses


## [0.25.0] - 2023-09-26

### Added
- Add diagnostics if the verify() function is called by the non-signature and the destination is not defined as boolean
- Add diagnostics when the address value is not valid in the input file

### Fixed
- The input records in the examples on the playground does not belong to the signers
- Remove a redundant diagnostic error if a function parameter contains a duplicate function name instead of a colon
- Fix diagnostics when there is an integer with several minus signs
- Fix an error message if the number of inputs is not as expected
- Fix the error underlining when the used struct is not defined in the program scope
- Fix diagnostics if the literal in the input file is out of range
- Add diagnostics when the structure defined in the import file is used
- Fix diagnostics when comparison operators gt(), gte(), lt(), lte() contain an address
- Fix diagnostics if a signature value in the input file is invalid
- Remove duplicate error message when address value is not valid
- Changes in the input file are diagnosed only after the playground is reloaded
- Fix diagnostics when the underscore character in the signature value is in the inside or immediately after sign1
- Add diagnostics if the verify() function is called by not a signature and the first argument is not an address
- Fix the message of the Error [ETYC0372003] with mapping
- Fix a problem with a series of transitions running without waiting for the previous call to complete on the playground


## [0.24.0] - 2023-09-12

### Added
- Implement diagnostics if private key length is invalid 
- Implement diagnostics if there is no private key in the .env file
- Implement diagnostics if the account private key prefix is invalid
- Update the Aleo Instructions grammar for structs highlighting
- Color the signature type green 
- Add diagnostics if the verify() method is called by a not "signature" type
- Implement autocomplete for signature methods
- Show hover for the verify() function and signature type parameters and variables
- Color the literals that contain underscores
- Color the numeric literals that contain underscores

### Fixed
- Fix diagnostic [ETYC0372078] for code containing numbers with underscores
- Fix diagnostics if the last parameter of the verify() function is a signature
- Fix diagnostics when the signature type parameter is defined in the input file
- Fix diagnostics when tuple index contains underscores or leading zeros
- Fix error messages if the assert_eq() or assert_neq() function argument is an unknown variable
- Fix diagnostics if a numeric literal that contains underscores is a function argument
- Fix diagnostics if there is a literal with underscores
- Fix an error message if a transition expects a literal but gets a struct
- Fix diagnostics if the value of the literal with underscores is out of range


## [0.23.3] - 2023-09-07

### Added
- Implement diagnostics when there is an import call from a non-leo file
- Implement diagnostics if there is no dot after an import file name
- The error is not diagnosed when trying to import a file that does not exist
- Implement diagnostics if the import file identifier is missing from the import declaration
- Implement diagnostics if there is no semicolon at the end of the import declaration
- Implement diagnostics if there is no .env file in the leo project
- Implement diagnostics of the 'signature' type
- Add diagnostics if the loop range is decreasing

### Changed
- Change Leo/Aleo code toggle styles

### Removed
- On change active editor tab set the Leo color scheme

### Fixed
- Fix diagnostics if the casting operator is enclosed in double parentheses and is not followed by a semicolon
- The unique identifier of the application disappears after Reset
- Fix diagnostics when {},:;=?/+-[]() characters follow a dot in an import file
- Fix file type in error message when imported file does not exist
- Remove diagnostic errors that appear on the playground after entering any character
- Fix the underlining of the error when a digital string follow a dot in an import file
- The color of the file names in import declarations must be completely yellow
- Remove a diagnostic error that appears on the playground after entering two characters


## [0.23.2] - 2023-08-28

### Changed
- Rebrand color scheme

### Fixed


## [0.23.1] - 2023-08-25

### Changed
- Rebrand with new logos and color scheme


## [0.23.0] - 2023-08-24

### Added
- Implement records and structures coloring in input files on the playground
- Implement diagnostics when the exponent type is u128
- Implement record members and struct members coloring in input files
- Add diagnostics of conditional AND and conditional OR statements
- Implement diagnostics when the signed integer type of the base of the exponent matches the type of the exponent
- Add diagnostics for `&` and `|` operators
- Add missing diagnostics for the exponentiation operator
- Implement the Deploy/Execute functionality in the Playground
- Implement an error [EPAR0370005] diagnostics when a string that starts with numbers or special characters is found instead of a variable type
- Implement diagnostics if function name is not identifier

### Fixed
- Fix an underlining of the error [ETYC0372007] for conditional AND and conditional OR statements
- Fix critical issue in the implementation of hovers on circuit/struct
- Fix critical issue in the implementation of hovers on Mapping methods
- Fix critical issue when function name is not identifier
- Fix diagnostics when instead of defining a struct member we have an expression starting with a keyword


## [0.22.0] - 2023-07-24

### Added
- Implement diagnostics when a struct member in the input file is incorrect
- Implement autocomplete feature for group static methods and group instance methods
-  Show parameter modifiers when hovering over a finalize and transition functions
- Add types diagnostic when a cast statement is an expression operand
- Implement .env file support according to Leo 1.9.0 on the playground
- Show hover for inline functions
- Add diagnostics if the cast statement contains an implicitly typed tuple
- Add diagnostics of Mapping::contains and Mapping::remove methods when the type of the method's argument does not match the expected

### Fixed
- Fix diagnostics where there is an unexpected string after a cast statement instead of a semicolon
- Fix diagnostics when casting a type of a statement second operand
- Fix diagnostics when a cast operator has an unexpected string instead of a cast type
- Fix diagnostics if a Leo program is named 'increment' or 'decrement'
- Fix diagnostics if the first struct member declaration is followed by spaces
- Fix autocomplete feature of static methods
- Fix diagnostics when an unexpected string follows an annotation
- The 'private' modifier is not shown when hovering over functions
- Remove redundant diagnostic error if a cast expression contains an unexpected string instead of a cast type


## [0.21.0] - 2023-07-12

### Added
- Show hover over for the transition and finalize functions
- Implement autocomplete for Mapping methods
- Add hover for mapping
- Implement autocomplete for BHP, Pedersen, Poseidon and ChaCha methods
- Implement hover for ChaCha 


## [0.20.0] - 2023-07-07

### Added
- Implement diagnostics when  a `finalize` statement is used without a `finalize` block
- Implement diagnostics when a double colon `::` syntax is used for access to a struct member
- Implement structure initialization expression diagnostics if the structure is defined multiple times
- Implement diagnostics when transition inputs are not defined in the input file
- Add diagnostics when Mapping core functions are used outside of the finalize block
- Implement diagnostics of the ChaCha::rand core functions
- Add diagnostics when ChaCha:rand core functions are passed an unexpected args number
- Add diagnostics when ChaCha::rand core functions are used outside of the finalize block
- Implement diagnostics of Mapping::contains and Mapping.remove core functions
- Implement diagnostics of to_x_coordinate() and to_y_coordinate() group core functions
- Implement diagnostics of remove() and contains() operators
- Implement diagnostics of to_x_coordinate() and to_y_coordinate() group core functions when the function's argument is not a group
- Implement diagnostics of the types casting 
- Add diagnostics when trying to cast a field to a group or address
- Add diagnostics when trying to cast an address, group, or field to a boolean type
- Add diagnostics if more than sixteen inputs are added to function
- Show hover over for record and record variables

### Fixed
- Fix diagnostics when BHP, Pedersen, and Poseidon core functions contain a mapping or tuple argument
- Fix diagnostics when a scalar or integer literal is cast to another type
- Fix a diagnostics error when a struct member is cast to a different type
- Fix tooltip when hovering over a record variable or struct member


## [0.19.0] - 2023-06-23

### Added
- Implement diagnostics if a Leo program does not have transition functions
- Implement diagnostics for BHP, Pedersen, and Poseidon core functions of Leo compiler v.1.8.0
- Implement diagnostics when a finalize function contains a self.caller operand
- Implement diagnostics when a finalize block contains a finalize statement
- Implement diagnostics when "mapping" contains a tuple or any special character as type
- Implement diagnostics when mapping and transition have the same name
- Add diagnostics if Mapping core functions contain a variable defined as self.caller
- Implement diagnostics of the block.height command

### Fixed
- Fix diagnostics if there is no curly bracket after the function type
- Fix diagnostics when several functions that are not associated with a given type are called consecutively
- Add diagnostics when a function parameter has an identifier `scalar`
- Fix diagnostics message for incorrect type of binary methods argument
- Fix diagnostics when hash_to_integer core functions of BHP, Pedersen, and Poseidon contain mapping or unit expression
- Fix diagnostics of commit_to_... core functions of BHP, and Pedersen
- Fix diagnostics if self.caller operand is in a finalize context


## [0.18.0] - 2023-06-15

### Added
- Implement diagnostics when there is an unexpected space between a number and a type
- Add diagnostics when a tuple expression contains multiple other tuples
- Add diagnostics when a tuple member type is not found in the current scope
- Implement diagnostics if there is no "=>" sign in the mapping statement
- Add diagnostics if a finalize function contains a return statement and returns a value but an output from a finalize function is not defined
- Add diagnostics if the assert() function argument is an unknown variable
- Implement diagnostics when the mapping value is defined as a record and the mapping functions set the mapping value to a not record
- Add diagnostics for group constant
- Implement diagnostics if Mapping functions are not inside a finalize block
- Implement diagnostics when a "string" type is the type of the first argument of BHP, Pedersen, and Poseidon functions
- Implement diagnostics when comparing string values
- Implement diagnostics when a function returns an unknown struct

### Fixed
- Fix underline of [ETYC0372015] and [ETYC0372016] errors when `struct` and/or `record` are defined with more than one member with the same name
- Fix an underlining error when calling a variable of nested non-existent structure
- Fix diagnostics if a comparison statement contains an unknown variable
- Fix diagnostics if a condition type in the `if` statement is not `boolean`
- Remove a duplicate of the error message when a tuple expression contains an unknown variable
- Fix diagnostics when a `finalize` block returns a value
- Fix an underline of the [ETYC0372003] error when assert_eq() and assert_neq() functions contain arguments of different types
- Fix error message [EPAR0370009] when the assert() function has no argument
- Fix diagnostics if a function argument is a tuple instead of a value
- Fix incorrect diagnostics for group:GEN
- Remove redundant diagnostics when the struct member type is a tuple with nested tuples
- Fix diagnostics when a nested tuple is typed implicitly
- Remove a duplicate of the error message when there are unexpected spaces between a number and the `group` or `field` type
- Fix diagnostics when the variable type does not match the return type of the Mapping methods
- Fix diagnostics if an assert function argument type is not boolean
- Implement diagnostics if the negative zero is an unsigned integer
- Fix an underline of the [ETYC0372048] error when a transition function calls another transition function
- Fix missing core functions incorrect diagnostics BHP256::commit_to_group, BHP256::hash_to_group, BHP512::commit_to_group, BHP512::hash_to_group, BHP768::commit_to_group, BHP768::hash_to_group, BHP1024::commit_to_group, BHP1024::hash_to_group, Pedersen64::commit_to_group, Pedersen64::hash_to_group, Pedersen128::commit_to_group, Pedersen128::hash_to_group, Poseidon2::hash_to_group, Poseidon2::hash_to_scalar, Poseidon4::hash_to_group, Poseidon4::hash_to_scalar, Poseidon8::hash_to_group, Poseidon8::hash_to_scalar
- Fix diagnostics if a function type is public or private and enclosed in parentheses
- Fix diagnostics if a return statement in the if-else operator is enclosed in curly braces
- Fix a diagnostic of the error [EPAR0370005] when a program name is entered incorrectly
- Fix a diagnostic of the error [EPAR0370009] when we have a keyword instead of a program identifier
- Fix diagnostics when calling a member of the unknown variable 'group'
- Fix a diagnostics error [EPAR0370005] when there is no dot after the program identifier
- Fix diagnostics when calling an unknown member of the variable type not struct
- Fix diagnostics if an invalid core constant is called
- Fix an underline of the [ETYC0372071] error when a finalize block returns a value
- Fix an underline of error [ETYC0372025] when an unreachable operator is enclosed in curly braces
- Add diagnostics when a "string" type is the type of the second argument of commit(), and commit_to_group() functions for BHP and Pedersen
- Fix diagnostics if the program definition has an unexpected string instead of a curly brace


## [0.17.1] - 2023-05-24

### Fixed
- Fixed files watcher settings [issue](https://github.com/sublimelsp/LSP-leo/issues/3)

## [0.17.0] - 2023-05-24

### Added
- Implement diagnostics when an identifier is missing from the finalize function
- Implement diagnostics when a standard function definition is missing its identifier
- Implement diagnostics when there is an impossible negative type
- Add missing diagnostic for [ETYC0372060] error
- An error is not diagnosed if there are no semicolons at the end of the expressions
- Implement diagnostics when an unknown variable is a function input
- Implement diagnostics when both commas and semicolons are used to declare record member variables
- Add diagnostics if there is a colon instead the struct member type
- Add missing diagnostic for `"` before `}`

### Fixed
- Fix incorrect underlining of error [ETYC0372003]
- Fix error message [ETYC0372012]
- Fix diagnostic message when there is an unsigned negative value with spaces
- Fix incorrect shift expression diagnostic
- Remove a duplicate of error message for duplicate variables
- Remove incorrect diagnostic for maximum number of mappings
- Remove diagnostic with required gates in record
- Fix an error underline and an error message if a key type is missing in the mapping statement
- Fix diagnostics if a value type is missing in the mapping statement
- Fix diagnostics if the struct type is not found but the struct member is called
- Fix diagnostics when inputs types of BHP and Pedersen functions are unexpected
- Fix diagnostics when a struct has 'owner' or/and 'gates' variables
- Fix diagnostics if there is an unexpected symbol or keyword instead of a struct or record identifier 
- Fix diagnostics when both commas and semicolons are used to declare structure member variables
- Fix diagnostics if there is an unexpected symbol or keyword instead of a struct or record identifier
- Fix diagnostics if there is an unexpected symbol or keyword instead of a mapping identifier
- Remove duplicate error message if a keyword is a structure member identifier
- Fix underline of [ETYC0372031] error if a function has an empty `finalize` block
- Remove duplicate of [EPAR0370009] error message if a keyword is a structure identifier

## [0.16.0] - 2023-04-28

### Added
- Implement diagnostics when function and argument of other function have the same name 
- Implement diagnostics when a finalize name does not match a function name
- Implement diagnostics when a helper or inline functions have a finalize function
- Implement diagnostics when a function doesn't contain a 'finalize' statement
- Implement diagnostics when transition number exceeds the maximum
- Implement diagnostics if there is an unexpected string in the for statement
- Implement diagnostics when the tuple index is negative value
- Implement diagnostics when the tuple definition statement does not contain tuple members
- Implement diagnostics if a type of the increment/decrement parameters is not an expected
- Implement diagnostics when a finalize block parameter is a constant or private
- Implement diagnostics if there are unicode bidi override code points in the comments of Leo program
- Implement diagnostics when a finalize block takes a tuple as input
- Implement diagnostics when an output from a finalize block is private
- Implement diagnostics when in a for statement there are literals of scalar, group, field, address, or boolean types
- Implement diagnostics when arguments of BHP, Pedersen, and Poseidon static methods are unknown variables
- Implement diagnostics if a colon is missing after the struct member identifier
- Implement diagnostics when a keyword is used as an identifier of mapping, function, struct, transition
- Implement diagnostics if a deprecated increment/decrement function is used
- Implement diagnostics when a function returns a tuple, whose members have a constant mode
- Add diagnostics when there is an invalid core function call in tuple element access syntax
- Implement diagnostics if a colon is missing after the struct member identifier
- Add diagnostic for division not supported for scalar types.
- Add diagnostic for cyclic dependency between structs
- Add diagnostic for `const` word in input files.
- Add diagnostic for redundant modes in input files
- Add diagnostic for multiple modes in input files
- Add diagnostic for incorrect section definition in input files
- Add diagnostic for `?` symbol in annotations arguments
- Add diagnostics for checking types between values in boolean operations
- Add missing diagnostic for incorrect syntax of access mapping value with `[]`
- Implement diagnostics when a record is a mapping's key or value
- Implement diagnostics when inline functions have modes associated with their inputs.
- Implement diagnostics when a member of a structure has a value of type "string"
- Fix diagnostics when the transition parameter type is defined as 'string'
- Implement diagnostics if function type is "string"
- Implement diagnostics if the value mapping type is 'string'
- Add diagnostics when an invalid static methods of the Mapping class are called
- Add diagnostic for hex numbers
- Add diagnostic for `'}` symbol combination
- Implement diagnostics if an inputs type of the Mapping functions is not as expected

### Fixed
- Fix error message when a `function` keyword is used as an identifier of mapping, function, struct, inline, or transition
- Implement diagnostics if there are increment/decrement statements inside a transition, function, or inline
- Fix diagnostics when a transition parameter has a private mode
- Fix error message [ETYC0372027]
- Remove redundant diagnostics error when there is an annotation @program in a program scope
- Remove the sub() method from autocomplete dropdown for scalar type
- Add diagnostics for all structs from cyclic dependency
- Fix quotes in error message [ETYC0372003]
- Fix diagnostics when there is a subtraction operator in the comparison operator
- Fix diagnostics when a scalar is multiplied by a group in a comparison operator
- Fix quotes in error message [ETYC0372047] and [ETYC0372066]
- Fix diagnostics when a function is called that is defined multiple times with the same name
- Fix quotes in error message [ETYC0372013]
- Fix diagnostics error when a identifier of the transition or function parameter is "const"
- Fix diagnostics if there is a whitespace between the `@` symbol and the annotation identifier
- Diagnostics error when a tuple index out of range
- Fix quotes and bool to boolean in the error message [ETYC0372003]
- The Leo Language Server crashes when trying to parse a broken struct/record
- Fix diagnostics if in the program there are symbols that are not used or prohibited in the Leo language
- Missing diagnostics Could not determine the type of
- Remove incorrect diagnostic for arithmetic operations with boolean comparison
- Fix incorrect diagnostic message and underline for incorrect syntax with mut keyword.
- Fix diagnostics if there is no semicolon before or after the return statement
- Fix diagnostics when there are structs/records with the same name
- Remove redundant diagnostics errors when a semicolon is missed after the expression
- Fix diagnostics when a tuple member is called from a variable of another type
- Fix incorrect underline of the error when a struct member type is defined as `string`
- Fix diagnostics when a tuple expression contains another tuple expression that is typed implicitly
- Fix incorrect underline of the error [ETYC0372054]
- Fix diagnostics when a structure/record member's type is undefined or incorrect
- Fix diagnostics when a struct member is called from a non-struct
- Remove redundant diagnostic errors when a program contains structures with the same name and different parameters
- Fix a diagnostics of error [ETYC0372042] when a finalize function arguments are undefined
- Fix incorrect the error underlining when a struct initialization expression is missing a member
- Add diagnostics if a nested tuple has several members whose types don`t match the defined
- Diagnostics error when there are white spaces between terms 'minus' and 'field' or 'group'
- Fix diagnostics when the deprecated `async finalize` construct is used in a transition function
- Fix diagnostics when arguments of transitions/functions/inlines are unknown variables
- Fix bool to boolean in all error messages [ETYC0372003]
- Fix incorrect underline of the error when a finalize block is empty
- Fix incorrect diagnostic underline for function empty return with record return statement
- Fix incorrect underlining of error when there is an unexpected space between a number and the terms `field` or `group`
- Fix diagnostics when a record variable type does not match the defined one
- Remove duplicate errors [ETYC0372005] when passing an unknown variable to a functions
- Fix diagnostics when a function returns a tuple, whose members have a private mode
- Fix diagnostics when there is an exponentiation expression in the comparison operator
- Fix diagnostics when a function returns a tuple, whose members have a constant mode
- Update diagnostic messages for Pedersen `hash` function
- Fix diagnostics if the number of function inputs does not exceed sixteen
- Update diagnostic message when the number of transitions exceeds the maximum
- Fix diagnostic of type of required record field "gate"
- Fix incorrect diagnostic message for `'` symbol
- Diagnostics errors when static methods of the Mapping class are used
- Fix diagnostics for mapping type associated methods
- Fix an error code in a statement declaration when the right-hand side is an expression with associated functions

## [0.15.0] - 2023-03-22

### Added
- Implement diagnostics if an invalid type is specified when defining a variable or any structure
- Implement diagnostics if the gates keyword is a struct identifier
- Implement diagnostics when a standard function has a finalize block
- Implement diagnostics when cyclic dependency of helper and inline functions
- Implement diagnostics if a helper function outputs a record
- Add diagnostics for mapping arguments in increment function
- Add diagnostic for use `finalize` after `function`
- Add diagnostics for struct or record inside record
- Add diagnostic for `self.` with unknown property
- Add diagnostic for shadow mapping name by function name

### Fixed
- Diagnostics error if there are several functions with the same name
- Fix quotes and underline coordinates in error message [ETYC0372003]
- Fix incorrect underline in diagnostic of undefined function
- Fix diagnostics when a function parameter type is undefined
- An error is incorrectly highlighted when the structure member type is not found in the current scope
- Fix quotes and bool to boolean in the error message ETYC0372003
- Diagnostic error when the function returns a unit expression
- Fix diagnostics when a tuple expression or tuple type has one element
- Fix quotes in error message ETYC0372013
- Fix incorrect diagnostic underline for expected `,` in arguments
- Fix incorrect underline in diagnostic where function must return value
- Fix incorrect underline in diagnostics when type not found in current scope
- Fix incorrect underline in diagnostic for `finalize` expression without finalize block
- Fix incorrect underline in diagnostic for `finalize` expression arguments check
- Fix incorrect underline in diagnostic when function argument type not found
- Fix incorrect underline in diagnostic when group tuple expression forbidden has white space
- Incorrect underline in diagnostic for unreachable statement
- Add diagnostics for strings in if statement and fix underline for error in definition
- Fix incorrect underline on diagnostic for not found type in statement declaration
- Fix diagnostics when defining a variable of type record if the record variables are defined with mode
- Fix diagnostics when struct members have `private`, `public`, or `constant` mode
- Fix diagnostics of variable types in inline function
- Extra spaces in error messages [ETYC0372003], [ETYC0372006] and [ETYC0372007]
- Fix diagnostics when a comparison operator contains another comparison operator with a negative variable
- Fix error message [ETYC0372021]
- Fix diagnostics when Pedersen methods contain unsupported types
- Implement diagnostics when cyclic dependency of helper and inline functions
- Fix diagnostics when an application scope contains an unexpected character instead of the keywords "inline", "function", "transition" and so on
- Fixed incorrect parsing structs with an error
- Fixed incorrect autocomplete dropdown if the cursor is positioned to the left of the semicolon
- Fix Leo Language Server errors caused by the rem operator
- Diagnostic errors, if in the process of calculating expressions after the division operation, the intermediate result is less than one
- The autocomplete list should not freeze with the title "Loading..." 
- Fix diagnostics if an output from a finalize block is defined as constant
- Fix diagnostics if inputs to a finalize block are defined as constant
- Implement diagnostics if a `finalize` name does not match a transition name
- Implement diagnostics if a transition function does not contain a `finalize` statement

## [0.14.0] - 2023-03-08

### Added
- Implement diagnostics when the type of the exponent is not field when exponentiating a variable of type field
- Implement diagnostics when a variable type is not specified after the colon in the condition of the for statement
- Implement diagnostics when a struct has members with 'constant', 'private', or 'public' modes
- Implement diagnostics when tuple type or tuple expression contain another tuple
- Implement diagnostics when cyclic dependency of struct
- Implement diagnostics when a struct member type is a record
- Implement diagnostics when a transition function calls other transition functions
- Implement diagnostics if a colon is missing after the struct member identifier
- Implement diagnostics when integer values ​​are out of range in comparison operations

### Fixed
- Fix diagnostics of conditional OR operator
- Implement diagnostics when the type of the second member of the pow operator does not match the expected types
- Fix the error code when the record is defined with more than one variable with the same name
- Fix the error message when the struct is defined with more than one member with the same name
- Fix diagnostics when a helper function calls itself
- Fix diagnostics of conditional AND operator
- Fix diagnostics when a transition, function, structure, or record does not have an identifier
- Fix autocomplete of Core Unary and Binary methods

## [0.13.0] - 2023-02-28

### Added
- Implement diagnostics when the type of the exponent is not field when exponentiation a variable of type field
- Implement diagnostics when a variable type is not specified after the colon in the condition of the for statement

### Fixed
- Fix autocomplete dropdown in the transition scope so that variables, parameters, assert operators, helper functions, inline functions, etc. are present

## [0.12.0] - 2023-02-24

### Added
- The error is not diagnosed when the variable defined in the condition of the for statement is defined again
- The error is not diagnosed if the types of integer in the functions arguments are not defined explicitly
- Implement diagnostics when transition returns an unknown variable
- Implement diagnostics when there is  an unknown variable in the if-else statement condition
- Implement diagnostics when a comment block is not closed
- Implement diagnostics when struct contains a tuple
- Implement diagnostics when a variable name starts with a number
- Implement diagnostics when standard function and variable have the same name
- Implement diagnostics when inputs number does not match number of transition parameters
- Implement diagnostics when instead of a struct parameter we have a keyword
- Implement diagnostics if there is an implicit integer value in the arithmetic expression
- Add diagnostics when the type of inputs does not match type of arguments of transition function
- Implement diagnostics when a standard function has no inputs
- Implement diagnostics when "mapping" contains a types that are not defined in the current scope
- Implement diagnostics when a type of input does not match a type of transition argument, regardless of the input's name
- Implement diagnostics when a struct member is an assignment target
- Implement diagnostics if a mapping key is a tuple
- Implement diagnostics when a function and its argument have the same name
- Implement diagnostics if there is an expression instead of an identifier when defining a variable
- Implement diagnostics when a tuple member is an assignment target  
- Implement diagnostics when a function takes a tuple as input
- Implement diagnostics when the type of a number power is not as expected
- Implement diagnostics when integer values ​​are out of range in Leo methods
- Implement diagnostics when a transition return a tuple
- Implement diagnostics when the variable type is defined as a tuple with one member
- Implement diagnostics when there is an expression with data of different types and a variable with a minus sign
- Implement diagnostics if an expression result that contains a Shift statement is out of range
- Implement diagnostics when the tuple member type is not as expected
- Implement types diagnostics for shift left and shift right operators

### Changed
- Change the word circuit to the word struct in all error messages
- Changed the Record and Struct data type details in the data type autocomplete dropdown

### Removed
- Remove redundant diagnostic errors when the program ends with an unexpected eof
- Remove redundant diagnostic errors when the program contains non-Latin letters or emoji
- Remove a redundant diagnostic error when at least one member of an expression is out of range

### Fixed
- Add error diagnostics and fix error highlighting when variable type is defined as string, which is not yet supported
- Fix diagnostics when trying to assign a new value to a constant
- Fix diagnostics error code when there is constant parameter in the standard function
- Remove redundant diagnostic error when an unknown variable is used to create a record
- Fix diagnostics when a transition whose type is not defined returns a value
- Diagnostic error when functions return empty braces ()
- Fix diagnostics when the type of the function parameter and the type of the value passed to the function do not match
- Fix diagnostics when transition parameters have a same names
- Fix error code when deprecated data type circuit is defined
- Fix and implement diagnostics when instead of a variable identifier we have a keyword
- Diagnostics error when a transition returns a value in parentheses and also has a type in parentheses
- Fix error code when called function doesn't associate with variable type
- Remove a 'SnarkVM' string from the diagnostics error messages
- Remove duplicates of error messages
- Handling the case of no transition/struct in the cache when diagnosing a transition_declaration/struct_declaration node
- Diagnostic error when the first argument of the BHP commit function is a struct
- Fix diagnostics when the program contains non-Latin letters or emoji
- The Leo Language server crashes if an input type is undefined
- Fix diagnostics when the type of an integer value is defined incorrectly
- Diagnostic error when self.caller is used in a finalize function comparison statement
- Diagnostics error when comparing struct
- Diagnostics error when accessing a variable, if the identifier of this variable is enclosed in quotation marks when defining it
- Fixed: Implement diagnostics when a tuple member is an assignment target
- Fixed diagnostics related to unexpected EOF
- Diagnostic errors when the expression contains a power of a number
- Fix highlighting of the error [ETYC0372003] for unary operators
- Diagnostic errors when variable names match type names
- Fix diagnostics when the transition type is a tuple with a public member but the type of that tuple member is not specified.
- The unary and binary operators should be fully highlighted when error [ETYC0372007] occurs
- Implement diagnostics when an integer value in the Shift statement is out of range
- Diagnostic error when in the Shift Statement a type of a right-hand side does not match a type of a left-hand side
- Fix autocomplete dropdown in the program area for the new Leo syntax
- Fix and add diagnostics when unit expressions are used in expressions of the Leo program
- Fix autocomplete dropdown menu of the data types
- Added finalize definition to autocomplete dropdown in the program area
- Fix diagnostics error when a tuple is assigned to a variable that is not defined as a tuple
- Diagnostics error when you call an inline function
- Fix diagnostics when assignment statement has no expression at the right-hand side
- Fix diagnostics when the type of the first member of the pow statement is a field
- - [lsp] Fix diagnostics when a record has members with 'constant', 'private', or 'public' modes

## [0.11.0] - 2022-12-26

### Added
- Implement diagnostics when a variable type in for statement condition is a tuple, struct, field, group or scalar
- An error is not diagnosed if the values type in the condition of the for statement are not specified explicitly
- Diagnostics does not define the tuple member type
- Add diagnostics when instead of the program identifier we have a keyword
- Change the word circuit to the word struct in all error messages

### Fixed
- Remove redundant diagnostic error when an extra member is used for initialization of struct
- Fix diagnostic error message when expected tuple length does not match tuple length in tuple definition expression
- Remove redundant diagnostic error when a transition returns a ternary if else statement with types that do not match the transition type
- Diagnostics is not correctly if the left operand in the bitwise shift operator has an unexpected type
- Diagnostics error when the spaces number between the minus sign and an unsigned integer is greater than one

## [0.10.2] - 2022-12-13

### Changed

## [0.10.1] - 2022-12-13

### Added
- Diagnostics for console keyword.

### Changed
- Color for assert, assert_eq, assert_neq functions.

## [0.10.0] - 2022-12-13

### Added
- Implement diagnostics when a loop bound is a variable
- Implement diagnostics when there is an unknown variable in the condition of the for statement
- Implement diagnostics when a variable type in the condition of the for statement is not defined
- Implement diagnostics when there is an unknown annotation
- Implement autocomplete for Leo language
- Implement diagnostics when there are spaces between a minus sign and unsigned integer

### Fixed
- Fix a diagnostics when a struct and function have the same name
- Fix error message when a tuple member type does not match with expected in the definition statement
- Fix diagnostic errors when the identifier of struct parameter is preceded by a special symbol or number

## [0.9.0] - 2022-12-07

### Added
- Implement parser and cache for aleo files
- Added feature to execute certain Leo transition function on the playground
- Implement go to definition for aleo
- Added diagnostics when a return statement is missing from the finalize function
- Implement diagnostics when the finalize block is empty
- Implement diagnostics of unsupported strings
- Implement diagnostics when transition function has a constant inputs
- Implement diagnostics when the finalize statement is not preceded by the async keyword
- Implement diagnostics when the number of finalize arguments is not as expected
- Error is not diagnosed if there are several programs with the same name in a Leo file
- Implement diagnostics of duplicated structs and records
- Implement a diagnostic if there is no colon after the identifier of the variable being defined
- Implement diagnostics when a record member type is a tuple
- Diagnostics for deprecated async finalize.
- Implement hover for aleo.
- Implement diagnostics when a struct or record contains another record
- Implement diagnostics when two record variables with the same names are defined
- Implement diagnostics when a variable name starts with a number
- Implement diagnostics when the type of the transition function parameter is undefined
- Implement diagnostics when the struct parameters values are implicit and undefined
- Implement diagnostics when a struct member has an unknown type 
- Implement diagnostics when a struct and a variable inside of transition function have the same name
- Implement diagnostics when there is unknown type in definition

### Changed

### Fixed
- Diagnostic error if the return statement has no value or invalid string
- The problem with different colors of syntax highlighting
- An error is not diagnosed when the function returns unsupported comparisons ">", "<", ">=", "<=" for address types
- Error message and target node when a function has no return statement
- An errors are not diagnosed when the function returns unsupported comparisons ">", "<", ">=", "<=" for group types
- Diagnostic error when instead of a variable identifier we have a keyword
- Remove invalid diagnostic error "Identifier can not be protected name"
- Fix error message when a standard function has a public argument
- Fix diagnostics message when the number of transition function arguments is not as expected
- Diagnostic error when there is not allowed access to 'self'
- Fix diagnostics if curly bracket of the program scope is missing
- Diagnostic error if string "input" is a variable name
- Fix diagnostics if a transition/finalize/helper functions type is defined as a constant
- Diagnostic error when adding variables of 'group' type
- Diagnostic error when multiplying group and scalar variables
- Fix diagnostics if a transition/finalize/helper functions type is defined as a reserved keyword
- Diagnostic error when logic operation between scalar types
- Diagnostic error when transition/finalize/helper functions return a public value
- Shadowed by diagnostic coordinates and message code
- Diagnostics for invalid assignment target
- Diagnostic error if transition/helper functions have an invalid type
- Fix an error message if the type of record members is not as expected
- Fix diagnostics when transition/helper functions have the same name
- Fix an error message when record initialization is missing member owner or gates
- Fix diagnostic when function argument type is not defined
- Fix diagnostic when there is a space instead of a struct/record field
- Remove the redundant error message when transition/helper functions type is declared as public but the type itself does not exist
- Diagnostic error when defining the tuple type of a transition function/helper function/variable if there is no closing parenthesis
- Fix diagnostic error message when called function not found
- Fix diagnostic when transition/helper functions type is declared as public but the type itself does
- Fix diagnostic when the type of the second transition/helper function argument is not defined
- Fix the error code when the next statement cannot be reached
- Fix the error code when a loop body contains a return statement
- Diagnostic error if the right-hand side of the logical statement is an arithmetic expression or a value with a minus sign
- Diagnostics error when a transition function returns a ternary if-else statement
- Diagnostics error when there is any invalid string with a semicolon at the end
- Diagnostics error when instead of a transition type there is a string with numbers at the beginning or with special characters anywhere
- Fix the error code when there are two program scopes in a Leo file
- Diagnostics error when checking the statement_assign, it is not possible to find transition/helper function that contains it
- Fix error message when an instance of a non-existent struct is defined
- Fix error message when a non-existent struct member is called
- Fix error code when a struct contains a record
- Fix error code when a struct defined with more than one member with the same name
- Fix an issue with determining the type of a tuple member
- Diagnostic error when the transition function does not contain a return statement but returns an empty tuple

## [0.8.40] - 2022-10-28

### Added
- Diagnostics on editor open event
- Diagnostics on change active editor event
- The error is not diagnosed if a variable is used before it is defined
- An implicit type integer is not diagnosed as an error if it is contained in a function's return expression
- An error is not diagnosed if the values type in the condition of the if-else statement are not specified explicitly

### Fixed
- Fix diagnostics when a variable is defined outside a transition function.

## [0.8.39] - 2022-10-21

### Added
- Add diagnostics when the network identifier is not `aleo`
- Add diagnostics when there are no curly braces after the network identifier in the application scope definition
- Add diagnostics when a standard function calls another function 

### Fixed
- Add diagnostics for the deprecated keyword 'circuit' after transition function
- Fix diagnostics when there are no 'program' or 'import' keywords at the beginning of Leo program
- Fix incorrect error code when there is an implicit integer value

## [0.8.38] - 2022-10-20

### Added
- Add diagnostic for incorrect program scope name
- Add diagnostics for the deprecated keyword 'circuit'

### Fixed
- Fix diagnostic of if-else ternary statement
- Diagnostic error of the decrement() function

## [0.8.37] - 2022-10-17

### Fixed
- Diagnostic error of field and group type values
- Fix diagnostics of parameters passed to the function
- The parenthesis after the increment() and decrement() function names are purple but should be white
- Diagnostic error when calculating the integer expression
- Diagnostics error when defining the finalize() function
- A valid 'not equal' statement for integers is diagnosed as an error

## [0.8.36] - 2022-10-14

### Added
- Implement a parse of transition function

### Fixed
- The parenthesis after the function name is purple and should be white
- Incorrect definition of data types of parameters in transition

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
- Aleo theme.

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

