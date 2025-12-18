def marcar_pontos(x, memo=None):
    if memo is None:
        memo = {}
    
    if x == 0:
        return 1
    if x < 0:
        return 0
    
    if x in memo:
        return memo[x]
    memo[x] = marcar_pontos(x-1, memo) + marcar_pontos(x-2, memo) + marcar_pontos(x-3, memo)
    
    return memo[x]

print(marcar_pontos(1))   # 1
print(marcar_pontos(2))   # 2
print(marcar_pontos(3))   # 4
print(marcar_pontos(4))   # 7
print(marcar_pontos(5))   # 13
print(marcar_pontos(6))   # 24
print(marcar_pontos(7))   # 44
print(marcar_pontos(8))   # 81
print(marcar_pontos(30))  # 53798080
print(marcar_pontos(100)) # 180396380815100901214157639