import os
import pandas as pd
import time

start_time = time.time()
# Usando os.path.join para garantir compatibilidade entre sistemas operacionais
PATH_DO_TXT = os.path.join("data", "measurements.txt")

# Atribui o valor de PATH_DO_TXT para file_path
file_path = PATH_DO_TXT

# Especificar os tipos de dados ao ler o arquivo CSV
dtype = {
    'station': 'category',
    'measure': 'float32'
}

# Ler o arquivo CSV com os tipos de dados especificados
df = pd.read_csv(file_path, sep=';', header=None, names=['station', 'measure'], dtype=dtype)

# Realizar as operações de groupby, agregação e ordenação
sorted_df = (
    df.groupby('station')['measure']
    .agg(Min='min', Max='max', Avg='mean')
    .sort_values(by='station')
)

# Exibir o resultado
print(sorted_df)
took = time.time() - start_time
print(f"Tempo total de execução: {took:.2f} segundos")