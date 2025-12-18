def conta_numeros_com_raiz_perto_de(n, epsilon):
    """
    ENTRADA: 'n' é um inteiro maior que 2
                       'epsilon' é um inteiro positivo  menor que 1
    SAÍDA: Retorna quantos números inteiros tem uma raíz quadrada próxima de 'n'.
                 Uma raíz quadrada próxima é aquela que tem uma distância menor que 'epsilon' do valor 'n'.
    """
    contagem = 0
    for i in range ((n-1)**2, (n+1)**2):
        raiz = i ** (1/2)
        if (raiz > (n - epsilon)) and (raiz < (n + epsilon)):
            contagem += 1
    return contagem

print(f"{conta_numeros_com_raiz_perto_de(1, 0.1)}")
print("++++++++++")
print(f"{conta_numeros_com_raiz_perto_de(10, 0.1)}")