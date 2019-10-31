def programa():
    nome = input('Nome do profissional\n>>> ')
    regime_trabalho = int(input('20 ou 40 hrs\n >>> '))
    qualifica = input('qual sua qualificação E,M ou D\n>>> ')
    salariofixo = 0
    adicional = 0
    if regime_trabalho == 20:
        salariofixo = 2500
    elif regime_trabalho == 40:
        salariofixo = 4500
    if qualifica.upper() == 'E':
        adicional = (salariofixo + salariofixo * (30/100))
    elif qualifica.upper() == 'M':
        adicional = salariofixo + salariofixo * (52/100)
    else:
        adicional = salariofixo + salariofixo * (70/100)
    salarioliquido = desconto(adicional)
    print(f'Olá {nome} seu salario bruto é {adicional}, seu salario liquido é {salarioliquido}')

def desconto(adicional):
    previdencia = adicional * (11/100)
    ir = adicional * (27.5/100)
    salario = adicional - previdencia - ir
    return salario


programa()    