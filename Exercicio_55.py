lista = []
tamanho = int(input("Informe o tamanho da lista: "))

for i in range(tamanho):
    valor = int(input(f"Digite o {i+1}º valor: "))
    lista.append(valor)

lista.reverse()

print("Lista invertida:", lista)