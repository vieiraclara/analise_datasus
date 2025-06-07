import pandas as pd

# Importar a função de carregamento robusto do script de limpeza de dados
from data_cleaning import load_csv_robust

# Carregar os conjuntos de dados usando a função robusta (caminhos relativos ao diretório \'scripts\')
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
    print(f"Erro ao carregar os arquivos no script de análise de relacionamento: {e}")
    exit()

# --- Relacionamento entre os dois conjuntos de dados ---

print("\n--- Análise de Relacionamento entre Vigilância Cianobactérias e Cadastro Tratamento de Água ---")

# 1. Média de ResultadoCiano por Região
media_resultado_ciano_por_regiao = df_cianobacterias.groupby("Regiao")["ResultadoCiano"].mean().reset_index()
media_resultado_ciano_por_regiao.rename(columns={
    "ResultadoCiano": "MediaResultadoCiano"
}, inplace=True)
print("\nMédia de ResultadoCiano por Região (Cianobactérias):")
print(media_resultado_ciano_por_regiao)

# 2. Média de VazaoAguaTratada por Região
media_vazao_agua_por_regiao = df_tratamento_agua.groupby("Regiao")["VazaoAguaTratada"].mean().reset_index()
media_vazao_agua_por_regiao.rename(columns={
    "VazaoAguaTratada": "MediaVazaoAguaTratada"
}, inplace=True)
print("\nMédia de VazaoAguaTratada por Região (Tratamento de Água):")
print(media_vazao_agua_por_regiao)

# 3. Combinar os resultados por Região
relacionamento_regiao = pd.merge(
    media_resultado_ciano_por_regiao,
    media_vazao_agua_por_regiao,
    on="Regiao",
    how="inner"
)

print("\nRelacionamento entre Média de ResultadoCiano e Média de VazaoAguaTratada por Região:")
print(relacionamento_regiao)

# Pergunta: Existe alguma correlação aparente entre a média de cianobactérias e a vazão de água tratada por região?
# Resposta (baseada nos dados agregados): Observando a tabela acima, podemos ver as médias de ResultadoCiano e VazaoAguaTratada para cada região. Uma análise mais aprofundada, como o cálculo de coeficientes de correlação ou testes estatísticos, seria necessária para determinar se existe uma correlação estatisticamente significativa.
