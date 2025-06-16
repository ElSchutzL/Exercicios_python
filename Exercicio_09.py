print("Seu salário é de R$1200 e precisa pagar 2 contas que estão atrasadas, uma de R$200, outra de R$120")

conta_01 = 200
conta_02 = 120

conta_atrasada_01 = conta_01 * 1.02
conta_atrasada_02 = conta_02 * 1.02

total_conta = conta_atrasada_01 + conta_atrasada_02
salario_desconto = 1200 - total_conta

print("O seu salário de R$1200, após pagar R$", total_conta, "de multas, restará R$", salario_desconto)