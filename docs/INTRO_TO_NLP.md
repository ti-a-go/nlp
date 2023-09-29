# Como os computadores representam línguas naturais como o português?
(Representação computacional de dados textuais)

palavras-chave: String, Unicode, Encoding

Computadores têm esse nome porque são seres que computam, ou seja, calculam. Calcular segundo o google é "determinar o valor ou grandeza numérica por meio de cálculo matemático." Isso significa dizer que computadores só sabem fazer operações matamáticas (operações aritiméticas: soma, subtração, multiplicação e divisão). Então como os computadores podem fazer operações linguísticas, ou seja, como os computadores podem entender e gerar textos em línguas naturais (pt, en, es, ...)?

Computadores entendem apenas números. Então é necessário uma forma de representar a língua através de números.
Vamos buscar um conceito de língua no livro de sintaxe do professor Mário ?????.
A língua, por sua vez, é uma sequencia de sons que representam significados. No Caso da língua escrita podemos falar em uma sequência de letras. Então o computados precisa de uma forma de representar uma sequência de sons (no caso da fala) ou letras no caso da escrita.

A forma escolhida para fazer isso foi a seguinte:

Vamos imaginar que queremos representar o alfabeto do português através de números. Poderíamos fazer o seguinte:

a = 1

b = 2

c = 3

d = 4

e = 5

f = 6

...

z = 26

O computador então seria programado para representar a palavra "café" da seguinta forma:

3 1 6 5

A partir disso é possível criar uma tabela com a representação numérica de qualquer "caracter" utilizado em qualquer língua. Essa tabela já existe e se chama Unicode. Vamo falar caracter em vez de letras para podermos incluir nesse conjunto os sinais de pontuação e outros simbolos que podemos usilizar na língua escrita.

Essa esplicação é simplista para fins didáticos, mas a solução real para esse problema de representar textos em computadores é um pouco mais complexa e será apresentado abaixo.

## Unicode

## Encoding

## Palavras & Tokens