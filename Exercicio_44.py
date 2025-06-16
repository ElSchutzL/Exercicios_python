qtdnum =  int(input("Quantos números quer fatorar: "))

while qtdnum > 0:
    valorfatorarr = int(input("Informe o valor a ser fatorado: "))
    resultado = 1
    conta = 0
    valorfatorar = valorfatorarr

    while valorfatorar > 1:
        conta = valorfatorar * (valorfatorar - 1)
        resultado = resultado * conta
        valorfatorar = valorfatorar - 2

    qtdnum = qtdnum - 1
    print(f"{valorfatorarr}! = {resultado}")