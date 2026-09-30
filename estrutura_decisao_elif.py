temperatura = 0

temperatura = int(input("Digite a temperatura da sua cidade: "))

if temperatura <= 15: 
    print("Está frio")

elif temperatura >= 15 and temperatura <= 25:
    print("O clima está ameno")

elif temperatura <= 25 and temperatura <= 30:
    print("A temperatura está agradável")

else:
    print("Está quente")