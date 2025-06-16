cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0

for v in range(1, 101):
    voto = int(input("informe seu voto: "))

    if voto == 1:
        cand1 = cand1 + 1
    elif voto == 2:
        cand2 = cand2 + 1
    elif voto == 3:
        cand3 = cand3 + 1
    elif voto == 4:
        cand4 = cand4 + 1
    elif voto == 5:
        nulo = nulo + 1
    elif voto == 6:
        branco = branco + 1
    else:
        print("Valor informado não foi computado.")

print(f"O candidato 1 recebeu {cand1} votos")
print(f"O candidato 2 recebeu {cand2} votos")
print(f"O candidato 3 recebeu {cand3} votos")
print(f"O candidato 4 recebeu {cand4} votos")
print(f"{nulo} votos foram nulos")
print(f"{branco} votos foram em branco")