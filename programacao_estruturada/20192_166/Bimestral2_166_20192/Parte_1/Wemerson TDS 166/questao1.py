n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))

soma = (n1 + n2 + n3 + n4) / 4

print('Media: ', soma)

if soma >= 7:
    print('APROVADO')
else:
    print('REPROVADO')