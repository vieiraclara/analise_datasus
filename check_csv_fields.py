import csv

file_path = 'vigilancia_cianobacterias_cianotoxinas.csv'

def count_fields(file_path, delimiter=';', quotechar='"', encoding='latin1'):
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
            for i, row in enumerate(reader):
                if len(row) != 3: # Assuming 3 fields based on the error message
                    print(f"Linha {i+1}: {len(row)} campos. Conteúdo: {row}")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

print("Verificando o número de campos por linha no arquivo de cianobactérias...")
count_fields(file_path)


