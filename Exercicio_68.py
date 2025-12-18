palavra_usuario = input("Digite uma palavra: ")

def mantem_consoantes(palavra): 
    """
    Entrada: 'palavra' é uma string formada por letras minúsculas
    Saída: Retorna uma string contendo apenas as consoantes de 'palavra'
    na mesma ordem em que aparecem
    """
    vogais = "aeiou"
    resultado = ""
    for letra in palavra:
        if letra not in vogais:
            resultado += letra
    return resultado

resultado = mantem_consoantes(palavra_usuario)

print("Somente as consoantes:", resultado)