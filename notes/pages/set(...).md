- ```cmake
  set(<VarName> <Value> [PARENT_SCOPE])
  ```
- ```cmake
  set(myVar a b c) # myVar = "a;b;c"
  set(myVar a;b;c) # myVar = "a;b;c"
  set(myVar "a b c") # myVar = "a b c"
  set(myVar a b;c) # myVar = "a;b;c"
  set(myVar a "b c") # myVar = "a;b c"
  ```
- ```cmake
  set(foo ab) # foo = "ab"
  set(bar ${foo}cd) # bar = "abcd"
  set(baz ${foo} cd) # baz = "ab;cd"
  set(myVar ba) # myVar = "ba"
  set(big "${${myVar}r}ef") # big = "${bar}ef" = "abcdef"
  set(${foo} xyz) # ab = "xyz"
  set(bar ${notSetVar}) # bar = ""
  ```
- ```cmake
  set(<VarName> <Value> CACHE <Type> <Docstring> [FORCE])
  ```
	- `<Type>`: tipo de variável, pode ser `BOOL`, `FILEPATH`, `PATH`, `STRING`, `INTERNAL`
		- O principal objetivo é facilitar a manipulação em GUIs para o CMake
	- `<Docstring>`: descrição da variável
	- Detalhes: variáveis normais possuem precedência sobre variáveis de cache (existem exceções)
	  id:: 65283658-1b7c-46c5-8736-f983a1ef24e4