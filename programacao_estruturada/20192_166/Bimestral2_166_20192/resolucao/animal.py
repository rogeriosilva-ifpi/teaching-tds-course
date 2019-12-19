def programa():
    palavra1 = input('Palavra 1:')
    palavra2 = input('Palavra 2:')
    palavra3 = input('Palavra 3:')

    if palavra1 == 'vertebrado':
        if palavra2 == 'ave':
            if palavra3 == 'carnivoro':
                print('aguia')
            elif palavra3 == 'onivoro':
                print('pomba')
            else:
                print('Palavra 3 inválida!')
        elif palavra2 == 'mamifero':
            if palavra3 == 'onivoro':
                print('homem')
            elif palavra3 == 'herbivoro':
                print('vaca')
            else:
                print('Palavra 3 inválida')
        else:
            print('Palavra 2 inválida!')
    elif palavra1 == 'invertebrado':
        if palavra2 == 'inseto':
            if palavra3 == 'hematofago':
                print('pulga')
            elif palavra3 == 'herbivoro':
                print('lagarta')
            else:
                print('Palavra 3 inválida!')
        elif palavra2 == 'anelideo':
            if palavra3 == 'hematofago':
                print('sanguessuga')
            elif palavra3 == 'onivoro':
                print('minhoca')
            else:
                print('Palavra 3 inválida')
        else:
            print('Palavra 2 inválida!')
    else:
        print('Palavra 1 inválida')


programa()
