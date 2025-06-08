import pandas as pd

from data_cleaning import get_cleaned_dataframes
try:
    df_cianobacterias, df_tratamento_agua = get_cleaned_dataframes()
    print("df_cianobacterias carregado com sucesso. Formato:", df_cianobacterias.shape)
    print("df_tratamento_agua carregado com sucesso. Formato:", df_tratamento_agua.shape)

except Exception as e:
    print(f"Erro ao carregar os arquivos no script de análise de relacionamento: {e}")
    exit()

#relacionamento entre os dois conjuntos

print("\n--- Análise de Relacionamento entre Vigilância de Cianobactérias e Cadastro de Tratamento de Água ---")

# 1. Calculamos a média do 'ResultadoCiano' por 'Regiao'
media_resultado_ciano_por_regiao = df_cianobacterias.groupby("Regiao")["ResultadoCiano"].mean().reset_index()
media_resultado_ciano_por_regiao.rename(columns={
    "ResultadoCiano": "MediaResultadoCiano" # Renomeia a coluna pra ficar mais claro
}, inplace=True)
print("\nMédia de 'ResultadoCiano' por Região (Dados de Cianobactérias):")
print(media_resultado_ciano_por_regiao)

# 2. Calculamos a média da 'VazaoAguaTratada' por 'Regiao'
media_vazao_agua_por_regiao = df_tratamento_agua.groupby("Regiao")["VazaoAguaTratada"].mean().reset_index()
# Aqui, a coluna original provavelmente está escrita incorretamente em 'VazaoAguaTraatada', corrigindo para 'VazaoAguaTratada'
media_vazao_agua_por_regiao.rename(columns={
    "VazaoAguaTratada": "MediaVazaoAguaTratada" # Renomeia para clareza
}, inplace=True)
print("\nMédia de 'VazaoAguaTratada' por Região (Dados de Tratamento de Água):")
print(media_vazao_agua_por_regiao)

# 3. Agora, juntamos os dois resultados por 'Regiao' (um 'merge' interno pega só as regiões em comum)
relacionamento_regiao = pd.merge(
    media_resultado_ciano_por_regiao,
    media_vazao_agua_por_regiao,
    on="Regiao", # A coluna 'Regiao' é nossa chave para unir
    how="inner" # Só queremos as regiões que aparecem nos dois DataFrames
)

print("\nRelacionamento entre a Média de 'ResultadoCiano' e a Média de 'VazaoAguaTratada' por Região:")
print(relacionamento_regiao)

# Pergunta: Existe alguma correlação aparente entre a média de cianobactérias e a vazão de água tratada por região?
# Resposta (com base nos dados que agrupamos): Olhando a tabela que geramos acima, podemos ver as médias de 'ResultadoCiano' e 'VazaoAguaTratada' para cada região. Mas só essa olhada não basta. Pra ter certeza se existe uma correlação estatisticamente relevante (ou seja, se uma coisa *influencia* a outra), a gente precisaria ir além: calcular coeficientes de correlação (tipo o de Pearson) ou fazer testes estatísticos mais específicos.