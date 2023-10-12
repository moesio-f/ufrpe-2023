- O `CMakeLists.txt` é o arquivo principal para se utilizar o CMake, nele são definidas o que deve ser construído, testado, empacotado bem como define como essas etapas devem ser realizadas
  title:: Visão Geral do CMakeLists
	- Ele utiliza uma linguagem agnóstica ao sistema operacional e à linguagem do código fonte
	- É um arquivo versátil que permite incluir outros arquivos (potencialmente outros `CMakeLists.txt`)
	- Ele é utilizado por um *generator* para criação dos arquivos do projeto
- Como um arquivo `CMakeLists.txt` se parece?
  ```cmake
  # Normalmente, a 1ª linha define a policy para ser utilizada.
  #	Essencialmente, isso significa que o CMake suportado
  #	precisa agir como na versão X.Y.Z.W
  # Se essa linha for omitida, o CMake gera um aviso
  #	durante o processo de geração
  cmake_minimum_requirement(VERSION X.Y[.Z[.W]])
  
  # Nome do projeto desenvolvido (letras, números, _ e -)
  # Esse nome é utilizado por alguns geradores
  project(<ProjectName>
  		[VERSION major[.minor[.patch[.tweak]]]]
          [LANGUAGES <LanguageName>])
  
  # <TargetName> pode ser utilizado
  #	para se referir a esse executável
  # Podemos ter múltiplos executáveis sendo
  #	produzidos
  add_executable(<TargetName> <Source>{1,})
  add_executable(<TargetName> <Source>{1,})
  ```