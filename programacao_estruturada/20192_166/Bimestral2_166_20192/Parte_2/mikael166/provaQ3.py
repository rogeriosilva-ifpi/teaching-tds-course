jogou=int(input("quantas partidas foram jogadas? "))

for i in range(jogou):
    r = int(input("resultado cada partida? "))
    contador = r + r
pontos_v = contador + (3/100)
pontos_e = contador + (1/100)

print("pontos;",pontos_v)
print("pontos",pontos_e)
   
