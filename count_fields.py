import csv

file_path = 'vigilancia_cianobacterias_cianotoxinas.csv'

def get_field_counts(file_path, delimiter=';', encoding='latin1'):
    field_counts = {}
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            for i, row in enumerate(reader):
                num_fields = len(row)
                field_counts[num_fields] = field_counts.get(num_fields, 0) + 1
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
    return field_counts

print("Contando o número de campos por linha no arquivo de cianobactérias...")
counts = get_field_counts(file_path)
for count, freq in sorted(counts.items()):
    print(f"Número de campos: {count}, Frequência: {freq}")


