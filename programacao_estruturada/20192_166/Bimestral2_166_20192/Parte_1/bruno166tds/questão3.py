def main():
    valor_atual_veiculo = input('digite o valor atual do veículo: ')
    ano_fabricação = int(input('quantos anos de fabricão seu carro tem?: '))
    ipva = valor_atual_veiculo * 25/10
    if ano_fabricação > 15:
        ipva = 0
        print(ipva)
    if ano_fabricação >= 5 and ano_fabricação <= 10:
        novo_ipva = ipva - ipva * 0.15
        print(novo_ipva) 

main()