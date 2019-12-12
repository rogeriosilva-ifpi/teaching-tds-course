def main():
    partida = int(input('Quantas partidas você fez? '))
    
    valor_total = 0

    for p in range(2):
        vitoria = int(input('Digite quantidade de vitoria: '))
        empate = int(input('Digite quantidade de empate:' ))
        vitoria2 = vitoria*3
        empate2 = empate*1
    valor_total = vitoria2 + empate2


    print(valor_total)



main()
