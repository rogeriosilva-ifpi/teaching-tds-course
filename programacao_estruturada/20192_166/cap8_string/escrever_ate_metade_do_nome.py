def programa():
    nome = input('Nome: ')

    # for letra in nome:
    #     print(letra)

    tamanho = len(nome) // 2
    for i in range(tamanho):
        print(nome[i])


programa()
