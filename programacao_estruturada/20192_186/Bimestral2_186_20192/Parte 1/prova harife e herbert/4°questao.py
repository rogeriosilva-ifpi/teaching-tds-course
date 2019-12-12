print('o animal é vetebrado ou invertebrado?')
palavra = input('resposta \n >>>>>>> ')

if palavra == 'vertebrado':
    tipo_de_animal = input('o animal é ave ou mamifero? \n >>>>>')
    if tipo_de_animal == 'ave':
        alimento = input('é carnivoro ou onivoro? ')
        if alimento == 'carnivoro':
            print('é uma aguia')
        else:
            print('é um pombo')
    elif tipo_de_animal == 'mamifero':
        alimento = input('é onivoro ou herbivoro?')
        if alimento == 'onivoro':
            print('é um homem')
        else:
            print('é uma vaca')        
elif palavra == 'invertebrado':
    tipo_de_animal = input('o animal é inseto ou anelideo?')
    if tipo_de_animal == 'inseto':
        alimento = input('é hematofogo ou herbivoro?')
        if alimento == 'hematofogo':
            print('é uma pulga')
        else:
            print('é uma lagarta')
    elif tipo_de_animal == 'anelideo':
        alimento = input('é hematofogo ou onivoro?')
        if alimento == 'hematofogo':
            print('é um sanguessuga')
        else:
            print('é uma minhoca')