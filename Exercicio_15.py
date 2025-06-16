idade = int(input("Insira sua idade: "))

if 0<=idade<=4:
    categoria = "inexistente"
    print (f"Não possuímos categoria para essa idade")
elif 5<=idade<=7:
    categoria = "Infantil A"
    print (f"Sua categoria é {categoria}")
elif 8<=idade<=10:
    categoria = "Infantil B"
    print (f"Sua categoria é {categoria}")
elif 11<=idade<=13:
    categoria = "Juvenil A"
    print (f"Sua categoria é {categoria}")
elif 14<=idade<=17:
    categoria = "Juvenil B"
    print (f"Sua categoria é {categoria}")
elif idade>=18:
    categoria = "Adulto"
    print (f"Sua categoria é {categoria}")
else:
    categoria = "idade inválida"
    print (f"A idade informada deve ser válida")