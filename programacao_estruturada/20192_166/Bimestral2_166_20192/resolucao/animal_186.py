def programa():
    palavra1 = input('Palavra 1')
    palavra2 = input('Palavra 2')
    palavra3 = input('Palavra 3')

    if palavra1 == 'vertebrado':
        if palavra2 == 'ave':
            if palavra3 == 'carnivoro':
                print('Águia')
            elif palavra3 == 'onivoro':
                print('Pomba')
        elif palavra2 == 'mamifero':
            if palavra3 == 'onivoro':
                print('Homem')
            elif palavra3 == 'herbivoro':
                print('Vaca')
    elif palavra1 == 'invertebrado':
        if palavra2 == 'inseto':
            if palavra3 == 'hematofago':
                print('Pulga')
            elif palavra3 == 'herbivoro':
                print('Largata')
        elif palavra2 == 'anelideo':
            if palavra3 == 'hematofago':
                print('Sanguessuga')
            elif palavra3 == 'onivoro':
                print('Minhoca')


programa()
