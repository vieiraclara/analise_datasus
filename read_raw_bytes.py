with open("vigilancia_cianobacterias_cianotoxinas.csv", "rb") as f:
    f.seek(0) # Go to the beginning of the file
    for i, line_bytes in enumerate(f):
        if i == 1471: # Line 1472 (index 1471)
            print(f"Linha {i+1} (bytes): {line_bytes}")
            break


