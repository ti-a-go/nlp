# Como os computadores representam a língua natural?

palavras-chave: String, Unicode, Encoding

Computadores entendem apenas números. Então é necessário uma forma de representar a língua através de números. Então temos um tipo de dado especial chamado "string". Uma string é uma cadeia de caracteres. Um caracter é um simbolo representado por um número.

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

A partir disso é possível criar uma tabela com a representação numérica de qualquer caracter utilizado em qualquer língua. Essa tabela já existe e se chama Unicode.

## Unicode

