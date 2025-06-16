num_ident_aluno = int(input("Insira o número de indentificação do aluno: "))
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

me = (nota1+nota2+nota3)/3
ma = (nota1 + nota2*2 + nota3*3 + me)/7
classific = None
result = None

if 10>=ma>=9:
    classific=="A"
elif 9>ma>=7.5:
    classific=="B"
elif 7.5>ma>=6:
    classific=="C"
elif 6>ma>=4:
    classific=="D"
elif 4>ma>=0:
    classific=="E"
else:
    print("Média é inválida, insira as notas novamente")

if classific=="A" or classific=="B" or classific=="C":
    result=="APROVADO"
else:
    result=="REPROVADO"

if nota1>10 or 0>nota1 or nota2>10 or 0>nota2 or nota3>10 or 0>nota3:
    print(f"Notas estão erradas, coloque-as novamente")
else:
    print(f"Número do aluno: {num_ident_aluno}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Média dos exercícios: {me}")
    print(f"Média de aproveitamento: {ma}")
    print(f"Conceito correspondente: {classific}")
    print(f"Resultado final: {result}")