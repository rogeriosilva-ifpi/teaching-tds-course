# Entrada
minutos = int(input('Digite os minutos: '))

# Processamento
horas = minutos // 60
min = minutos % 60

# Saida
# print('4h32min' )
print('%dh%dmin' % (horas, min))
