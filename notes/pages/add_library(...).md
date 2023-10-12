- O CMake oferece o comando `add_library(...)` para lidar com o uso de bibliotecas externas ao projeto sendo desenvolvido
- No geral, esse comando possui a seguinte sintaxe:
  ```cmake
  add_library(<TargetName> [STATIC | SHARED | MODULE]
  			[EXCLUDE_FROM_ALL]
              <Source>{1,n})
  ```
	- Essencialmente, possui o mesmo formato que o `add_executable(...)`
	- O tipo para construção da biblioteca tem os seguintes significados:
		- `STATIC`:  biblioteca/arquivo estático (normalmente, `<TargetName>.lib` no Windows e `<TargetName>.a` em Unix-like)
			- Essencialmente, significa que o código da biblioteca é incluído no executável em tempo de compilação
		- `SHARED`: biblioteca compartilhada/dinamicamente linkada. `<TargetName>.dll` no Windows, `<TargetName>.so` em Unix-likes e `<TargetName>.dylib` em sistemas Apple
			- Essencialmente, significa que as funcionalidades da biblioteca não são incluídas no executável e devem ser resolvidas durante tempo de execução
		- `MODULE`: biblioteca quase-compartilhada mas que deve ser carregada dinamicamente em tempo execução (no lugar de ser linkada diretamente ao executável)
			- Normalmente, são plugins ou componentes opcionais
		- Uma prática comum é não definir o tipo de construção, a não ser que o projeto tenha alguma particularidade
- Para mais informações sobre Linguagens Compiladas, acessar [[Implementação de LPs]]