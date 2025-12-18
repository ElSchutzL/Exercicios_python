texto = input("Insira o texto: ")

def eh_palindromo(s):
    """
    Entrada: Uma string s
    Saída: Retorna True se 's' é um palíndromo, e False caso contrário.
    """
    return s == s[::-1]

if eh_palindromo(texto):
    print("É palíndromo")
else:
    print("Não é palíndromo")