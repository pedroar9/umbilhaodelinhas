# Desafio de um bilhão de linhas em [Python](https://www.python.org/doc/) #

Implementação em [Python](https://www.python.org/doc/) do desafio de 1 bilhão de linhas.  

Inspirado pelo [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc?tab=readme-ov-file#1%EF%B8%8F%E2%83%A3%EF%B8%8F-the-one-billion-row-challenge), originalmente proposto para `Java`.

https://www.morling.dev/blog/one-billion-row-challenge


## Introdução
O objetivo deste projeto é demonstrar como processar eficientemente um arquivo de dados massivo contendo 1.000.000.000 de linhas (~14GB), especificamente para calcular estatísticas (Incluindo agregação e ordenação) utilizando [Python](https://www.python.org/doc/).

O arquivo de dados consiste em medições de temperatura de várias estações meteorológicas.  
Cada registro segue o formato `<string: nome da estação>;<double: medição>`, com a temperatura sendo apresentada com precisão de uma casa decimal.

Exemplo de Dados:

```CSV
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

O desafio é desenvolver um programa [Python](https://www.python.org/doc/) capaz de ler esse arquivo e calcular a temperatura mínima, média (arredondada para uma casa decimal) e máxima para cada estação, exibindo os resultados em uma tabela ordenada por nome da estação.

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

Os testes foram realizados em um notebook com Linux Mint 21.3 e Windows 11 equipado com um processador 13th Gen Intel(R) Core(TM) i7-13800H e 62GB de RAM.  

As implementações utilizaram algumas abordagens com [Python](https://www.python.org/doc/), [Pandas](https://pandas.pydata.org/docs/user_guide/index.html), [Dask](https://dash.plotly.com/), [Polars](https://docs.pola.rs/user-guide/getting-started/), [Loguru](https://loguru.readthedocs.io/en/latest/) e [DuckDB](https://duckdb.org/docs/connect/overview).  

Os resultados de tempo de execução para processar o arquivo de 1 bilhão de linhas são apresentados abaixo:

## Tempo de Execução

| ![imagem](img/screenpc.png) Implementação   | ![imagem](img/logo_linux_mint_32.png) Tempo(min) | ![imagem](img/logo_linux_mint_32.png) Tempo(s) | ![imagem](img/windows-32.png) Tempo(min) | ![imagem](img/windows-32.png) Tempo(s) |
|-----------------|------------|----------|------ | ------ |
| Bash + awk      | 12.40      | 744      | |  |
| Python          | 10.25      | 615      | 12.64 | 758.16 |
| Python + Pandas | 4.25       | 254.76   | 5.58 | 334.74 |
| Python + Pandas2| 3.65       | 218.92   | 5.34 | 320.67 |
| Python + Dask   | 2.83       | 169.55   | 2.41 | 144.42 |
| Python + Polars | 0.37       | 22.17    | 0.56 | 33.86 |
| Python + Polars  + Loguru| 0.22       | 13.38    | 0.28  | 16.95  |
| Python + Duckdb | 0.20       | 12.30    | 0.23 | 13.93  |

---


## Conclusão

Este desafio destacou claramente a eficácia de diversas [bibliotecas Python](https://blog.dsacademy.com.br/top-25-bibliotecas-python-para-data_science/) na manipulação de grandes volumes de dados. Métodos tradicionais, como Bash levou por volta de 12 minutos e com Python puro 10 minutos, exigiram uma série de táticas para implementar o processamento em "lotes". Mesmo utilizando o [Pandas](https://pandas.pydata.org/docs/user_guide/index.html) que levou cerca de 4 minutos, foi necessário adotar estratégias específicas para gerenciar eficientemente os dados.  

Por outro lado, bibliotecas como [Dask](https://dash.plotly.com/), [Polars](https://docs.pola.rs/user-guide/getting-started/) e [DuckDB](https://duckdb.org/docs/connect/overview) se mostraram excepcionalmente eficazes. Essas ferramentas requerem menos linhas de código devido à sua capacidade inerente de distribuir os dados em "lotes em streaming" de maneira mais eficiente.  

O [Dask](https://dash.plotly.com/) facilita o processamento de dados em paralelo e a divisão de grandes conjuntos de dados em blocos menores, permitindo uma manipulação mais ágil e eficaz.  

O [Polars](https://docs.pola.rs/user-guide/getting-started/) oferece um desempenho altamente otimizado para operações de agregação e ordenação, sendo uma escolha ideal para análises rápidas de grandes volumes de dados.  

Já o [DuckDB](https://duckdb.org/docs/connect/overview) destaca-se por sua eficiência em consultas SQL embutidas, proporcionando uma maneira rápida e fácil de executar análises complexas diretamente no ambiente [Python](https://www.python.org/doc/).

Essas bibliotecas demonstraram que, com as ferramentas certas, [Python](https://www.python.org/doc/) pode ser uma escolha poderosa para enfrentar desafios de big data, oferecendo soluções rápidas, eficientes e relativamente simples de implementar.

## Como Executar

Passos para Configuração

1. Clone esse repositório
   
```bash
    git clone https://github.com/pedroar9/umbilhaodelinhas.git
    cd umbilhaodelinhas
```

2. Definir a versao do Python usando o [`pyenv`](https://github.com/pyenv/pyenv)
   
```bash
    pyenv install 3.12.1
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
    python src/create_measurements.py
```

**Nota**: Esse processo pode demorar cerca de 7 minutos para gerar o arquivo `data/measurements.txt` de aproximadamente 16 GiB.

5. Instalar as bibliotecas necessárias:

```bash
    pip install dask
    pip install "dask[dataframe]" --upgrade
    pip install polars
    pip install loguru
    pip install duckdb
    pip install streamlit
    pip install tqdm

```

6. Executar os scripts de ETL:
   
```bash
    chmod +x etl_bash_and_awk.sh
    ./etl_bash_and_awk.sh
    python etl_python.py
    python etl_pandas.py
    python etl_pandas2.py
    python etl_dask.py
    python etl_polars.py
    python etl_polars_loguru.py
    python etl_duckdb.py
    python etl_duckdb_to_save_parquet.py
```

## Executando o Script Bash
Para rodar o script Bash descrito, siga os passos abaixo:  
Instalando o Pipe Viewer (pv).  
Se você não tem o pv instalado, pode facilmente instalá-lo usando o gerenciador de pacotes do seu sistema.

* No Ubuntu/Debian:
    
```bash
    sudo apt-get update
    sudo apt-get install pv python-is-python3
    
```

## Vídeo de como foi realizado o desafio


[![](img/1bi.png)](https://www.youtube.com/watch?v=X3_QTVIjJz0)
