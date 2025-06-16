print ("Insira abaixo dois números inteiros positivos, que sejam diferentes")
num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))

if num1==num2:
    print(f"Insira dois valores diferentes")
elif num1<=0 or num2<=0:
    print(f"Insira dois valores positivos")
else:
    conta1 = num1%num2
    conta2 = num2%num1

    if conta1==0 or conta2==0:
        print(f"São múltiplos")
    else:
        print(f"Não são múltiplos")