saldo_medio = float(input("Insira o saldo medio do ano anterior: "))

if 0<=saldo_medio<200:
    credito = 0
elif 200<=saldo_medio<400:
    credito = saldo_medio*0.2
elif 400<=saldo_medio<600:
    credito = saldo_medio*0.3
elif 600<=saldo_medio:
    credito = saldo_medio*0.4
else:
    credito = 0

print (f"O saldo médio do ano anterior é R${saldo_medio} e o crédito que foi concedido a você é de de R${credito}")