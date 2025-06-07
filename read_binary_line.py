with open("vigilancia_cianobacterias_cianotoxinas.csv", "rb") as f:
    f.seek(0) # Go to the beginning of the file
    for i, line_bytes in enumerate(f):
        if i == 1471: # Line 1472 (index 1471)
            try:
                line_decoded = line_bytes.decode("latin1")
                print(f"Linha {i+1} (latin1): {line_decoded}")
            except UnicodeDecodeError as e:
                print(f"Erro de decodificação latin1 na linha {i+1}: {e}")
                line_decoded = line_bytes.decode("latin1", errors=\'ignore\') # Corrected: 'ignore' as a single string literal
                print(f"Linha {i+1} (latin1 com ignore): {line_decoded}")
            break


