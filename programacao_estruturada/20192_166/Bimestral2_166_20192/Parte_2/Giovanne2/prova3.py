def prr():
    partidas = int(input('Quantidade de jogos: '))
    total = 0

    for I in range(partidas):
        redpartida = input('Qual o resultado: ')
        if redpartida == 'v':
            total = total + 3
        elif redpartida == 'e':
            total = total + 1
        else:
            pass
    
    print('O resultado é total: ', total )

prr()
