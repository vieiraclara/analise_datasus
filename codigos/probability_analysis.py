import pandas as pd
import numpy as np

# função que retorna os dataframes limpos
from data_cleaning import get_cleaned_dataframes
try:
    df_cianobacterias, df_tratamento_agua = get_cleaned_dataframes()
except Exception as e:
    print(f"Erro ao carregar os arquivos no script de análise de probabilidade: {e}")
    exit() 

# --- Análises de Probabilidade ---

print("\n--- Análises de Probabilidade: Vigilância Cianobactérias e Cianotoxinas ---")

print(f"Tipo de df_cianobacterias: {type(df_cianobacterias)}")
print(f"Conteúdo de df_cianobacterias (primeiras 5 linhas): \n{df_cianobacterias.head()}") 

# Probabilidade de ResultadoCiano ser maior que 0a média de True (1) e False (0) nos dá a proporção, que é a probabilidade
prob_resultado_maior_que_zero = (df_cianobacterias['ResultadoCiano'] > 0).mean()
print(f"Probabilidade de 'ResultadoCiano' ser maior que 0: {prob_resultado_maior_que_zero:.4f}")

# P de a regiao ser SUDESTE
prob_regiao_sudeste_ciano = (df_cianobacterias['Regiao'] == 'SUDESTE').mean()
print(f"Probabilidade da 'Regiao' ser SUDESTE (Cianobactérias): {prob_regiao_sudeste_ciano:.4f}")

print("\n--- Análises de Probabilidade: Cadastro Tratamento de Água ---")

# p de vazaoaguatratada ser maior que 0
prob_vazao_maior_que_zero = (df_tratamento_agua['VazaoAguaTratada'] > 0).mean()
print(f"Probabilidade de 'VazaoAguaTratada' ser maior que 0: {prob_vazao_maior_que_zero:.4f}")

# p de estado ser SP
prob_estado_sp_agua = (df_tratamento_agua['Estado'] == 'SP').mean()
print(f"Probabilidade do 'Estado' ser SP (Tratamento de Água): {prob_estado_sp_agua:.4f}")