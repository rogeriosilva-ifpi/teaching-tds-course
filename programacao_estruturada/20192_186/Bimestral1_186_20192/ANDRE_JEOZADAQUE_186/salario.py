nome = input('Digite o nome:')
regime_trabalho = int(input('Digite o regime de trabalho - 20 ou 40:'))
adicional = input('Digite o adicional - E, M ou D:')
if regime_trabalho == 20:
    if adicional == 'E':
        salario_bruto = 2500 + (30*2500)/100
        descontos = (38,5 * salario_bruto)/100
        salario_liquido = salario_bruto - descontos
        print('O salario bruto é', salario_bruto)
    elif adicional == 'M':
        salario_bruto = 2500 + (52*2500)/100
        descontos = (38,5 * salario_bruto)/100
        salario_liquido = salario_bruto - descontos
        print('O salario bruto é', salario_bruto)
    elif adicional == 'D':
        salario_bruto = 2500 + (70*2500)/100
        descontos = (38,5 * salario_bruto)/100
        salario_liquido = salario_bruto - descontos
        print('O salario bruto é', salario_bruto)
    else:
        print('invalido')
if regime_trabalho == 40:
    if adicional == 'E':
        salario_bruto = 4500 + (30*4500)/100
        descontos = (38,5 * salario_bruto)/100
        salario_liquido = salario_bruto - descontos
        print('O salario bruto é', salario_bruto)
    elif adicional == 'M':
        salario_bruto = 4500 + (52*4500)/100
        descontos = (38,5 * salario_bruto)/100
        salario_liquido = salario_bruto - descontos
        print('O salario bruto é', salario_bruto)
    elif adicional == 'D':
        salario_bruto = 4500 + (70*4500)/100
        descontos = (38,5 * salario_bruto)/100
        salario_liquido = salario_bruto - descontos
        print('O salario bruto é', salario_bruto)
    else:
        print('invalido')


    

