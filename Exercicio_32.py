#Uma rainha requisitou os serviços de um monge, o qual exigiu o pagamento em grãos de trigo da seguinte maneira:
#os grãos de trigo seriam dispostos em um tabuleiro de xadrez, de tal forma que a primeira casa do tabuleiro tivesse
#um grão, e as casas seguintes o dobro da anterior.
#Construa um algoritmo que calcule quantos grãos de trigo a Rainha deverá pagar ao monge. Um tabuleiro tem 64 casas.


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