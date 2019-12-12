def main():
    numero_corrida = int(input('Digite a quantidade: '))
    total = 0

    for i in range(numero_corrida):
        preço_corrida = float(input('Digite o valor: '))
        total = total + preço_corrida
        print('Preço final: ' , total)
        taxa_motorista = total/100
        uber = taxa_motorista*25
        motorista = taxa_motorista*75
        print('Valor do Uber: ' , uber)
        print('Valor do Motorista: ' , motorista)







main()
