# entrada
numero = int(input('Número: '))

# processamento
c = numero // 100
resto = numero % 100
d = resto // 10
u = resto % 10

soma = c + d + u

# saida
print('Somatório:', soma)
