num = int(input("Insira o número da tabuada: "))
tabuada = 1

while tabuada <= 10:
    result = num * tabuada
    print(f"{num} x {tabuada} = {result}")
    tabuada += 1