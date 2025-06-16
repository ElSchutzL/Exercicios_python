maior = 0

numero = int(input("Digite um número inteiro positivo (-1 para parar): "))

while numero != -1:
    if numero > maior:
        maior = numero
    numero = int(input("Digite um número inteiro positivo (-1 para parar): "))

if maior > 0:
    print(f"O maior número digitado foi: {maior}")
else:
    print("Nenhum número válido foi digitado.")