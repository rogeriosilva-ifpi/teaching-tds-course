nome_do_time = input('qual o nome do time: ')
quantidade_de_partidas = int(input('quantas partida seu time jogou: '))
contador = 0
pontos = 0
while contador < quantidade_de_partidas:
    contador = contador + 1
    resultado = input('empatou ou ganhou? ')
    if resultado == 'empatou':
        pontos = 1 + pontos
    if resultado == 'ganhou':
        pontos = 3 + pontos
    

print('esse é a quantidades que o time',nome_do_time,'acumulou durante o campeonato',pontos)