# Acurácia (medida de desempenho)

ou score (no código)

Representa a fração de previsões corretas que você fez no seu conjunto de testes.

`Acurácia = Número de previsões corretas / Número todal de previsões`

# Dados desbalanciados

Quando temos mais dados de uma classe do que de outra. Exemplo: base de dados de emails com 99 emails não-spam e 1 email spam.

Nesses casos a acurácia não é uma boa medida

# Matriz de confusão

* cada linha representa uma classe chamada de **classe real**.
* cada coluna representa **prevista**.

A partir da matriz de confusão se extrai 4 conceitos:

* verdadeiros positivos (VP)
* falsos positivos (FP)
* verdadeiros negativos (VN)
* falsos negativos (FN)

# Precisão (medida de desempenho)

Precisão = VP / VP + FP

Todos os positivos previstos = VP + FP, 

i.e. os positivos que o algorítmo retornou.

# Revocação (medida de desempenho)

Revocação = VP / VP + FN

Todos os reais positivos = VP + FN