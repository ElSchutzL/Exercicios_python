# Você se formou e conseguiu um emprego. Agora quer comprar uma casa. Para isso, irá economizar uma porcentagem de seu
# salário todo mês e colocar em uma caderneta de poupança.

# Faça um programa que pergunta para o usuário:

# 1) Qual o seu salário.
# 2) Qual a porcentagem que ele deseja economizar todo mês.
# 3) Qual o preço da casa.

# O programa deve imprimir quantos meses de salário você deve economizar para conseguir a casa, assumindo que você
# pode comprar ela à partir do momento que conseguir pagar 25% de seu valor como entrada.
# Assuma que a cada mês, o valor que você tinha economizado até então, rendeu 0,5% a mais desde o mês anterior.

salario = float(input("Insira seu salário: "))
porcent = float(input("Insira a porcentagem que você deseja economizar todo mês: "))
casa = float(input("Insira o preço da casa: "))

dindin_mes = salario * (porcent / 100)
entrada = 0.25 * casa
dindin_rendendo = 0
meses = 0

while True:
    dindin_rendendo *= 1.005 
    dindin_rendendo += dindin_mes
    meses += 1
    if dindin_rendendo >= entrada:
        print(f"Em", meses, "meses você consegue dar entrada na casa")
        print(f"Em", meses/12, "anos você consegue dar entrada na casa")
        while True:
            dindin_rendendo *= 1.005
            dindin_rendendo += dindin_mes
            meses += 1
            if dindin_rendendo >= casa:
                print(f"Em", meses, "meses você consegue quitar a casa")
                print(f"Em", meses/12, "anos você consegue quitar a casa")
                break
        break