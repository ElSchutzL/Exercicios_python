valorfatorar = int(input("Informe um valor: "))
contador = valorfatorar
fatorial = 1
calculo = ""

while contador > 0:
    fatorial = fatorial * contador

    calculo += str(contador)  # Adiciona o número ao cálculo
    if contador > 1:
        calculo += " x "
    else:
        calculo += " = "

    contador -= 1

print(f"{valorfatorar}! = {calculo}{fatorial}")