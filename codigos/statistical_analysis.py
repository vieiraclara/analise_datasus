import pandas as pd
import numpy as np

# função que nos retorna os dataframes limpos
from data_cleaning import get_cleaned_dataframes
try:
    df_cianobacterias, df_tratamento_agua = get_cleaned_dataframes()
except Exception as e:
    print(f"Erro ao carregar os arquivos limpos no script de análise estatística: {e}")
    exit() # Se der erro, para por aqui

#anaelises estatisticas descritivas

print("\n--- Análises Estatísticas Descritivas: Vigilância de Cianobactérias e Cianotoxinas ---")

#medidas de tendencia central e dispersão resultadociano
print("\nEstatísticas para 'ResultadoCiano':")
print(df_cianobacterias["ResultadoCiano"].describe())

#frequencia de cada regiao no dataframe de cianobacterias
print("\nFrequência de Região (df_cianobacterias):")
print(df_cianobacterias["Regiao"].value_counts())

# frequencia de cada estado no dataframe de cianobacterias
print("\nFrequência de Estado (df_cianobacterias):")
print(df_cianobacterias["Estado"].value_counts())

print("\n--- Análises Estatísticas Descritivas: Cadastro de Tratamento de Água ---")

# medidas de tendencia central e dispersão para a coluna vazaoaguatratada
print("\nEstatísticas para 'VazaoAguaTratada':")
print(df_tratamento_agua["VazaoAguaTratada"].describe())

# frequencia de cada regiao no dataframe de tratamento de agua
print("\nFrequência de Região (df_tratamento_agua):")
print(df_tratamento_agua["Regiao"].value_counts())

# frequência de cada estado no dataframe de tratamento de agua
print("\nFrequência de Estado (df_tratamento_agua):")
print(df_tratamento_agua["Estado"].value_counts())