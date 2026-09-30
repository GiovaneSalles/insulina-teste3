# arroz
# feijão
# banana
# leite

# variavel para cada
nome = ""

# LISTAS
compras = ["arroz", "feijão", "banana", "leite"]
numero = [0, 1, 2, 3]

nome = input("Insira um item: ")
compras.append(nome)

# Recurso que add novos itens a lista (APPEND())
compras.append("Macarrão")     # Recurso
compras.append("Tang")
compras.append("Chocolate")

# Recurso que remove itens da lista (pop())
compras.pop()

# Acessar um item da lista
primeiro_item = compras[0]

print(compras)
print("O primeiro item é " + primeiro_item)