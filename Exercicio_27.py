print("Insira dois números inteiros diferentes:")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    resultado = num1 - num2
elif num2 > num1:
    resultado = num2 - num1
else:
    resultado = "inválido"

print(f"A diferença é:{resultado}")
