def main():
    ano_carro = int(input('Digite o ano do veiculo: '))
    valor = int(input('Digite o valor do carro R$: '))
    
    ipva = ano_carro - 2020
    valor_ipva: 

    if ipva < 5:
        ipva * (2/100)
    elif ipva >= 15:
        ipva = isento

    print('O desconto em R$: ',ipva)

main()