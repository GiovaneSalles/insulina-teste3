opc = 0

opc = int(input("Digite a opção desejada: "))

match opc:
    case 1:
        print("Acessando portal de login...")
    case 2:
        print("Escolhendo uma música...")
    case _:
        print("Valor incorreto")

# Switch case