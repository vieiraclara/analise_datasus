import pandas as pd
from scipy import stats

from data_cleaning import get_cleaned_dataframes
try:
    df_cianobacterias, df_tratamento_agua = get_cleaned_dataframes()
    print("df_cianobacterias carregado com sucesso. Shape:", df_cianobacterias.shape)
    print("df_tratamento_agua carregado com sucesso. Shape:", df_tratamento_agua.shape)

except Exception as e:
    print(f"Erro ao carregar os arquivos no script de análise de inferência: {e}")
    exit() 

#Análises de Inferência Estatística

print("\n--- Análises de Inferência Estatística: Vigilância Cianobactérias e Cianotoxinas ---")

# Nossa hipótese: A média de ResultadoCiano é igual a 100
# H0 (Hipótese Nula): A média (mu) é igual a 100
# H1 (Hipótese Alternativa): A média (mu) é diferente de 100

# tirar os valores NaN antes de rodar o teste t
resultado_ciano_clean = df_cianobacterias["ResultadoCiano"].dropna()

if not resultado_ciano_clean.empty:
    t_statistic, p_value = stats.ttest_1samp(resultado_ciano_clean, 100)
    print(f"\nTeste t de uma amostra para ResultadoCiano (comparando com a média = 100):")
    print(f"Estatística t: {t_statistic:.4f}") # Quatro casas decimais para o t
    print(f"Valor p: {p_value:.4f}") # Quatro casas decimais para o p-valor

    alpha = 0.05 # Nosso nível de significância
    if p_value < alpha:
        print(f"Com p-valor ({p_value:.4f}) menor que alpha ({alpha}), a gente **rejeita a hipótese nula**. Isso significa que a média de ResultadoCiano é significativamente diferente de 100.")
    else:
        print(f"Com p-valor ({p_value:.4f}) maior ou igual a alpha ({alpha}), a gente **não rejeita a hipótese nula**. Não temos evidências suficientes para dizer que a média de ResultadoCiano é diferente de 100.")

    # Intervalo de Confiança para a média de ResultadoCiano
    if len(resultado_ciano_clean) > 1:
        confidence_interval = stats.t.interval(confidence=0.95, df=len(resultado_ciano_clean)-1, 
                                               loc=resultado_ciano_clean.mean(), # A média da amostra
                                               scale=stats.sem(resultado_ciano_clean)) # Erro padrão da média
        print(f"Intervalo de Confiança de 95% para a média de ResultadoCiano: {confidence_interval}")
    else:
        print("Não temos dados suficientes para calcular o Intervalo de Confiança para ResultadoCiano (precisamos de pelo menos 2 pontos de dados).")
else:
    print("Não há dados suficientes na coluna 'ResultadoCiano' para rodar o teste t.")

print("\n--- Análises de Inferência Estatística: Cadastro Tratamento de Água ---")

# Nossa hipótese aqui: Existe uma diferença significativa na VazaoAguaTratada entre as regiões SUDESTE e NORDESTE
# H0: A média da vazão no SUDESTE é igual à média da vazão no NORDESTE
# H1: A média da vazão no SUDESTE é diferente da média da vazão no NORDESTE

# Separa os dados de vazão por região, já tirando os NaNs
vazao_sudeste = df_tratamento_agua[df_tratamento_agua["Regiao"] == "SUDESTE"]["VazaoAguaTratada"].dropna()
vazao_nordeste = df_tratamento_agua[df_tratamento_agua["Regiao"] == "NORDESTE"]["VazaoAguaTratada"].dropna()

if not vazao_sudeste.empty and not vazao_nordeste.empty:
    # teste t de Welch (equal_var=False) porque geralmente as variâncias não são iguais
    t_statistic_ind, p_value_ind = stats.ttest_ind(vazao_sudeste, vazao_nordeste, equal_var=False) 
    print(f"\nTeste t independente para VazaoAguaTratada (SUDESTE vs. NORDESTE):")
    print(f"Estatística t: {t_statistic_ind:.4f}")
    print(f"Valor p: {p_value_ind:.4f}")

    alpha = 0.05 # nível de significância de novo
    if p_value_ind < alpha:
        print(f"Com p-valor ({p_value_ind:.4f}) menor que alpha ({alpha}), a gente **rejeita a hipótese nula**. Isso indica que há uma diferença significativa na VazaoAguaTratada entre SUDESTE e NORDESTE.")
    else:
        print(f"Com p-valor ({p_value_ind:.4f}) maior ou igual a alpha ({alpha}), a gente **não rejeita a hipótese nula**. Não temos evidências suficientes para afirmar que há uma diferença significativa na VazaoAguaTratada entre SUDESTE e NORDESTE.")
else:
    print("Não temos dados suficientes para comparar a VazaoAguaTratada entre SUDESTE e NORDESTE.")