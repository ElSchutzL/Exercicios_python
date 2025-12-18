def soma_len(L):
    if not L:
        return 0
    return len(L[0]) + soma_len(L[1:])

# Testes
teste = ["oi", "ai", "casa"]
print(soma_len(teste))  # Deve imprimir 8
print(soma_len([]))     # Deve imprimir 0