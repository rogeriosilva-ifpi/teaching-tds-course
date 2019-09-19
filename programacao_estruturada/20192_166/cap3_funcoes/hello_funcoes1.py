def programa_principal():
    # entrada
    nome = input('Nome: ')
    salario_fixo = float(input('Salario R$: '))
    total_vendas = float(input('Total Vendas R$: '))

    # processamento
    comissao = calcular_percentual(total_vendas, 15)
    salario_final = salario_fixo + comissao

    # saída
    print('Vendedor', nome)
    print('Salário Fixo R$', salario_fixo)
    print('Comissão R$', comissao)
    print(' Salário Final R$', salario_final)


def calcular_percentual(valor, porcento):
    resultado = valor * (porcento/100)
    return resultado


programa_principal()
