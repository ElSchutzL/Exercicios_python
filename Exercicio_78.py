class Fracao:
    def __init__(self, n, d=1):
        self.n = n
        self.d = d

    def __add__(self, outra):
        cima = self.n * outra.d + outra.n * self.d
        baixo = self.d * outra.d
        return Fracao(cima, baixo)

    def __mul__(self, outra):
        return Fracao(self.n * outra.n, self.d * outra.d)

    def __str__(self):
        if self.d == 1:
            return f"{self.n}"
        else:
            return f"{self.n}/{self.d}"


f1 = Fracao(2, 3)
f2 = Fracao(1, 4)
f3 = Fracao(5, 1)

print(f1 + f2)
print(f1 * f2)
print(f3 + f3)