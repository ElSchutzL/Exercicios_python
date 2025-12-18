def conta_caracteres(s):
    """
    ENTRADA: Uma string 's' com caracteres em letra minúscula
    SAÍDA: Uma tupla onde o primeiro elemento é o número de vogais e o segundo é o número de consoantes.
    """
    vogais = "aeiou"
    consoantes = "bcdfghijklmnpqrstvwxyz"
    qtd_vogais = 0
    qtd_consoantes = 0

    for c in s:
        if c in vogais:
            qtd_vogais += 1
        elif c in consoantes:
            qtd_consoantes += 1

    return (qtd_vogais, qtd_consoantes)


palavra = str(input("Insira a palavra: "))
print(conta_caracteres(palavra))