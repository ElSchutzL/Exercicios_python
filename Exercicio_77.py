class Fracao:
    def __init__(self, numerador, denominador):
        self.n = numerador
        self.d = denominador

    def multiplica(self, outra):
        return (self.n * outra.n) / (self.d * outra.d)

    def soma(self, outra):
        baixo = self.d * outra.d
        cima = self.n * outra.d + outra.n * self.d
        return cima / baixo
    
    def obter_inverso(self):
        return Fracao(self.d, self.n)

    def inverte(self):
        self.n, self.d = self.d, self.n


f1 = Fracao(2, 3)
f2 = Fracao(1, 4)

print("Soma:", f1.soma(f2))

inv = f1.obter_inverso()
print("Inverso obtido:", inv.n, "/", inv.d)

f1.inverte()
print("Após inverter:", f1.n, "/", f1.d)