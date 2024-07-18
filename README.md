# Desafio de um bilhão de linhas em Python #

Implementação em Python do desafio de 1 bilhão de linhas

https://www.morling.dev/blog/one-billion-row-challenge




Introdução
O objetivo deste projeto é demonstrar como processar eficientemente um arquivo de dados massivo contendo 1 bilhão de linhas (~14GB), especificamente para calcular estatísticas (Incluindo agregação e ordenação que são operações pesadas) utilizando Python.

Este desafio foi inspirado no [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc?tab=readme-ov-file#1%EF%B8%8F%E2%83%A3%EF%B8%8F-the-one-billion-row-challenge), originalmente proposto para Java.

O arquivo de dados consiste em medições de temperatura de várias estações meteorológicas. Cada registro segue o formato <string: nome da estação>;<double: medição>, com a temperatura sendo apresentada com precisão de uma casa decimal.

