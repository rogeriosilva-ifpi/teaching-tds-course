number_of_runs = int(input('Oi, tudo bom, quantas corridas você fez por dia? '))

price = 0

for price in number_of_runs:
    
    n = float(input('Escreva um valor da corrida: '))
    price += n

uber = price * 0.75
motorista = price * 0.25

print('O valor total arrecadado é {}, o valor arrecadado pelo aplicadivo é {}, e o valor que voçê arrecadou é {}'.format(price, uber, motorista))