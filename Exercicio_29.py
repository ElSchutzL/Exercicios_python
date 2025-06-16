soma = 0
somapares = 0
somaimpares = 0
somamulti3 = 0

for n in range(1, 11):
    soma = soma + n

    if n % 2 == 0:
        somapares = somapares + n
    else:
        somaimpares = somaimpares + n

    if n % 3 == 0:
        somamulti3 = somamulti3 + n

print(f"Soma: {soma}")
print(f"Soma dos pares: {somapares}")
print(f"Soma dos ímpares: {somaimpares}")
print(f"Soma dos múltiplos de 3: {somamulti3}")