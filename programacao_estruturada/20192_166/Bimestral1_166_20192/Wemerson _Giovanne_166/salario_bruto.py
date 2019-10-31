def pao():
    nome = input('Seu nome: ')
    regime = int(input('seu regime de trabalho: '))
    qualificacao = input('sua qualificação: ')


    if regime == 20:
        print(salario)
    else:
        salario = 4500
        print(salario)
    if qualificacao == 'E':
        adicional = 30/100
        print(adicional)
    elif qualificacao == 'M':
        adicional = 52/100
        print(adicional)
    elif qualificacao == 'D':
        adicional = 70/100
        print(adicional)
    else:
        print('não deu')

    salario_bruto = salario + (salario * adicional)
    previdencia = salario_bruto * (11//100)
    imposto_renda = salario_bruto * (27.5//100)
    descontos = imposto + previdencia
    previdencia = imposto + previdencia
    salario_liquido = salario_bruto - descontos

    print('salario_bruto', salario_bruto)
    print('previdencia', previdencia)
    print('imposto_renda', imposto)
    print('salario_liquido', salario_liquido)


pao()