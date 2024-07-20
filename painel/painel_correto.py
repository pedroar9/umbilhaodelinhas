import streamlit as st
import duckdb
import pandas as pd

# Função para carregar dados do arquivo Parquet
def load_data():
    con = duckdb.connect()
    df = con.execute("SELECT * FROM 'data/measurements_summary.parquet'").df()
    con.close()
    return df

# Função principal para criar o dashboard
def main():
    st.title("Resumo da estação meteorológica")
    st.write("Este painel mostra o resumo dos dados da estação meteorológica, incluindo temperaturas mínimas, médias e máximas.")

    # Carregar os dados
    data = load_data()

    # Exibir os dados em formato de tabela
    st.dataframe(data)

if __name__ == "__main__":
    main()