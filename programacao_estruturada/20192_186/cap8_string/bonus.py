def programa():

    nomes = ['Maria da Silva', 'Joaquim jose',
             'Luis da Silva', 'Maria Teresa', 'Silva Jr']

    qtd = int(input('Quantos nomes quer add? '))

    for i in range(qtd):
        nome = input('Nome: ')
        nomes.append(nome)

    chave = input('Busca ... ').upper()

    for nome in nomes:
        if chave in nome.upper():
            print(nome)


programa()
