import pandas as pd
import numpy as np

# Importar a função de carregamento robusto do script de limpeza de dados
from data_cleaning import load_csv_robust

# Carregar os conjuntos de dados usando a função robusta (caminhos relativos ao diretório 'scripts')
try:
    df_cianobacterias = load_csv_robust(
        "../data/vigilancia_cianobacterias_cianotoxinas.csv",
        delimiter=";",
        encoding="latin1"
    )
    df_tratamento_agua = load_csv_robust(
        "../data/cadastro_tratamento_de_agua.csv",
        delimiter=";",
        encoding="latin1"
    )
except Exception as e:
    print(f"Erro ao carregar os arquivos no script de análise de probabilidade: {e}")
    exit()

# --- Análises de Probabilidade ---

print("\n--- Análises de Probabilidade: Vigilância Cianobactérias e Cianotoxinas ---")

# Probabilidade de 'ResultadoCiano' ser maior que 0
prob_resultado_maior_que_zero = (df_cianobacterias['ResultadoCiano'] > 0).mean()
print(f"Probabilidade de ResultadoCiano ser maior que 0: {prob_resultado_maior_que_zero:.4f}")

# Probabilidade de 'Regiao' ser 'SUDESTE'
prob_regiao_sudeste_ciano = (df_cianobacterias['Regiao'] == 'SUDESTE').mean()
print(f"Probabilidade da Região ser SUDESTE (Cianobactérias): {prob_regiao_sudeste_ciano:.4f}")

print("\n--- Análises de Probabilidade: Cadastro Tratamento de Água ---")

# Probabilidade de 'VazaoAguaTratada' ser maior que 0
prob_vazao_maior_que_zero = (df_tratamento_agua['VazaoAguaTratada'] > 0).mean()
print(f"Probabilidade de VazaoAguaTratada ser maior que 0: {prob_vazao_maior_que_zero:.4f}")

# Probabilidade de 'Estado' ser 'SP'
prob_estado_sp_agua = (df_tratamento_agua['Estado'] == 'SP').mean()
print(f"Probabilidade do Estado ser SP (Tratamento de Água): {prob_estado_sp_agua:.4f}")


