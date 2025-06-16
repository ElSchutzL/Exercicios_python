qtdnum =  int(input("Quantos números devem ser lidos: "))

v0_25 = 0
v26_50 = 0
v51_75 = 0
v76_100 = 0
valordiferente = 0

while qtdnum > 0:
    valor = int(input("Informe o valor: "))
    
    if 0 <= valor <= 25:
        v0_25 += 1

    elif 26 <= valor <= 50:
        v26_50 += 1

    elif 51 <= valor <= 75:
        v51_75 += 1

    elif 76 <= valor <= 100:
        v76_100 += 1

    else:
        valordiferente += 1

    qtdnum = qtdnum - 1

print(f"{v0_25} números então entre o intervalo [0;25]")
print(f"{v26_50} números então entre o intervalo [26,50]")
print(f"{v51_75} números então entre o intervalo [51,75]")
print(f"{v76_100} números então entre o intervalo [76,100]")
print(f"{valordiferente} números não estão dentro de nenhum intervalo")