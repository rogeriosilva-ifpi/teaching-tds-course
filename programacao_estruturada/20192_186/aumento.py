# As Organizações Tabajara resolveram dar um aumento
# de salário aos seus colaboradores e lhe contrataram
# para desenvolver o programa que calculará os reajustes.
# Escreva um algoritmo que leia o salário de um colaborador
#  e reajuste-o segundo o seguinte critério,
# baseado no salário atual:
# o salários até R$ 280,00 (incluindo) : aumento de 20%
# o salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# o salários de R$ 1500,00 em diante : aumento de 5%


def programa():
    salario = float(input('Salário: '))

    aumento = calcular_aumento(salario)
    novo_salario = salario + aumento

    print('Se novo salário R$ ', novo_salario)


def calcular_aumento(s):
    if s <= 280:
        return s * (20/100)
    elif s <= 700:
        return s * (15/100)
    elif s <= 1500:
        return s * (10/100)
    else:
        return s * (5/100)


programa()
