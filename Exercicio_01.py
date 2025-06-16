moeda_01 = int(input("Quantas moedas de 1 centavo você tem: "))
moeda_05 = int(input("Quantas moedas de 5 centavos você tem: "))
moeda_10 = int(input("Quantas moedas de 10 centavos você tem: "))
moeda_25 = int(input("Quantas moedas de 25 centavos você tem: "))
moeda_50 = int(input("Quantas moedas de 50 centavos você tem: "))
moeda_1 = int(input("Quantas moedas de 1 real você tem: "))

valor_01 = moeda_01 * 1
valor_05 = moeda_05 * 5
valor_10 = moeda_10 * 10
valor_25 = moeda_25 * 25
valor_50 = moeda_50 * 50
valor_1 = moeda_1 * 100

soma = valor_01 + valor_05 + valor_10 + valor_25 + valor_50 + valor_1

total = soma/100

print("Você economizou no total", total, "reais!")