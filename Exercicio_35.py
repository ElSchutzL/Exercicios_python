valorfatorar = int(input("Informe um valor:"))
resultado = 1

for i in range(1, valorfatorar + 1):
    resultado = resultado * i

print(f"O resultado de {valorfatorar} é: {resultado}")