cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo = 0
branco = 0
ordemvotar = 1

pessoasvotar = int(input("Informe quantas pessoas irão votar: "))

while ordemvotar <= pessoasvotar:
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

    ordemvotar += 1

porc1 = (cand1 / pessoasvotar) * 100
porc2 = (cand2 / pessoasvotar) * 100
porc3 = (cand3 / pessoasvotar) * 100
porc4 = (cand4 / pessoasvotar) * 100
porcn = (nulo / pessoasvotar) * 100
porcb = (branco / pessoasvotar) * 100

if porc1 > 50 or porc2 > 50 or porc3 > 50 or porc4 > 50:
    print("Não será necessário um segundo turno")

print(f"Do total de {pessoasvotar} pessoas que votaram:")
print(f"O candidato 1 recebeu {cand1} votos, que representam {porc1}%")
print(f"O candidato 2 recebeu {cand2} votos, que representam {porc2}%")
print(f"O candidato 3 recebeu {cand3} votos, que representam {porc3}%")
print(f"O candidato 4 recebeu {cand4} votos, que representam {porc4}%")
print(f"{nulo} votos foram nulos, que representam {porcn}%")
print(f"{branco} votos foram em branco, que representam {porcb}%")