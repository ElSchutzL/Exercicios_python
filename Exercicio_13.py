print ("Cálculo de IMC")

altura = float(input("Informe sua altura em metro: "))
peso = float(input("Informe seu peso em quilos: "))

imc = peso / altura**2
imc = round(imc,2)

print ("Seu imc é:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >=25 and imc < 30:
    print("Sobrepeso")
elif imc >=30:
    print("Obesidade")

print("Fim")