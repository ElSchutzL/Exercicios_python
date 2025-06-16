nome = input("Insira seu nome completo: ")

primeiro_nome = ""
for letra in nome:
    if letra == " ":
        break 
    else:
        primeiro_nome = primeiro_nome + letra

print("Primeiro nome na vertical:")
for letra in primeiro_nome:
    print(letra)

print("Primeiro nome na horizontal:")
print(primeiro_nome)