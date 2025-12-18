peso = float(input("Insira o peso do prato em kg: "))

def preco(peso):
    """
    Entrada: Um número qualquer 'p' representando o peso em quilos.
    Saída: Um inteiro representando o valor a pagar (em centavos).
    """

    return peso * 12


print(f"O preço a pagar é de {preco(peso)} reais")