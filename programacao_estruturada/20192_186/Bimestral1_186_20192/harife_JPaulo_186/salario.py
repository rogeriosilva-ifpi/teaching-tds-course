nome = str(input('Digite seu nome: '))
carga_h = int(input('Coloque sua carga horaria, 20 ou 40 horas \n >>> '))
qualificacao = str(input(
    'Coloque sua qualificação \n Digite E para especialista \n Digite M para mestre \n Digite D para doutor \n >>> '))


def calculo_salario():
    if carga_h == 20:
        basefixa = 2500
    elif carga_h == 40:
        basefixa = 4500
    else:
        print('Carga horaria desconhecida')

    if qualificacao == 'E':
        adicional = 0.3 * basefixa
    elif qualificacao == 'M':
        adicional = 0.52 * basefixa
    elif qualificacao == 'D':
        adicional = 0.7 * basefixa
    else:
        print('Qualificação desconhecida')

    salario_bruto = basefixa + adicional
    previdencia = 0.11 * salario_bruto
    irrf = 0.275 * salario_bruto
    salario_liquido = salario_bruto - previdencia - irrf

    print('O salario bruto do professor', nome, 'é',
          salario_bruto, 'e o salario liquido é', salario_liquido)
    print('Os descontos foram de', previdencia,
          'da previdencia e', irrf, 'do imposto de renda')


calculo_salario()
