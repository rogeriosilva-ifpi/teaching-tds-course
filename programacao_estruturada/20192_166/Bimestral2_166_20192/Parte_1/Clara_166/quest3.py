

valor = float(input('Digite o vcalor do seu veículo: '))
fabric = float(input('Digite ano do seu veículo: '))


idade = 2020 - fabric
ipva = valor * (2.5/100)


if idade >= 5 and idade <= 10):
    print('desconto de 15%)'
elif idade >= 11 and <= 15:
    print('desconto de 20%')
elif idade > 15:
    print('isento')
    
