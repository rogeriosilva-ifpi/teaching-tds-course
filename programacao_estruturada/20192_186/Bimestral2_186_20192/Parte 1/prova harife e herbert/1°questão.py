corridas = int(input('quantas corridas? '))
contador = 0
valor_total = 0
while contador < corridas:
    contador = contador + 1
    valor_por_corrida = float(input('valor por corrida:'))
    valor_total = valor_por_corrida + valor_total

total_do_motorista = valor_total * 0.75
total_do_app = valor_total * 0.25

print('esse é o valor que o motorista vai receber', total_do_motorista,'e esse é o valor que o aplicativo vai receber', total_do_app)


#apenas conseguir usar o while nessa questao
