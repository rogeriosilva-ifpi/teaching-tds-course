def programa():
    # entrada
    nome = input('Digite seu nome: ')
    idade = int(input('Digite a idade: '))

    if idade >= 18:
        print('Parabens', nome, 'voce ja e de maior')
    else:
        print('Infelizmente voce ainda e um bebezinho')

    print('fim')


programa()
