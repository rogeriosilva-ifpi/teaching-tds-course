def programa():

    nomes = ['Maria da Silva', 'Joaquim jose',
             'Luis da Silva', 'Maria Teresa', 'Silva Jr']

    chave = input('Busca ... ').upper()

    for nome in nomes:
        if chave in nome.upper():
            print(nome)


programa()
