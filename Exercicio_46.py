qtdnum =  10
negat = 0
positivo = 0

while qtdnum > 0:
    num = int(input("Informe o valor: "))
    
    if 0 > num:
        negat += num

    qtdnum = qtdnum - 1

print(f"O somatório dos números negativos é de {negat}")