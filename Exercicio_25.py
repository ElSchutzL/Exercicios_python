descricao = str(input("Insira a descrição do produto: "))
qtd_adq = float(input("Insira a quantidade adquirida: "))
preco_unit = float(input("Insira o preço unitário: "))

total = qtd_adq * preco_unit

if qtd_adq <= 5:
    desconto = 0.02 * total
elif qtd_adq > 5 and qtd_adq <= 10:
    desconto = 0.03 * total
elif qtd_adq > 10:
    desconto = 0.05 * total
else:
    desconto = 0 * total
    print ("Quantidade de produtos inválida, por favor verifique se os dados estão corretos")

total_a_pagar = total - desconto

print (f"Descrição: {descricao} \n Quantidade adquirida: {qtd_adq} \n Preço unitário: {preco_unit} \n Total sem desconto: {total} \n Desconto: {desconto} \n Total a pagar: {total_a_pagar}")
