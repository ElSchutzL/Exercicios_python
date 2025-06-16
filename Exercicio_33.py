menoralt = 0
maioralt = 0
altura = 0

for i in range(1, 16):
    altura = float(input(f"Digite a altura da {i}ª pessoa em metro: "))

    if i == 1:
        menoralt = altura
        maioralt = altura
    else:
        if altura > maioralt:
            maioralt = altura
        elif altura < menoralt:
            menoralt = altura

print(f"A maior altura é de {maioralt}m e a menor é de {menoralt}m")