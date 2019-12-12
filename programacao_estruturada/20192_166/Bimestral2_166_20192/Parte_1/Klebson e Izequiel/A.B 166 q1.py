n0 = int(input('Nota: '))
n1 = int(input('Nota: '))
n2 = int(input('Nota: '))
n3 = int(input('Nota: '))
media = int(input('Media: '))

soma = (n0 + n1)/2 + (n2 + n3)/2

if media >= 7:
    return  'aprovado'
else:
    return 'reprovado'

