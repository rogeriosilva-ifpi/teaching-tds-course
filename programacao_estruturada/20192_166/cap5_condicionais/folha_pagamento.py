def programa():
    horas = int(input('Qtd Horas: '))
    valor_hora = int(input('Valor: '))

    salario_bruto = horas * valor_hora
    imposto_renda = calcular_ir(salario_bruto)
    taxa_sindicato = salario_bruto * (3/100)
    fgts = salario_bruto * (11/100)

    salario_liquido = salario_bruto - imposto_renda - taxa_sindicato

    print('Salário Bruto R$ %.2f' % salario_bruto)
    print('Imposto de Renda R$ %.2f' % imposto_renda)
    print('Taxa do Sindicato R$ %.2f' % taxa_sindicato)
    print('FGTS depositado R$ %.2f' % fgts)
    print('Salário Líquido R$ %.2f' % salario_liquido)


def calcular_ir(s):
    if s <= 900:
        return 0
    elif s <= 1500:
        return s * (5/100)
    elif s <= 2500:
        return s * (10/100)
    else:
        return s * (20/100)


programa()
