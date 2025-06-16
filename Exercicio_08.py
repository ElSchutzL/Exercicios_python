ano_nascimento = int(input("Insira o ano em que você nasceu: "))
ano_atual = 2025

diferença_anos = ano_atual - ano_nascimento

idade_anos = diferença_anos
idade_meses = diferença_anos *12
idade_dias = diferença_anos *365
idade_semanas = diferença_anos * 52
idade_minutos = diferença_anos * 525960
idade_segundos = diferença_anos * 31557600

print("Sua idade é:", "\n",
      "em anos:", idade_anos, "\n",
      "em meses:", idade_meses, "\n",
      "em dias:", idade_dias, "\n",
      "em semanas:", idade_semanas, "\n"
      "em minutos:", idade_minutos, "\n"
      "em segundos:", idade_segundos
      )