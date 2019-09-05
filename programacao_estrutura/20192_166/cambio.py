# entrada
cotacao_dollar = float(input('** Cotação Dollar: '))
valor_real = float(input('** Valor em R$: '))

# processamento
valor_dollar = valor_real / cotacao_dollar

# saida
print('Conversão: R$', valor_real, 'é igual a US$', valor_dollar)
