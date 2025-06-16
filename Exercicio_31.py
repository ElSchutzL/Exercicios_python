print(f"Insira valores reais ")
numtab = int(input("Insira a tabuada desejada: "))

for n in range(numtab, 101):
    resultado = numtab * n
    print(f"{numtab} x {n} = {resultado}")