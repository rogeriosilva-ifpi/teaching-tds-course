import os


def programa():
    num1 = int(input('Número 1 >>> '))
    num2 = int(input('Número 2 >>> '))

    nome_programa = '\n ** *** MENU ** ***\n'
    menu = nome_programa + '1 - Soma\n2 - Diferença\n3 - Produto\n\n0 - Sair\n>>> '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            soma(num1, num2)
        elif opcao == 2:
            diferenca(num1, num2)
        elif opcao == 3:
            produto(num1, num2)
        else:
            print('Opção inválida!!!')

        input('Pressione <enter>...')
        os.system('clear')
        opcao = int(input(menu))


def soma(n1, n2):
    r = n1 + n2
    print(f'A soma de {n1} com {n2} = {r}')


def diferenca(n1, n2):
    r = n1 - n2
    print(f'A diferença de {n1} e {n2} = {r}')


def produto(n1, n2):
    r = n1 * n2
    print(f'O produto de {n1} e {n2} = {r}')


programa()
