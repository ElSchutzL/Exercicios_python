lista = []

for i in range(5):
    valor = int(input("Digite um número inteiro: "))
    lista.append(valor)

contador = 0

for numero in lista:
    if numero % 2 == 0:
        contador += 1

print("Quantidade de valores pares:", contador)