# Desafio de um bilhão de linhas em Python #

Implementação em Python do desafio de 1 bilhão de linhas.  

Inspirado pelo [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc?tab=readme-ov-file#1%EF%B8%8F%E2%83%A3%EF%B8%8F-the-one-billion-row-challenge), originalmente proposto para `Java`.

https://www.morling.dev/blog/one-billion-row-challenge


## Introdução
O objetivo deste projeto é demonstrar como processar eficientemente um arquivo de dados massivo contendo 1.000.000.000 de linhas (~14GB), especificamente para calcular estatísticas (Incluindo agregação e ordenação) utilizando Python.

O arquivo de dados consiste em medições de temperatura de várias estações meteorológicas.  
Cada registro segue o formato `<string: nome da estação>;<double: medição>`, com a temperatura sendo apresentada com precisão de uma casa decimal.

Exemplo de Dados:

``` csv

Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
Cracow;12.6
Bridgetown;26.9
Istanbul;6.2
Roseau;34.4
Conakry;31.2
Istanbul;23.0

```

O desafio é desenvolver um programa Python capaz de ler esse arquivo e calcular a temperatura mínima, média (arredondada para uma casa decimal) e máxima para cada estação, exibindo os resultados em uma tabela ordenada por nome da estação.

| station     | min_temperature | mean_temperature | max_temperature |
|-------------|-----------------|------------------|-----------------|
| Abha        | -31.1           | 18.0             | 66.5            |
| Abidjan     | -25.9           | 26.0             | 74.6            |
| Accra       | -24.8           | 26.4             | 76.3            |
| Albuquerque | -35.0           | 14.0             | 61.9            |
| Alexandra   | -40.1           | 11.0             | 67.9            |
| ...         | ...             | ...              | ...             |
| Yangon      | -23.6           | 27.5             | 77.3            |
| Yaoundé     | -26.2           | 23.8             | 73.4            |
| Yellowknife | -53.4           | -4.3             | 46.7            |
| Ürümqi      | -42.1           | 7.4              | 56.7            |
| İzmir       | -34.4           | 17.9             | 67.9            |

## Dependências

Para executar os scripts deste projeto, você precisará das seguintes bibliotecas:

* Polars: `0.20.3`
* DuckDB: `0.10.0`
* Dask: `^2024.2.0`

## Resultados

Os testes foram realizados em um notebook com Linux Mint 21.3 equipado com um processador 13th Gen Intel(R) Core(TM) i7-13800H e 62GB de RAM.  

As implementações utilizaram abordagens puramente Python, Pandas, Dask, Polars e DuckDB.  

Os resultados de tempo de execução para processar o arquivo de 1 bilhão de linhas são apresentados abaixo:

## Tempo de Execução

| Implementação   | Tempo(min) | Tempo(s) |
|-----------------|------------|----------|
| Bash + awk      | 12,40      | 744      |
| Python          | 10,25      | 615      |
| Python + Pandas | 4,25       | 254.76   |
| Python + Dask   | 2,83       | 169,55   |
| Python + Polars | 0,43       | 25.55    |
| Python + Duckdb | 0,22       | 13.14    |


## Conclusão

Este desafio destacou claramente a eficácia de diversas bibliotecas Python na manipulação de grandes volumes de dados. Métodos tradicionais como Bash (12 minutos), Python puro (10 minutos) e até mesmo o Pandas (4 minutos) demandaram uma série de táticas para implementar o processamento em "lotes", enquanto bibliotecas como Dask, Polars e DuckDB provaram ser excepcionalmente eficazes, requerendo menos linhas de código devido à sua capacidade inerente de distribuir os dados em "lotes em streaming" de maneira mais eficiente.  
O DuckDB se sobressaiu, alcançando o menor tempo de execução graças à sua estratégia de execução e processamento de dados.

Esses resultados enfatizam a importância de selecionar a ferramenta adequada para análise de dados em larga escala, demonstrando que Python, com as bibliotecas certas, é uma escolha poderosa para enfrentar desafios de big data.

## Como Executar

Passos para Configuração

1. Clone esse repositório
   
```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
```

2. Definir a versao do Python usando o `pyenv`
   
```bash
    pyenv local 3.12.1
```


3. Instalar dependências com Poetry:
   
```bash
    poetry env use 3.12.1
    poetry install --no-root
    poetry lock --no-update
```
   
4. Gerar o arquivo de teste:
   
```bash
    python3 src/create_measurements.py
```

**Nota**: Esse processo pode demorar cerca de 7 minutos para gerar um arquivo data/measurements.txt de aproximadamente 15 GiB.



5. Instalar as bibliotecas necessárias:

```bash
    pip install dask
    pip install "dask[dataframe]" --upgrade
    pip install polars
    pip install duckdb
```

6. Executar os scripts de ETL:
   
```bash
    chmod +x etl_bash_and_awk.sh
    ./etl_bash_and_awk.sh
    python3 etl_python.py
    python3 etl_pandas.py
    python3 etl_dask.py
    python3 etl_polars.py
    python3 etl_duckdb.py
```

## Executando o Script Bash
Para rodar o script Bash descrito, siga os passos abaixo:
Instalando o Pipe Viewer (pv)
Se você não tem o pv instalado, pode facilmente instalá-lo usando o gerenciador de pacotes do seu sistema.

* No Ubuntu/Debian:
    
```bash
    sudo apt-get update
    sudo apt-get install pv
```