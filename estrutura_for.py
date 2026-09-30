# nomes = ["Italo", "DaviBraga", "Matheus"]

# for item in nomes:
#     print("Seja bem vind/o/a " + item)

# print("Final do programa")

lista = []
valor = 0
contador = 0

while contador <= 3:
    valor = int(input("Insira um valor: "))
    lista.append(valor)
    contador = contador + 1

for item in lista:
    print(item * item)

