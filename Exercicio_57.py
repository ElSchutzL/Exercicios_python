alturas = []

while True:
    altura = float(input("Digite uma altura (0 para sair): "))
    if altura == 0:
        break
    alturas.append(altura)

if alturas:
    print("Menor altura:", min(alturas))
    print("Maior altura:", max(alturas))
else:
    print("Nenhuma altura informada.")