def eh_triangular(n):
    """
    Entrada: um inteiro positivo 'n'.
    Saída: True, se 'n' é um número triangular. Isto é, ele é a soma de números naturais
           sequenciais começando em 1. Exemplo: 1+2+3+...+k
    """
    total = 0
    for i in range(1, n+1):  # começa em 1 e vai até n
        total += i
        if total == n:
            return True  # achou, retorna imediatamente
        elif total > n:
            return False  # passou do valor, não pode mais ser triangular
    return False

print("+++++++++++++++")
print(f"4: {eh_triangular(4)}") # Deve imprimir 'False'
print("+++++++++++++++")
print(f"6: {eh_triangular(6)}") # Deve imprimir 'True'
print("+++++++++++++++")
print(f"1: {eh_triangular(1)}") # Deve imprimir 'True'
print("+++++++++++++++")