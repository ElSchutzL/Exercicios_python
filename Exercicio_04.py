salario_inicial = float(input("Insira seu salário fixo: "))
vendas = float(input("Insira a quantos reais você conseguiu vender esse mês: "))

comissao = vendas * 0.04
salario_final = salario_inicial + comissao

print ("O seu salário fixo é de", salario_inicial, "reais, a comissão que você obteve com", vendas,
       "reais em vendas é de", comissao, "reais")
print ("O seu salário final é de", salario_final, "reais")