- É comum na construção de múltiplos programas a dependência de uma parte de código na outra, dessa forma é necessário um método para realizar o *link* entre essas dependências
- ```cmake
  target_link_libraries(<TargetName> [<PRIVATE|PUBLIC|INTERFACE> <Item>{1,n}]{1,n})
  ```
- Especificamente, podemos definir as seguintes relações de dependências entre duas bibliotecas $A$ e $B$
	- `PRIVATE`: biblioteca $A$ usa biblioteca $B$ nas suas implementações internas
		- Qualquer biblioteca $C$ que use $A$ não precisa saber da existência de $B$
	- `PUBLIC`:  biblioteca $A$ usa $B$ em suas interfaces e implementações
		- Qualquer biblioteca $C$ que use $A$ precisa saber da existência de $B$
	- `INTERFACE`: biblioteca $C$ que use $A$ precisa de algumas partes de $B$
		- Essencialmente, só usa na implementação
- ```cmake
  # === Exemplo de uma linkagem ===
  
  # Adição de biblitoecas
  add_library(Collector src1.cpp)
  add_library(Algo src2.cpp)
  add_library(Engine src3.cpp)
  add_library(Ui src4.cpp)
  
  # Adição de um executável
  add_executable(MyApp main.cpp)
  
  # Linkagem das bibliotecas entre si
  target_link_libraries(Collector
  					  PUBLIC Ui
  					  PRIVATE Algo Engine)
                        
  # Linkagem da biblioteca com o executável
  target_link_libraries(MyApp PRIVATE Collector)
  ```
- Existem outras variações de comando `target_` que permitem melhor controlar as dependências entre bibliotecas/programas
-