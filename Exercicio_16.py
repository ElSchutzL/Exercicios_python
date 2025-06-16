num = int(input("Insira o número: "))

if num % 2 == 0:
    print(f"O número é Par")
else:
    print(f"O número é Ímpar")

if num > 0:
    print(f"O número é Positivo")
elif num == 0:
    print(f"O número é Neutro")
elif num < 0:
    print(f"O número é Negativo")