def principal():
    qtd_acoes = int(input('Quantas ações: '))

    contador_corretos = 0
    contador_incorretos = 0
    contador_on = 0
    contador_pn = 0
    contador_unit = 0

    for i in range(qtd_acoes):
        acao = input('Código >>> ')

        if nome_valido(acao):
            # contador_corretos = contador_corretos + 1
            contador_corretos += 1
            
            # verificar o tipo de acao
            numero = int(acao[4:])
            if numero == 3:
                contador_on += 1
            elif numero == 4:
                contador_pn += 1
            else: # 11
                contador_unit += 1
        else:
            contador_incorretos += 1

    # saídas
    print('Nomes válidos: ', contador_corretos)
    print('Nomes inválidos: ', contador_incorretos)
    print('Qtd de ON: ', contador_on)
    print('Qtd de PN: ', contador_pn)
    print('Qtd de UNIT: ', contador_unit)


def nome_valido(nome):
    letras = nome[0:4]
    # verificacao de letras
    for letra in letras:
        if letra < 'A' or letra > 'Z':
            return False

    # numero
    numero = int(nome[4:])
    if numero == 3 or numero == 4 or numero == 11:
        return True
    else:
        return False


principal()
