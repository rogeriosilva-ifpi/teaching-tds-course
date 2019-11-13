def programa():
    nome = input('Nome? ')

    for i in range(len(nome)-1, -1, -1):
        print(i, nome[i])


programa()
