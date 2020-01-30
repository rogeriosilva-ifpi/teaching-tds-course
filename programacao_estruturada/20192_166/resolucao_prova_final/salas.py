def main():
    nome_escola = input('Nome da escola: ')
    sigla = input('Sigla: ')
    qtd_salas = int(input('Quantidade de salas: '))

    gerar_sala(sigla, qtd_salas)


def gerar_sala(sigla, qtd):
    for i in range(1, qtd+1):
        num = str(i)
        if i < 10:
            num = '0' + str(i)

        sala = sigla + '-' + num
        print(sala)


main()
