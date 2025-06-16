nome = str(input("Insira seu nome completo: "))
caractere = 0

for c in nome:
    if c == " ":
        continue
    else:
        caractere = caractere + 1

print (F"Seu nome possui {caractere} caracteres")