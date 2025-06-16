caes_atendidos = int(input("Informe quantos cães foram atendidos: "))

if caes_atendidos < 20:
    print("Pet shop está ocioso")
elif 20 <= caes_atendidos <= 30:
    print("Pet shop está normal")
elif caes_atendidos > 30:
    print("Pet shop com carga alta de demanda")
else:
    print("Número inválido, verifique o valor informado")
