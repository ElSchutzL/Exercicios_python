tmin = float(input("Insira o tempo em minutos: "))
hora = 0
min = 0
seg = 0

if tmin>=60:
    hora = tmin//60
    tmin = tmin - (hora*60)

if tmin>=1:
    min = tmin//1
    tmin = tmin - (min)
    
if tmin<1:
    seg = 60*tmin
    tmin = tmin - (seg)
    
hora = int(hora)
min = int(min)
seg = int(seg)

print (f"O tempo em minutos que você inseriu é equivalente a:\n {hora} horas, {min} minutos e {seg} segundos")
