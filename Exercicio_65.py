def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

contador = 0
n = 2

print("Os 100 primeiros números primos são:")
while contador < 100:
    if primo(n):
        print(n, end=" ")
        contador += 1
    n += 1