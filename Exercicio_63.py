# Escreva um programa que:

# 1) Salva um número secreto em uma variável
# 2) Pede para o usuário adivinhar o número
# 3) Imprime 'True' ou 'False' dependendo do usuário ter adivinhado corretamente ou não.
# 4) Se o usuário errou, o programa deve avisar se o número correto é maior ou menor que o número dito pelo usuário.

import random
import os

aleatorio = random.randint(1, 1000)
print(f"Descubra qual o número de 1 a 1000")

tentativas = 0

while True:
    numero_inserido = int(input("Insira o número:"))
    if numero_inserido == aleatorio:
        print(f"Você acertou, parabéns")
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    elif numero_inserido > aleatorio:
        print(f"O número correto é menor")
        tentativas += 1
        continue
    elif numero_inserido < aleatorio:
        print(f"O número correto é maior")
        tentativas += 1
        continue
print(f"Você acertou o número em", tentativas, "tentativas")