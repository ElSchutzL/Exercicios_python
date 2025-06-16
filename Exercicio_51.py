Listapessoas = ["Pessoa1", "Pessoa2", "Pessoa3", "Pessoa4", "Pessoa5", "Pessoa6"]

print(f"Toda a lista dos The Boys: {Listapessoas}")
print(f"A pessoa no index = 0 é: {Listapessoas[0]}")
print(f"A pessoa no index = 1 é: {Listapessoas[1]}")
print(f"A pessoa no index = 2 é: {Listapessoas[2]}")
print(f"A pessoa no index = 3 é: {Listapessoas[3]}")
print(f"A pessoa no index = 4 é: {Listapessoas[4]}")
print(f"A pessoa no index = 5 é: {Listapessoas[5]}")

print(f"Listapessoas = {Listapessoas}")
print(f"Listapessoas[1:] = {Listapessoas[1:]}")
print(f"Listapessoas[:1] = {Listapessoas[:1]}")
print(f"Listapessoas[1:2] = {Listapessoas[1:2]}")
print(f"Listapessoas[2:1] = {Listapessoas[2:1]}")
print(f"Listapessoas[1:1] = {Listapessoas[1:1]}")
print(f"Listapessoas[3:3] = {Listapessoas[3:3]}")
print(f"Listapessoas[3:] = {Listapessoas[3:]}")
print(f"Listapessoas[:3] = {Listapessoas[:3]}")
print(f"Listapessoas[3:2] = {Listapessoas[3:2]}")
print(f"Listapessoas[::2] = {Listapessoas[::2]}")
print(f"O tamanho da minha lista é de: {len(Listapessoas)}")

Listapessoas.append("Pessoa7")

print(f"Listapessoas = {Listapessoas}")
print(f"O tamanho da minha lista é de: {len(Listapessoas)}")

Listapessoas.insert(1, "Pessoa8")
print(f"Listapessoas = {Listapessoas}")
print(f"O tamanho da minha lista é de: {len(Listapessoas)}")

Listapessoas.pop(1)

print(f"Listapessoas = {Listapessoas}")
print(f"O tamanho da minha lista é de: {len(Listapessoas)}")

Listapessoas.reverse()

print(f"Listapessoas = {Listapessoas}")
print(f"O tamanho da minha lista é de: {len(Listapessoas)}")
