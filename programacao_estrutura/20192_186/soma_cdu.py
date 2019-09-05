# entrada
numero = int(input('Numero: '))

# processamento
centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = (numero % 100) % 10

somatorio = centenas + dezenas + unidades
inverso = unidades*100 + dezenas*10 + centenas

# saida
print('C:', centenas)
print('D:', dezenas)
print('U:', unidades)
print('Soma:', somatorio)
print('Inverso:', inverso)
