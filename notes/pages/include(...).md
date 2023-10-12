- ```cmake
  include(<Filename> [OPTIONAL] [RESULT_VARIABLE <VarName>] [NO_POLICY_SCOPE])
  ```
	- > `include(...)` expects the name of a file to read in, whereas `add_subdirectory(...)` expects a directory and will look for a CMakeLists.txt file within that directory. The file name passed to `include(...)` typically has the extension .cmake, but it can be anything.
	- > `include(...)` does not introduce a new variable scope, whereas `add_subdirectory(...)` does.
	- > Both commands introduce a new policy scope by default, but the `include(...)` command can be told not to do so with the `NO_POLICY_SCOPE` option (`add_subdirectory(...)` has no such option).
	- > The value of the `CMAKE_CURRENT_SOURCE_DIR` and `CMAKE_CURRENT_BINARY_DIR` variables do not change when processing the file named by `include(...)`, whereas they do change for `add_subdirectory(...)`.
- ```cmake
  include(<Module> [OPTIONAL] [RESULT_VARIABLE <VarName>] [NO_POLICY_SCOPE])
  ```
	- Possui um significado diferente do anterior, sendo utilizado para carregar um *módulo*
	- Os 3 pontos finais da versão anterior continuam válidos