import pandas as pd
from scipy import stats

# Importar a função de carregamento robusto do script de limpeza de dados
from data_cleaning import load_csv_robust

# Carregar os conjuntos de dados usando a função robusta (caminhos relativos ao diretório \'scripts\')
try:
    df_cianobacterias = load_csv_robust(
        "../data/vigilancia_cianobacterias_cianotoxinas.csv",
        delimiter=";",
        encoding="latin1"
    )
    print("df_cianobacterias loaded successfully. Shape:", df_cianobacterias.shape)

    df_tratamento_agua = load_csv_robust(
        "../data/cadastro_tratamento_de_agua.csv",
        delimiter=";",
        encoding="latin1"
    )
    print("df_tratamento_agua loaded successfully. Shape:", df_tratamento_agua.shape)

except Exception as e:
    print(f"Erro ao carregar os arquivos no script de análise de inferência: {e}")
    exit()

# --- Análises de Inferência Estatística ---

print("\n--- Análises de Inferência Estatística: Vigilância Cianobactérias e Cianotoxinas ---")

# Hipótese: A média de ResultadoCiano é igual a 100
# H0: mu = 100
# H1: mu != 100

# Remover valores NaN antes do teste t
resultado_ciano_clean = df_cianobacterias["ResultadoCiano"].dropna()

if not resultado_ciano_clean.empty:
    t_statistic, p_value = stats.ttest_1samp(resultado_ciano_clean, 100)
    print(f"\nTeste t de uma amostra para ResultadoCiano (vs. média = 100):")
    print(f"Estatística t: {t_statistic:.4f}")
    print(f"Valor p: {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        print(f"Com p-valor ({p_value:.4f}) < alpha ({alpha}), rejeitamos a hipótese nula. A média de ResultadoCiano é significativamente diferente de 100.")
    else:
        print(f"Com p-valor ({p_value:.4f}) >= alpha ({alpha}), não rejeitamos a hipótese nula. Não há evidência suficiente para dizer que a média de ResultadoCiano é diferente de 100.")

    # Intervalo de Confiança para a média de ResultadoCiano
    confidence_interval = stats.t.interval(alpha=0.95, df=len(resultado_ciano_clean)-1,
                                           loc=resultado_ciano_clean.mean(),
                                           scale=stats.sem(resultado_ciano_clean))
    print(f"Intervalo de Confiança de 95% para a média de ResultadoCiano: {confidence_interval}")
else:
    print("Não há dados suficientes em ResultadoCiano para realizar o teste t.")

print("\n--- Análises de Inferência Estatística: Cadastro Tratamento de Água ---")

# Hipótese: Há diferença significativa na VazaoAguaTratada entre as regiões SUDESTE e NORDESTE
# H0: mu_SUDESTE = mu_NORDESTE
# H1: mu_SUDESTE != mu_NORDESTE

vazao_sudeste = df_tratamento_agua[df_tratamento_agua["Regiao"] == "SUDESTE"]["VazaoAguaTratada"].dropna()
vazao_nordeste = df_tratamento_agua[df_tratamento_agua["Regiao"] == "NORDESTE"]["VazaoAguaTratada"].dropna()

if not vazao_sudeste.empty and not vazao_nordeste.empty:
    t_statistic_ind, p_value_ind = stats.ttest_ind(vazao_sudeste, vazao_nordeste, equal_var=False) # Welch\'s t-test
    print(f"\nTeste t independente para VazaoAguaTratada (SUDESTE vs. NORDESTE):")
    print(f"Estatística t: {t_statistic_ind:.4f}")
    print(f"Valor p: {p_value_ind:.4f}")

    alpha = 0.05
    if p_value_ind < alpha:
        print(f"Com p-valor ({p_value_ind:.4f}) < alpha ({alpha}), rejeitamos a hipótese nula. Há uma diferença significativa na VazaoAguaTratada entre SUDESTE e NORDESTE.")
    else:
        print(f"Com p-valor ({p_value_ind:.4f}) >= alpha ({alpha}), não rejeitamos a hipótese nula. Não há evidência suficiente para dizer que há uma diferença significativa na VazaoAguaTratada entre SUDESTE e NORDESTE.")
else:
    print("Não há dados suficientes para comparar VazaoAguaTratada entre SUDESTE e NORDESTE.")