print ("Sistema de média")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1+nota2)/2

if media >= 6 and media <= 10:
    situação = "APROVADO!"
elif media >= 4 and media < 6:
    situação = "RECUPERAÇÃO!"
elif media >= 0 and media < 4:
    situação = "REPROVADO!"
else:
    situação = "DADOS INCORRETOS!"
    print("Verifique as notas informadas!")