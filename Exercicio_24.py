print(f"Insira idades diferentes de 2 homens e 2 mulheres")
idade_homem1 = int(input("Digite a idade do homem 1: "))
idade_homem2 = int(input("Digite a idade do homem 2: "))
idade_mulher1 = int(input("Digite a idade da mulher 1: "))
idade_mulher2 = int(input("Digite a idade da mulher 2: "))

if idade_homem1 > idade_homem2:
    homem_velho = idade_homem1
    homem_novo = idade_homem2
else:
    homem_velho = idade_homem2
    homem_novo = idade_homem1

if idade_mulher1 < idade_mulher2:
    mulher_nova = idade_mulher1
    mulher_velha = idade_mulher2
else:
    mulher_nova = idade_mulher2
    mulher_velha = idade_mulher1

soma = homem_velho + mulher_nova
produto = homem_novo * mulher_velha

print(f"A soma das idades do homem mais velho com a mulher mais nova é {soma}")
print(f"O produto das idades do homem mais novo com a mulher mais velha é {produto}")
