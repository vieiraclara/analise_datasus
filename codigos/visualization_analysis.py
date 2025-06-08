import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Importar a função de carregamento robusto do script de limpeza de dados
# Assegure-se de que o caminho para 'data_cleaning' esteja correto
from data_cleaning import get_cleaned_dataframes

# --- Carregar os conjuntos de dados limpos ---
try:
    df_cianobacterias, df_tratamento_agua = get_cleaned_dataframes()
    print("DataFrames carregados com sucesso para geração de gráficos.")
except Exception as e:
    print(f"Erro ao carregar os arquivos para geração de gráficos: {e}")
    exit()

# --- Configurações globais para os gráficos ---
sns.set_style("whitegrid") # Estilo do seaborn
plt.rcParams['figure.figsize'] = (10, 6) # Tamanho padrão das figuras
plt.rcParams['font.size'] = 12 # Tamanho da fonte
plt.rcParams['axes.labelsize'] = 14 # Tamanho da fonte dos rótulos
plt.rcParams['axes.titlesize'] = 16 # Tamanho da fonte dos títulos
plt.rcParams['xtick.labelsize'] = 12 # Tamanho da fonte dos ticks do eixo X
plt.rcParams['ytick.labelsize'] = 12 # Tamanho da fonte dos ticks do eixo Y
plt.rcParams['legend.fontsize'] = 12 # Tamanho da fonte da legenda
plt.rcParams['figure.dpi'] = 100 # Resolução da figura para melhor qualidade
plt.rcParams['savefig.dpi'] = 300 # Resolução da figura ao salvar

# --- 1. Gráficos para 'Vigilância de Cianobactérias e Cianotoxinas' (df_cianobacterias) ---
print("\nGerando gráficos para Vigilância de Cianobactérias e Cianotoxinas...")

# Histograma de 'ResultadoCiano' (apenas valores > 0)
# A análise mostrou muitos zeros, então focar em valores positivos é mais informativo.
resultado_ciano_positivo = df_cianobacterias[df_cianobacterias['ResultadoCiano'] > 0]['ResultadoCiano']
if not resultado_ciano_positivo.empty:
    plt.figure()
    sns.histplot(resultado_ciano_positivo, bins=20, kde=True, color='skyblue')
    plt.title('Distribuição de ResultadoCiano (Valores > 0)')
    plt.xlabel('Concentração de Cianobactérias/Cianotoxinas')
    plt.ylabel('Frequência')
    # APLICAR ESCALA LOGARÍTMICA NO EIXO X SE HOUVER VALORES VÁLIDOS
    if resultado_ciano_positivo.min() > 0: # Garante que não teremos log(0)
        plt.xscale('log')
        plt.xlabel('Concentração de Cianobactérias/Cianotoxinas (escala logarítmica)')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.savefig('../graficos/hist_resultado_ciano_positivo.png')
    plt.close() # Fecha a figura para liberar memória
    print("Histograma de ResultadoCiano (Valores > 0) salvo.")
else:
    print("Não há valores positivos em 'ResultadoCiano' para plotar o histograma.")

# Gráfico de Barras de Frequência por Região
plt.figure()
df_cianobacterias['Regiao'].value_counts().plot(kind='bar', color='lightcoral')
plt.title('Frequência de Amostras de Cianobactérias por Região')
plt.xlabel('Região')
plt.ylabel('Número de Amostras')
plt.xticks(rotation=45, ha='right') # Rotação dos rótulos para melhor legibilidade
plt.tight_layout()
plt.savefig('../graficos/bar_cianobacterias_regiao.png')
plt.close()
print("Gráfico de Barras de Frequência de Cianobactérias por Região salvo.")


# Gráfico de Barras de Frequência por Estado (Top 10)
plt.figure()
df_cianobacterias['Estado'].value_counts().head(10).plot(kind='bar', color='mediumseagreen')
plt.title('Top 10 Estados com Mais Amostras de Cianobactérias')
plt.xlabel('Estado')
plt.ylabel('Número de Amostras')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../graficos/bar_cianobacterias_estado_top10.png')
plt.close()
print("Gráfico de Barras de Frequência de Cianobactérias por Estado (Top 10) salvo.")


# --- 2. Gráficos para 'Cadastro Tratamento de Água' (df_tratamento_agua) ---
print("\nGerando gráficos para Cadastro Tratamento de Água...")

# Histograma de 'VazaoAguaTratada' (apenas valores > 0)
vazao_agua_positiva = df_tratamento_agua[df_tratamento_agua['VazaoAguaTratada'] > 0]['VazaoAguaTratada']
if not vazao_agua_positiva.empty:
    plt.figure()
    sns.histplot(vazao_agua_positiva, bins=20, kde=True, color='lightgreen')
    plt.title('Distribuição de VazaoAguaTratada (Valores > 0)')
    plt.xlabel('Vazão de Água Tratada')
    plt.ylabel('Frequência')
    # APLICAR ESCALA LOGARÍTMICA NO EIXO X SE HOUVER VALORES VÁLIDOS
    if vazao_agua_positiva.min() > 0: # Garante que não teremos log(0)
        plt.xscale('log')
        plt.xlabel('Vazão de Água Tratada (escala logarítmica)')
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.savefig('../graficos/hist_vazao_agua_positiva.png')
    plt.close()
    print("Histograma de VazaoAguaTratada (Valores > 0) salvo.")
else:
    print("Não há valores positivos em 'VazaoAguaTratada' para plotar o histograma.")

# Gráfico de Barras de Frequência por Região
plt.figure()
df_tratamento_agua['Regiao'].value_counts().plot(kind='bar', color='cornflowerblue')
plt.title('Frequência de Registros de Tratamento de Água por Região')
plt.xlabel('Região')
plt.ylabel('Número de Registros')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../graficos/bar_tratamento_agua_regiao.png')
plt.close()
print("Gráfico de Barras de Frequência de Tratamento de Água por Região salvo.")

# Gráfico de Barras de Frequência por Estado (Top 10)
plt.figure()
df_tratamento_agua['Estado'].value_counts().head(10).plot(kind='bar', color='darkorange')
plt.title('Top 10 Estados com Mais Registros de Tratamento de Água')
plt.xlabel('Estado')
plt.ylabel('Número de Registros')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../graficos/bar_tratamento_agua_estado_top10.png')
plt.close()
print("Gráfico de Barras de Frequência de Tratamento de Água por Estado (Top 10) salvo.")


# --- 3. Gráficos de Relacionamento entre os Conjuntos de Dados (AGORA COM GRÁFICOS SEPARADOS) ---
print("\nGerando gráficos de relacionamento...")

# Calcular as médias por região (reutilizando a lógica do script de relacionamento)
media_resultado_ciano_por_regiao = df_cianobacterias.groupby("Regiao")["ResultadoCiano"].mean().reset_index()
media_resultado_ciano_por_regiao.rename(columns={"ResultadoCiano": "MediaResultadoCiano"}, inplace=True)

media_vazao_agua_por_regiao = df_tratamento_agua.groupby("Regiao")["VazaoAguaTratada"].mean().reset_index()
media_vazao_agua_por_regiao.rename(columns={"VazaoAguaTratada": "MediaVazaoAguaTratada"}, inplace=True)

relacionamento_regiao = pd.merge(
    media_resultado_ciano_por_regiao,
    media_vazao_agua_por_regiao,
    on="Regiao",
    how="inner"
)

# NOVO GRÁFICO 1 DE RELACIONAMENTO: Média de ResultadoCiano por Região (separado)
plt.figure(figsize=(10, 6))
sns.barplot(x='Regiao', y='MediaResultadoCiano', data=relacionamento_regiao, palette='viridis')
plt.title('Média de ResultadoCiano por Região (para Análise de Relacionamento)')
plt.xlabel('Região')
plt.ylabel('Média de ResultadoCiano')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../graficos/rel_media_resultado_ciano_regiao.png')
plt.close()
print("Gráfico de Barras da Média de ResultadoCiano por Região (relacionamento) salvo.")

# NOVO GRÁFICO 2 DE RELACIONAMENTO: Média de VazaoAguaTratada por Região (separado)
plt.figure(figsize=(10, 6))
sns.barplot(x='Regiao', y='MediaVazaoAguaTratada', data=relacionamento_regiao, palette='cividis')
plt.title('Média de VazaoAguaTratada por Região (para Análise de Relacionamento)')
plt.xlabel('Região')
plt.ylabel('Média de VazaoAguaTratada')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../graficos/rel_media_vazao_agua_regiao.png')
plt.close()
print("Gráfico de Barras da Média de VazaoAguaTratada por Região (relacionamento) salvo.")


# Opcional: Gráfico de Dispersão (se houver variação suficiente e for significativo)
# Atenção: Se houver muitos zeros ou pouca variação, o gráfico de dispersão pode não ser informativo.
# Filtra para evitar o problema de muitos pontos em (0,0) que obscurecem a visualização.
rel_filtrado = relacionamento_regiao[(relacionamento_regiao['MediaResultadoCiano'] > 0) | (relacionamento_regiao['MediaVazaoAguaTratada'] > 0)]

if not rel_filtrado.empty:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=relacionamento_regiao, # Use relacionamento_regiao para incluir todos os pontos se desejar
        x='MediaVazaoAguaTratada',
        y='MediaResultadoCiano',
        hue='Regiao', # Colorir por região
        s=100, # Tamanho dos pontos
        alpha=0.7 # Transparência
    )
    plt.title('Dispersão: Média ResultadoCiano vs. Média VazaoAguaTratada por Região')
    plt.xlabel('Média Vazão de Água Tratada')
    plt.ylabel('Média ResultadoCiano')
    plt.xscale('log') # Escala logarítmica pode ajudar se os valores variarem muito
    plt.yscale('log') # Escala logarítmica pode ajudar se os valores variarem muito
    plt.grid(True, which="both", ls="--", c='0.7') # Adiciona grid para escalas log
    plt.tight_layout()
    plt.savefig('../graficos/scatter_relacionamento_regiao.png')
    plt.close()
    print("Gráfico de Dispersão de Relacionamento salvo.")
else:
    print("Não há dados suficientes ou variância para gerar um gráfico de dispersão informativo para o relacionamento.")


print("\nProcesso de geração de gráficos concluído.")
