import pandas as pd
import csv

# Função para carregar CSVs de forma robusta, pulando linhas mal formatadas
def load_csv_robust(file_path, delimiter=";", encoding="latin1"):
    data = []
    header = []
    num_malformed_lines = 0
    total_lines_read = 0

    with open(file_path, "r", encoding=encoding, errors="ignore") as f:
        reader = csv.reader(f, delimiter=delimiter)
        
        # Tentar ler o cabeçalho
        try:
            header = next(reader)
            # Remover espaços em branco e aspas duplas do cabeçalho
            header = [col.strip().strip("\'") for col in header]
        except StopIteration:
            print(f"Aviso: O arquivo {file_path} está vazio.")
            return pd.DataFrame()
        except Exception as e:
            print(f"Erro ao ler o cabeçalho de {file_path}: {e}")
            return pd.DataFrame()

        # Ler as linhas de dados
        for i, row in enumerate(reader):
            total_lines_read += 1
            # Remover espaços em branco e aspas duplas de cada campo
            cleaned_row = [field.strip().strip("\'") for field in row]
            
            if len(cleaned_row) == len(header):
                data.append(cleaned_row)
            else:
                num_malformed_lines += 1
    
    if num_malformed_lines > 0:
        percentage_malformed = (num_malformed_lines / total_lines_read) * 100
        print(f"Total de linhas mal formatadas em {file_path}: {num_malformed_lines} de {total_lines_read} ({percentage_malformed:.2f}% do total).")
        if percentage_malformed >= 5:
            print(f"Aviso: Mais de 5% das linhas em {file_path} estão mal formatadas. Considere uma limpeza mais aprofundada.")

    df = pd.DataFrame(data, columns=header)
    return df

# Carregar os conjuntos de dados usando a função robusta
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
    print(f"Erro ao carregar os arquivos: {e}")
    exit()

# --- Limpeza e Pré-processamento de Dados ---

# df_cianobacterias
print("\n--- Limpeza e Pré-processamento: Vigilância Cianobactérias e Cianotoxinas ---")

# Renomear colunas para facilitar o uso
df_cianobacterias.rename(columns={
    'Região Geográfica': 'Regiao',
    'UF': 'Estado',
    'Município': 'Municipio',
    'Data da Coleta': 'DataColeta',
    'Parâmetro (ciano)': 'ParametroCiano',
    'Resultado': 'ResultadoCiano'
}, inplace=True)

# Converter colunas para tipos numéricos, tratando erros
# Substituir vírgulas por pontos para conversão decimal
df_cianobacterias['ResultadoCiano'] = df_cianobacterias['ResultadoCiano'].str.replace(',', '.', regex=False)

# Converter para numérico, forçando NaN para valores não convertíveis
df_cianobacterias['ResultadoCiano'] = pd.to_numeric(df_cianobacterias['ResultadoCiano'], errors='coerce')

# Converter 'DataColeta' para datetime
df_cianobacterias['DataColeta'] = pd.to_datetime(df_cianobacterias['DataColeta'], errors='coerce', format='%d/%m/%Y')

# Preencher valores ausentes (NaN) em colunas numéricas com a mediana
df_cianobacterias['ResultadoCiano'] = df_cianobacterias['ResultadoCiano'].fillna(df_cianobacterias['ResultadoCiano'].median())

# Para colunas categóricas, preencher com a moda ou 'Desconhecido'
for col in ['Regiao', 'Estado', 'Municipio', 'ParametroCiano']:
    df_cianobacterias[col] = df_cianobacterias[col].fillna(df_cianobacterias[col].mode()[0])

# Remover linhas com 'DataColeta' nula após a conversão (se houver)
df_cianobacterias.dropna(subset=['DataColeta'], inplace=True)

print("\nInformações após limpeza (df_cianobacterias):")
print(df_cianobacterias.info())
print("\nValores nulos por coluna após limpeza (df_cianobacterias):")
print(df_cianobacterias.isnull().sum())

# df_tratamento_agua
print("\n--- Limpeza e Pré-processamento: Cadastro Tratamento de Água ---")

# Renomear colunas (exemplo, ajuste conforme necessário)
df_tratamento_agua.rename(columns={
    'Região Geográfica': 'Regiao',
    'UF': 'Estado',
    'Município': 'Municipio',
    'Vazão de água tratada': 'VazaoAguaTratada'
}, inplace=True)

# Converter 'VazaoAguaTratada' para numérico
df_tratamento_agua['VazaoAguaTratada'] = df_tratamento_agua['VazaoAguaTratada'].str.replace(',', '.', regex=False)
df_tratamento_agua['VazaoAguaTratada'] = pd.to_numeric(df_tratamento_agua['VazaoAguaTratada'], errors='coerce')

# Preencher valores ausentes em 'VazaoAguaTratada' com a mediana
df_tratamento_agua['VazaoAguaTratada'] = df_tratamento_agua['VazaoAguaTratada'].fillna(df_tratamento_agua['VazaoAguaTratada'].median())

# Para colunas categóricas, preencher com a moda ou 'Desconhecido'
for col in ['Regiao', 'Estado', 'Municipio']:
    df_tratamento_agua[col] = df_tratamento_agua[col].fillna(df_tratamento_agua[col].mode()[0])

print("\nInformações após limpeza (df_tratamento_agua):")
print(df_tratamento_agua.info())
print("\nValores nulos por coluna após limpeza (df_tratamento_agua):")
print(df_tratamento_agua.isnull().sum())


