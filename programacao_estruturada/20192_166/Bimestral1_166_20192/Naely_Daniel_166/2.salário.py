# Cálcular salário de Professor na Universidade

nome = input('Digite seu nome: ')
regime = int(input('Regime de Trabalho (20 ou 40 hrs): '))
qualificacao = input('Qualificação (E, M, D): ')

# Salário Bruto


def ch(regime):
    if regime == 20:
        valor = 2500
        return valor
    else:
        valor = 4500
        return valor


salario = ch(regime)

if qualificacao == 'E':
    salario = salario * 1.30
elif qualificacao == 'M':
    salario = salario * 1.52
else:
    salario = salario * 1.70

# Descontos
previdencia = salario * 0.11
IR = salario * 0.275
salario_liquido = salario - (previdencia + IR)

# Saída
print('')
print(f'Nome: {nome}')
print(f'Salário Bruto: {salario}')
print('')

print('    ----Descontos----    ')
print(f'Previdência -{previdencia}')
print(f'Imposto de Renda -{IR}')
print(f'Salário Liquido = {salario_liquido}')
