lista = []

for i in range(5):
    valor = int(input("Digite um número: "))
    lista.append(valor)

contador = 0

for numero in lista:
    if numero >= 10:
        contador += 1

print("Quantidade de valores >= 10:", contador)