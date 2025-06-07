import pandas as pd
import csv

# Função para carregar CSVs de forma robusta, pulando linhas mal formatadas
def load_csv_robust(file_path, delimiter=\";\
, encoding=\"latin1\"):
    data = []
    header = []
    num_malformed_lines = 0
    total_lines_read = 0

    with open(file_path, \"r\", encoding=encoding, errors=\"ignore\") as f:
        reader = csv.reader(f, delimiter=delimiter)
        
        # Tentar ler o cabeçalho
        try:
            header = next(reader)
            # Remover espaços em branco e aspas duplas do cabeçalho
            header = [col.strip().strip(\'"\') for col in header]
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
            cleaned_row = [field.strip().strip(\'"\') for field in row]
            
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
        \"vigilancia_cianobacterias_cianotoxinas.csv\
,
        delimiter=\";\
,
        encoding=\"latin1\"
    )
    df_tratamento_agua = load_csv_robust(
        \"cadastro_tratamento_de_agua.csv\
,
        delimiter=\";\
,
        encoding=\"latin1\"
    )
except Exception as e:
    print(f"Erro ao carregar os arquivos: {e}")
    exit()

# Análise exploratória inicial - Cianobactérias
print("\n--- Análise Exploratória: Vigilância Cianobactérias e Cianotoxinas ---")
print("Primeiras 5 linhas:")
print(df_cianobacterias.head())
print("\nInformações gerais:")
print(df_cianobacterias.info())
print("\nEstatísticas descritivas:")
print(df_cianobacterias.describe(include=\'all\'))
print("\nValores nulos por coluna:")
print(df_cianobacterias.isnull().sum())

# Análise exploratória inicial - Tratamento de Água
print("\n--- Análise Exploratória: Cadastro Tratamento de Água ---")
print("Primeiras 5 linhas:")
print(df_tratamento_agua.head())
print("\nInformações gerais:")
print(df_tratamento_agua.info())
print("\nEstatísticas descritivas:")
print(df_tratamento_agua.describe(include=\'all\'))
print("\nValores nulos por coluna:")
print(df_tratamento_agua.isnull().sum())


