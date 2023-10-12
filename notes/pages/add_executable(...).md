- ```cmake
  add_executable(<TargetName> [WIN32] [MACOSX_BUNDLE]
  			   [EXCLUDE_FROM_ALL]
                 <Source>{1,n})
  ```
	- `WIN32`: quando o executável é construído para Windows, indica que é pra ser gerado como um *Windows GUI*. Ignorado para outras plataformas
	- `MACOSX_BUNDLE`
	  > When present, this option directs CMake to build an app bundle when building on an Apple platform. Contrary to what the option name suggests, it applies not just to macOS, but also to other Apple platforms like iOS as well. The exact effects of this option vary somewhat between platforms.
	- `EXCLUDE_FROM_ALL`: flag que indica que esse executável deve ser desconsiderado quando `ALL` (ou equivalente do gerador) é utilizado
		- Por padrão, todos os targets são construídos
		- Nesse cenário, o target só é construído se explicitamente solicitado
	- Existem outras variações
- Uma funcionalidade essencial na construção de muitos programas (e por conseguinte, da geração de *targets*) é a habilidade de utilizar bibliotecas externas: [[add_library(...)]]
- A outra funcionalidade necessária é conseguir representar a dependência de um código em outro, isso é realizado através do comando [[target_link_libraries(...)]]
-