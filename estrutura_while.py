# contador = 1

# print("Valor inicial do Contador: " +str(contador))

# while contador <= 5:    # enquanto(while) expressão lógica = true/false
#     print(contador)     # exibir o número pro contador
#     contador = contador + 1

# print("Valor final do Contador: " + str(contador))

total = 0
numero = 0

numero = int(input("Insira um número positivo: "))

while numero > 0:
    total = total + numero
    numero = int(input("Insira um número positivo: "))

print (f"O total dos números digitados é: {total}")