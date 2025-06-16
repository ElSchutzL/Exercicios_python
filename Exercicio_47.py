chico = 1.5
juca = 1.1

crescchico = 0.02
crescjuca = 0.03

anos = 0

while chico >= juca:
    chico += crescchico
    juca += crescjuca
    anos += 1

print(f"Serão necessários {anos} anos para que Juca se torne maior que Chico")