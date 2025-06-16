salarioProf = None
nomeProf = input("Informe seu nome: ")
nivel = int(input("Informe:\n 1 - Nível 1\n 2 - Nível 2\n 3 - Nível 3: "))
horasTrabalhada = int(input("Informe quantas horas foram trabalhadas: "))

if nivel == 1:
    salarioProf = horasTrabalhada * 12.00
elif nivel == 2:
    salarioProf = horasTrabalhada * 17.00
elif nivel == 3:
    salarioProf = horasTrabalhada * 25.00
else:
    print("Nível inexistente.")

print(f"O salário do professor é de {salarioProf}")