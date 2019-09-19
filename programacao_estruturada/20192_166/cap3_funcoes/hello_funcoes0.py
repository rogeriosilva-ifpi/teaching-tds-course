
def programa_principal():
    print('Inicio')
    saudacao('Bruno')

    valor1 = int(input('Valor 1:'))
    exp1 = int(input('Expoente: '))

    resultado = potencia(valor1, exp1)

    print(valor1, 'elevado a', exp1, '=', resultado)

    print('Fim')


def saudacao(nome_pessoa):
    print('Olá', nome_pessoa, 'by night!')
    print('Tudo em paz?')


def potencia(numero, expoente):
    valor = numero ** expoente
    return valor


programa_principal()


# resultado = potencia(8)
# print('Resposta: ', resultado)

# nome = input('Digite seu nome: ')
# saudacao(nome)
# saudacao('Natanael')
# valor = saudacao('Maria J.')
# print('Resultado de saudacao: ', valor)
