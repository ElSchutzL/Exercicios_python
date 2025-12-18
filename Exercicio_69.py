def calcula_aumento(v):
    """
    ENTRADA: Um valor numérico 'v' representando um salário.
    SAÍDA: O valor inicial 'v' após passar por um aumento de 15%
    """
    return v * 1.15


def calcula_desconto(v):
    """
    ENTRADA: Um valor numérico 'v' representando um salário.
    SAÍDA: O valor inicial 'v' após passar por um desconto de 5% de impostos
    """
    return v * 0.95


def calcula_salario_final(v):
    """
    ENTRADA: Um valor numérico 'v' representando um salário.
    SAÍDA: O valor inicial 'v' após passar pelo aumento de 15% e o desconto de 5%
    """
    salario_com_aumento = calcula_aumento(v)
    salario_final = calcula_desconto(salario_com_aumento)
    return salario_final

salario_inicial = float(input("Digite o salário do funcionário: R$ "))
salario_com_aumento = calcula_aumento(salario_inicial)
salario_final = calcula_salario_final(salario_inicial)

print(f"Salário inicial: R$ {salario_inicial}")
print(f"Salário com aumento: R$ {salario_com_aumento}")
print(f"Salário final (após desconto de 5%): R$ {salario_final}")