import pandas as pd
import numpy as np

# Importar a função de carregamento robusto e os dataframes limpos do script de limpeza de dados
# Assumindo que data_cleaning.py está no mesmo diretório ou pode ser importado
from data_cleaning import load_csv_robust

# Carregar os conjuntos de dados usando a função robusta (caminhos relativos ao diretório 'scripts')
try:
    df_cianobacterias = load_csv_robust(
        "../dados/vigilancia_cianobacterias_cianotoxinas.csv",
        delimiter=";",
        encoding="latin1"
    )
    df_tratamento_agua = load_csv_robust(
        "../dados/cadastro_tratamento_de_agua.csv",
        delimiter=";",
        encoding="latin1"
    )
except Exception as e:
    print(f"Erro ao carregar os arquivos no script de análise estatística: {e}")
    exit()

# --- Análises Estatísticas Descritivas ---

print("\n--- Análises Estatísticas Descritivas: Vigilância Cianobactérias e Cianotoxinas ---")

# Medidas de tendência central e dispersão para 'ResultadoCiano'
print("\nEstatísticas para 'ResultadoCiano':")
print(df_cianobacterias["ResultadoCiano"].describe())

# Frequência de 'Regiao'
print("\nFrequência de Região (df_cianobacterias):")
print(df_cianobacterias["Regiao"].value_counts())

# Frequência de 'Estado'
print("\nFrequência de Estado (df_cianobacterias):")
print(df_cianobacterias["Estado"].value_counts())

print("\n--- Análises Estatísticas Descritivas: Cadastro Tratamento de Água ---")

# Medidas de tendência central e dispersão para 'VazaoAguaTratada'
print("\nEstatísticas para 'VazaoAguaTratada':")
print(df_tratamento_agua["VazaoAguaTratada"].describe())

# Frequência de 'Regiao'
print("\nFrequência de Região (df_tratamento_agua):")
print(df_tratamento_agua["Regiao"].value_counts())

# Frequência de 'Estado'
print("\nFrequência de Estado (df_tratamento_agua):")
print(df_tratamento_agua["Estado"].value_counts())


