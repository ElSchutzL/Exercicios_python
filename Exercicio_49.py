print(f"Insira valores reais entre 1 e 64")
numero = int(input("Insira a casa do tabuleiro: "))
soma = 0
numeroo = 0

if numero <= 64 and numero >=1:
    for n in range(1, numero + 1):
        numeroo = 2 ** (n - 1)
        print(f"Número de grãos da {n} casa é de {numeroo} grãos")
        soma = soma + numeroo
else:
    soma = "inexistente"

print(f"A soma é de {soma}")