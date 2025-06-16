maior = None
meio = None
menor = None

n = int(input("Informe o valor 1, 2 ou 3 para n: "))
print ("Insira 3 valores inteiros diferentes para a, b e c")
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

if a > b and a > c:
    maior = a
elif a < b and a < c:
    menor = a
elif (a > b and a < c) or (a < b and a > c):
    meio = a
else:
    print(f"Algum valor não está nos padrões requeridos, digite novamente")

if b > a and b > c:
    maior = b
elif b < a and b < c:
    menor = b
elif (b > a and b < c) or (b < a and b > c):
    meio = b
else:
    print(f"Algum valor não está nos padrões requeridos, digite novamente")

if c > b and c > a:
    maior = c
elif c < b and c < a:
    menor = c
elif (c > b and c < a) or (c < b and c > a):
    meio = c
else:
    print(f"Algum valor não está nos padrões requeridos, digite novamente")

if n == 1:
    print(f"{menor}, {meio}, {maior}")
elif n == 2:
    print(f"{maior}, {meio}, {menor}")
elif n == 3:
    print(f"{meio}, {maior}, {menor}")
else:
    print(f"Algo deu errado, tente novamente")