- Adiciona um outro diretório no contexto de build, esse novo diretório precisa possuir um `CMakeLists.txt`
	- Não é necessário utilizar o comando `project(...)`, mas é permitido
		- Se definido, novos arquivos podem ser gerados pelo CMake
	-
- O formato geral do comando é:
  ```cmake
  add_subdirectory(<SourceDir> [<BinaryDir>] [EXCLUDE_FROM_ALL])
  ```
	- `<SourceDir>` não precisa ser diretamente um sub-diretório do contexto atual, podemos utilizar um caminho relativo ou absoluto
	- `<BinaryDir>` pode ser omitido (CMake criará um caminho `<SourceDir>` no diretório de build atual) ou passado
	- `EXCLUDE_FROM_ALL` permite remover os *targets* presentes em `<SourceDir>` do `ALL` do contexto atual