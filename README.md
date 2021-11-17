# Minha experiência escrevendo um interpretador BrainFuck com a ferramenta RPython

## Introdução e contextualização

Esse repositório surgiu após eu ter assistido a esse vídeo no YouTune ["Pixie - A Lightweight Lisp with 'Magical' Powers" by Timothy Baldridge](https://www.youtube.com/watch?v=1AjhFZVfB9c&list=WL&index=2). No vídeo o palestrante fala sobre um nova implementação de [Lisp](https://pt.wikipedia.org/wiki/Lisp) que ele estava desenvolvendo fazia algum tempo, hoje esse projeto está parado. A parte importante é que o palestrante, além de falar sobre essa nova implementação de Lisp chamada [Pixie](https://pixielang.org/), explica como o interpretador foi construindo com o uso das "ferramentas" [RPython](https://rpython.readthedocs.io/en/latest/translation.html) e porque essas ferramentas foram escolhidas. Ele argumenta que há muito potencial e recursos prontos para a construção de interpretadores diversos no ambiente RPython. Essas ferramentas são usadas no desenvolvimento do interpretador [PyPy](https://www.pypy.org/), um interpretador Python alternativo ao CPython (o interpretador mais conhecido). Então, logo após o término do vídeo comecei a pesquisar tutoriais para aprender um pouco mais sobre RPython, acabei encontrando esse link [Tutorial: Writing an Interpreter with PyPy, Part 1](https://morepypy.blogspot.com/2011/04/tutorial-writing-interpreter-with-pypy.html), que é o tutorial base que deu origem a esse repositório, hoje tenho dois propósitos com esse repositório: ter um interpretador BrainFuck funcional, e por funcional digo que consiga executar uma parcela considerável de programas escritos na linguagem; ter um exemplo de um programa RPython para usar como material no futuro para possíveis outros interpretadores.

## Material principal

Os links do tutorial usado como base seguem abaixo, os dois primeiros são os links no blog original, conforme fui lendo descobri que o blog havia sido migrado para o servidor principal do projeto PyPy, por isso incluí os links dos posts no servidor novo logo a abaixo.
**Ainda não realizei a segunda parte do tutorial.**

* [Tutorial: Writing an Interpreter with PyPy, Part 1](https://morepypy.blogspot.com/2011/04/tutorial-writing-interpreter-with-pypy.html)
* [Tutorial Part 2: Adding a JIT](https://morepypy.blogspot.com/2011/04/tutorial-part-2-adding-jit.html)

* **Links novos:** [Tutorial: Writing an Interpreter with PyPy, Part 1](https://www.pypy.org/posts/2011/04/tutorial-writing-interpreter-with-pypy-3785910476193156295.html)
* **Links novos:** [Tutorial Part 2: Adding a JIT](https://www.pypy.org/posts/2011/04/tutorial-part-2-adding-jit-8121732841568309472.html)

### Sobre o material e o turorial

Partes do código do tutorial não estavam bem explicadas para mim, mesmo copiando e colando o código no arquivo o programa não rodou e quando rodou, não rodou corretamenta. Infelizmente os repositórios citados no tutorial já não existem mais, pelo menos não nos mesmos links. Fazendo uma pesquisa rápida na internet não fui capaz de encontrá-los através de outros nomes. Optei por gastar meu tempo entendo como completar o interpretador. Como não havia mais código de referência acabei lendo mais sobre a linguagem em questão e terminando o interpretador, no final acabei corrigindo bugs e aderindo ao modelo mais comum de interpretadores BrainFuck, com células de 8 bit sem sinal e com "wraparound", quando há overflow segue contando do zero ou quando ha "underflow" segue contando do 255.

## Requerimentos técnicos

Nesse repositório você vai encontrar duas versões do interpretador, uma para ser executada usando Python3 e a outra para ser executada com Python2 e principalmente para ser usada na criação do executável nativo atraves do processo de build das ferramentas RPython. Ambas as versões estão dentro da pasta `src` e possuem indicação da versão que contém no próprio nome. A versão python3 se chama `bf-interpreter__python3.py` e a versão python2/RPython `bf-interpreter__python2-rpython.py`

## Clonando o projeto

Esse projeto repositório contém dois interpretadores BF, um python3 e outro python2/RPython. Se sua intenção é apenas testar a versão python3, pode clonar o repositório normalmente.

```bash
# clonando
$ git clone https://github.com/marcoswitcel/bf-interpreter-rpython.git
```

No entanto, se quiser testar a versão RPython, deixei algumas conveniências configuradas. O projeto código fonte do interpretador PyPy e os scripts de build que vamos usar são hospedados aqui [https://foss.heptapod.net/pypy/pypy](https://foss.heptapod.net/pypy/pypy). O Heptapod usa [Mercurial SCM](https://www.mercurial-scm.org/), um gerenciador de código fonte diferente do Git, por este motivo, só conseguirá o source clonando usando um client [Mercurial](https://www.mercurial-scm.org/) ou baixando o ".zip" do repositório. Para simplificar, encontrei um [Espelho do repositório do PyPy](https://github.com/mozillazg/pypy) aqui no Github e adicionei como submodulo do meu projeto versionado pelo Git. Então se quiser pode clonar usando a flag `--recurse-submodules`. Enfatizo que, não tenho controle sobre esse repositório Mirror externo e que, portanto, não posso garantir a qualidade nem a segurança do código lá espelhado. Por isso seria o ideal baixar o código necessário direto do repositório original disponível aqui [https://foss.heptapod.net/pypy/pypy](https://foss.heptapod.net/pypy/pypy).

### Caso considerar esse espelho seguro, segue o comando para clonar o repositório com o submodulo junto

```bash
# Clonando com os submodulos juntos
$ git clone --recurse-submodules https://github.com/marcoswitcel/bf-interpreter-rpython.git
```

### Outra opção

Link direto para o zip do repositório hospedado no Heptapod, se o link não mudar com o tempo é só clicar, baixar, dezippar e mover para dentro deste repositório.

* **Link do zip** [https://foss.heptapod.net/pypy/pypy/-/archive/branch/default/pypy-branch-default.zip](https://foss.heptapod.net/pypy/pypy/-/archive/branch/default/pypy-branch-default.zip)

### Executando a versão Python3

```bash
# navegue até a raíz do projeto
$ cd bf-interpreter-rpython
# execute o arquivo "bf-interpreter__python3.py" da pasta "src"
# e passe como argumento o caminho de algum dos programas presentes
# na pasta "bf-programs-samples", como por exemplo o programa "hello-world.b"
$ python src/bf-interpreter__python3.py bf-programs-samples/hello-world.b
Hello world!

```

### Executando a versão Python2

```bash
# navegue até a raíz do projeto
$ cd bf-interpreter-rpython
# execute o arquivo "bf-interpreter__python3.py" da pasta "src"
# e passe como argumento o caminho de algum dos programas presentes
# na pasta "bf-programs-samples", como por exemplo o programa "hello-world.b"
$ python src/bf-interpreter__python2-rpython.py bf-programs-samples/hello-world.b
Hello world!

```

### Realizando o build com RPython

```bash
# navegue até a raíz do projeto
$ cd bf-interpreter-rpython
# Execute o script de build "pypy/rpython/bin/rpython", eu usei o próprio
# interpretador pypy para realizar o build, mas qualquer interpretador
# python2 deve funcionar, a parte mais complexa tem relação com a configuração
# dos compiladores C/C++, como realizei o build usando o
# Windows Subsystem for Linux (WSL), os compiladores no meu Ubuntu já
# estavam configurados. O processo de build demora um minuto mais ou menos
$ python pypy/rpython/bin/rpython src/bf-interpreter__python2-rpython.py
# Ao final você terá um executável chamado "bf-interpreter__python2-rpython-c"
# para executar seus programas BF basta digitar o nome do interpretador
# seguido pelo caminho do programa
$ ./bf-interpreter__python2-rpython-c  bf-programs-samples/hello-world.b
Hello world!

```

## Material suplementar

Links de materiais que usei para complementar a minha implementação do interpretador

* [Link do Gist com material adicional de como funciona e como implementar um "interpretador" BrainFuck](https://gist.github.com/roachhd/dce54bec8ba55fb17d3a)
* [Outro interpretador BF usado para fins de comparação](https://github.com/joshhoughton/PyFuck/blob/master/pyfuck.py)
* [Material sobre o comportamento esperado de "wrapping"](https://www.reddit.com/r/brainfuck/comments/7o2bxx/what_does_wrapping_mean/)