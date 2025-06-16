Lista = []
qtd = 1

while qtd < 6:
    valor = int(input("Insira o valor a ser adicionado: "))
    Lista.append(f"{valor}")
    qtd += 1

print(f"Lista: {Lista}")