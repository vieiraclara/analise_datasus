import pandas as pd
import csv

# função load_csv_robust
def load_csv_robust(file_path, delimiter=";", encoding="latin1"):
    data = []
    header = []
    num_malformed_lines = 0
    total_lines_read = 0

    #print(f"DEBUG(load_csv_robust): Tentando abrir o arquivo: {file_path}") # Debug
    try:
        with open(file_path, "r", encoding=encoding, errors="ignore") as f:
            reader = csv.reader(f, delimiter=delimiter)
            try:
                header = next(reader)
                header = [col.strip().strip("\'") for col in header]
                #print(f"DEBUG(load_csv_robust): Cabeçalho lido: {header[:5]}...") # Debug
            except StopIteration:
                print(f"Aviso: O arquivo {file_path} está vazio.")
                return pd.DataFrame()
            except Exception as e:
                print(f"Erro ao ler o cabeçalho de {file_path}: {e}")
                return pd.DataFrame()

            for i, row in enumerate(reader):
                total_lines_read += 1
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
        #print(f"DEBUG(load_csv_robust): Shape do DataFrame carregado: {df.shape} para {file_path}") # Debug
        return df
    except FileNotFoundError: # mostra se o arquivo não existe/vazio
        print(f"ERRO: Arquivo não encontrado: {file_path}. Verifique o caminho.")
        return pd.DataFrame()
    except Exception as e:
        print(f"ERRO INESPERADO durante o carregamento de {file_path}: {e}")
        return pd.DataFrame()


# encapsula a lógica de limpeza dos dados
def get_cleaned_dataframes():
    try:
        # df_cianobacterias
        df_cianobacterias = load_csv_robust(
            "../dados/vigilancia_cianobacterias_cianotoxinas.csv",
            delimiter=";",
            encoding="latin1"
        )
        #print(f"\n--- DEBUG get_cleaned_dataframes: CIANOBACTERIAS ---") # Debug
        print(f"PASSO 1: Shape após o carregamento inicial: {df_cianobacterias.shape}")
        if df_cianobacterias.empty:
            print("PASSO 1: df_cianobacterias está VAZIO imediatamente após load_csv_robust.")
            print(f"Verifique se o arquivo existe: ../dados/vigilancia_cianobacterias_cianotoxinas.csv")
            
        #df_tratamento_agua
        df_tratamento_agua = load_csv_robust(
            "../dados/cadastro_tratamento_de_agua.csv",
            delimiter=";",
            encoding="latin1"
        )
        #print(f"\n--- DEBUG get_cleaned_dataframes: TRATAMENTO AGUA ---") # Debug
        print(f"PASSO 1: Shape após o carregamento inicial: {df_tratamento_agua.shape}")
        if df_tratamento_agua.empty:
            print("PASSO 1: df_tratamento_agua está VAZIO imediatamente após load_csv_robust.")
            print(f"Por favor, verifique se o arquivo existe: ../dados/cadastro_tratamento_de_agua.csv")

    except Exception as e:
        print(f"Erro ao carregar os arquivos: {e}")
        return pd.DataFrame(), pd.DataFrame() 

    # Limpeza e Pré-processamento
    print("\n--- Limpeza e Pré-processamento: Vigilância Cianobactérias e Cianotoxinas ---")

    if not df_cianobacterias.empty:
        #print(f"PASSO 2: Colunas antes de renomear: {df_cianobacterias.columns.tolist()}") # Debug
        df_cianobacterias.rename(columns={
            'Região Geográfica': 'Regiao',
            'UF': 'Estado',
            'Município': 'Municipio',
            'Data da Coleta': 'DataColeta',
            'Parâmetro (ciano)': 'ParametroCiano',
            'Resultado': 'ResultadoCiano'
        }, inplace=True)
        #print(f"PASSO 2: Colunas após renomear: {df_cianobacterias.columns.tolist()}") # Debug

        if 'ResultadoCiano' in df_cianobacterias.columns: # checagem de existência da coluna
            df_cianobacterias['ResultadoCiano'] = df_cianobacterias['ResultadoCiano'].astype(str).str.replace(',', '.', regex=False)
            #original_resultadociano_nans = df_cianobacterias['ResultadoCiano'].isnull().sum() # Debug
            df_cianobacterias['ResultadoCiano'] = pd.to_numeric(df_cianobacterias['ResultadoCiano'], errors='coerce')
            #print(f"PASSO 3: NaNs em 'ResultadoCiano' após to_numeric (antes do fillna): {df_cianobacterias['ResultadoCiano'].isnull().sum()}") # Debug
            if df_cianobacterias['ResultadoCiano'].isnull().all(): # Se todos virarem NaN, a mediana não funcionará
                print("AVISO: Todos os valores de 'ResultadoCiano' se tornaram NaN. A mediana não pode ser calculada.")
                # Decida como lidar: preencher com 0, ou remover linhas. Por enquanto, deixando como NaN.
            else:
                df_cianobacterias['ResultadoCiano'] = df_cianobacterias['ResultadoCiano'].fillna(df_cianobacterias['ResultadoCiano'].median())
            #print(f"PASSO 3: NaNs em 'ResultadoCiano' após fillna: {df_cianobacterias['ResultadoCiano'].isnull().sum()}") # Debug
        #else:
            #print("PASSO 3: Coluna 'ResultadoCiano' não encontrada, pulando conversão numérica.") # Debug

        if 'DataColeta' in df_cianobacterias.columns: # Checa se a coluna existe antes de remover
            #print(f"PASSO 4: Valores únicos originais de 'DataColeta' (primeiros 5): {df_cianobacterias['DataColeta'].astype(str).unique()[:5]}") # Debug
            rows_before_dropna = df_cianobacterias.shape[0] # Debug
            df_cianobacterias['DataColeta'] = pd.to_datetime(df_cianobacterias['DataColeta'], errors='coerce', format='%Y/%m/%d %H:%M:%S.%f')
            #print(f"PASSO 4: NaNs em 'DataColeta' após to_datetime: {df_cianobacterias['DataColeta'].isnull().sum()}") # Debug
            
            # Identifica datas problemáticas ANTES de removê-las (novo debug)
            if df_cianobacterias['DataColeta'].isnull().sum() > 0:
                problematic_dates = df_cianobacterias[df_cianobacterias['DataColeta'].isnull()]['DataColeta'].astype(str)
                print(f"PASSO 4: Amostra de valores problemáticos de DataColeta (antes do dropna): {problematic_dates.unique()[:5]}") # Debug

            df_cianobacterias.dropna(subset=['DataColeta'], inplace=True)
            print(f"PASSO 4: Shape após dropna em DataColeta: {df_cianobacterias.shape}. Linhas removidas: {rows_before_dropna - df_cianobacterias.shape[0]}") # Debug
        #else:
            #print("PASSO 4: Coluna 'DataColeta' não encontrada, pulando dropna.") # Debug

        for col in ['Regiao', 'Estado', 'Municipio', 'ParametroCiano']:
            if col in df_cianobacterias.columns: # Checa se a coluna existe antes de preencher
                # Novo debug
                if df_cianobacterias[col].isnull().any():
                    mode_val = df_cianobacterias[col].mode()[0] if not df_cianobacterias[col].empty else "N/A"
                    #print(f"PASSO 5: Preenchendo NaNs em '{col}' com a moda '{mode_val}'. NaNs antes: {df_cianobacterias[col].isnull().sum()}")
                    df_cianobacterias[col] = df_cianobacterias[col].fillna(mode_val)
                    #print(f"PASSO 5: NaNs em '{col}' após fillna: {df_cianobacterias[col].isnull().sum()}")
            #else:
                #print(f"PASSO 5: Coluna categórica '{col}' não encontrada.") # Debug

    else:
        print("Aviso: df_cianobacterias está vazio após o carregamento. Pulando etapas de limpeza para este DataFrame.")

    print("\nInformações após limpeza (df_cianobacterias):")
    print(df_cianobacterias.info())
    print("\nValores nulos por coluna após limpeza (df_cianobacterias):")
    print(df_cianobacterias.isnull().sum())

    # Limpeza e Pré-processamento
    print("\n--- Limpeza e Pré-processamento: Cadastro Tratamento de Água ---")

    # Sóse não estiver vazio
    if not df_tratamento_agua.empty:
        df_tratamento_agua.rename(columns={
            'Região Geográfica': 'Regiao',
            'UF': 'Estado',
            'Município': 'Municipio',
            'Vazão de água tratada': 'VazaoAguaTratada'
        }, inplace=True)

        df_tratamento_agua['VazaoAguaTratada'] = df_tratamento_agua['VazaoAguaTratada'].astype(str).str.replace(',', '.', regex=False)
        df_tratamento_agua['VazaoAguaTratada'] = pd.to_numeric(df_tratamento_agua['VazaoAguaTratada'], errors='coerce')
        df_tratamento_agua['VazaoAguaTratada'] = df_tratamento_agua['VazaoAguaTratada'].fillna(df_tratamento_agua['VazaoAguaTratada'].median())

        for col in ['Regiao', 'Estado', 'Municipio']:
            if col in df_tratamento_agua.columns: # Checa se a coluna existe antes de preencher
                df_tratamento_agua[col] = df_tratamento_agua[col].fillna(df_tratamento_agua[col].mode()[0])
    else:
        print("Aviso: df_tratamento_agua está vazio após o carregamento. Pulando etapas de limpeza para este DataFrame.")

    print("\nInformações após limpeza (df_tratamento_agua):")
    print(df_tratamento_agua.info())
    print("\nValores nulos por coluna após limpeza (df_tratamento_agua):")
    print(df_tratamento_agua.isnull().sum())

    # Retorna os datafframes limpos
    return df_cianobacterias, df_tratamento_agua

# se data_cleaning.py for executado diretamente, ele ainda realize a limpeza
if __name__ == "__main__":
    df_cianobacterias_cleaned, df_tratamento_agua_cleaned = get_cleaned_dataframes()
    print("\nDataFrames limpos gerados.")