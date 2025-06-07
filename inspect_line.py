import pandas as pd

file_path = 'vigilancia_cianobacterias_cianotoxinas.csv'

# Tentar ler o arquivo linha por linha para identificar o problema
with open(file_path, 'r', encoding='latin1') as f:
    for i, line in enumerate(f):
        if i == 1471: # Linha 1472 (índice 1471)
            print(f"Linha {i+1}: {line}")
            break


