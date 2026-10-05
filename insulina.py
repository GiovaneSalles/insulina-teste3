# Sequência da pré-proinsulina humana
preproInsulin = "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKT" \
                "RREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"

# Partes da insulina
lsInsulin = "MALWMRLLPLLALLALWGPDPAAA"
bInsulin = "FVNQHLCGSHLVEALYLVCGERGFFYTPKT"
aInsulin = "GIVEQCCTSICSLYQLENYCN"
cInsulin = "RREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKR"

# Insulina madura = cadeia B + cadeia A
insulin = bInsulin + aInsulin

# Exibindo as sequências
print("Sequência da pré-proinsulina humana:")
print(preproInsulin)
print("Cadeia A da insulina: " + aInsulin)

# Peso de cada aminoácido
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13,
             'F': 165.19, 'G': 75.07, 'H': 155.16, 'I': 131.18,
             'K': 146.19, 'L': 131.18, 'M': 149.21, 'N': 132.12,
             'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09,
             'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Peso molecular: para cada letra, quantidade x peso, tudo somado
molecularWeightInsulin = sum(insulin.count(aa) * peso
                             for aa, peso in aaWeights.items())
print("Peso molecular: " + str(molecularWeightInsulin))

# Percentual de erro
realWeight = 5807.63
erro = abs(molecularWeightInsulin - realWeight) / realWeight * 100
print("Percentual de erro: " + str(erro) + "%")