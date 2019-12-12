# Na primeira parte o progama pergunta a quantidade de corida feita pelo motorista
def coridas ():
    quantas_coridas = int(input('quantas corridas voce fez hoje?  '))
    n_coridas = ''

    for c in quantas_coridas:
        n_coridas += (c+c)
    
