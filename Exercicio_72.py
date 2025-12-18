def aplica(criterio, n):
    """
    ENTRADA:
        criterio -> função que recebe um número e retorna True ou False
        n -> inteiro >= 0
    SAÍDA:
        Retorna True se **algum inteiro** de 0 até n (inclusive) se encaixa no critério,
        caso contrário retorna False.
    """
    for i in range(n + 1):
        if criterio(i):
            return True
    return False

def eh_par(x):
    return x % 2 == 0

print(aplica(eh_par, 10))