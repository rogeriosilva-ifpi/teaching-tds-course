n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))
n3 = float(input('Digite nota 3: '))
n4 = float(input('Digite nota 4: '))

media = float(input('Digite a média exigida em sua escola: '))

soma = (n1 + n2 + n3 + n4) / 4

nota_final = soma

if soma >= media:
    print('Aprovado', nota_final)
else:
    print('Reprovado', nota_final)