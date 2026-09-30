# Variáveis
nome = ""   # inicializar com um espaço em branco
ano_nasc = 0
altura = 0.0
resposta = False
resultado = 0
num1 = 0
num2 = 0
idade = 0

# Entrada
nome = input("Olá, qual o seu nome? ")
ano_nasc = input("Qual foi seu ano de nascimento? ")
altura = input("Qual a sua altura? ")
resposta = input("Você mentiu? ")

num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

# Processamento
idade = 2026 - int(ano_nasc)

resultado = int(num1) / int(num2)

# Saída
print("Hello World")
print(nome)
print(ano_nasc)
print(altura)
print(resposta)
print(f"Sua idade é {idade}")
print(num1)
print(num2)
print(f"O resultado da divisão é {resultado}")