soma = 0

while True > 0:
    num = int(input("Informe o valor: "))
    
    if 200 >= num >= 100:
        soma += 1

    if num == 0:
        break

print(f"Quantidade de números entre 100 e 200: {soma}")