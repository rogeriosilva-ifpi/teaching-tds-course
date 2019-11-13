nome = input('Nome do professsor: ')
regime = int(input('Regime de trabalho (20h ou 40h): '))
qualificacao = input('Qualificação do professor (E, M ou D): ')


def salario(nome, regime, qualificacao):
    if regime == 20:
        if qualificacao == 'E' or qualificacao == 'e':
            salario_bruto = 1.30*2500
            salario_liquido = salario_bruto*0.615
        elif qualificacao == 'M' or qualificacao == 'm':
            salario_bruto = 1.52*2500
            salario_liquido = salario_bruto*0.615
        elif qualificacao == 'D' or qualificacao == 'd':
            salario_bruto = 1.70*2500
            salario_liquido = salario_bruto*0.615
    elif regime == 40:
        if qualificacao == 'E' or qualificacao == 'e':
            salario_bruto = 1.30*4500
            salario_liquido = salario_bruto*0.615
        elif qualificacao == 'M' or qualificacao == 'm':
            salario_bruto = 1.52*4500
            salario_liquido = salario_bruto*0.615
        elif qualificacao == 'D' or qualificacao == 'd':
            salario_bruto = 1.70*4500
            salario_liquido = salario_bruto*0.615
    return salario_liquido


print('Professor(a)', nome, 'tem salário líquido igual a R$',
      salario(nome, regime, qualificacao), '.')
