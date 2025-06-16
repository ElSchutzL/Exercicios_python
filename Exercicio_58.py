lista = []
tamanho = int(input("Digite o tamanho da lista: "))

for i in range(tamanho):
    valor = int(input(f"Digite o {i+1}º valor: "))
    if valor < 0:
        valor = 0
    lista.append(valor)

print("Lista atualizada:", lista)