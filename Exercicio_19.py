nota1 = float(input("Insira sua nota 1: "))
nota2 = float(input("Insira sua nota 2: "))
nota3 = float(input("Insira sua nota 3: "))

tipo_media = str(input("Vai calcular a média aritmética ou ponderada: "))

if 10>=nota1>=0 and 10>=nota2>=0 and 10>=nota3>=0:
    if tipo_media == "aritmética":
        media = (nota1+nota2+nota3)/3
        print(f"Sua média é igual a {media}")
    elif tipo_media == "ponderada":
        media = ((nota1*3)+(nota2*3)+(nota3*4))/12
        print(f"Sua média é igual a {media}")
    else:
        media = "inexistente"
        print(f"Sua média é {media}")
else:
    print("Insira entre 0 e 10")
    media = "inexistente"
    print(f"Sua média é {media}")