def main():
    valor_do_veiculo = float(input('Digite o valor do seu veiculo: '))
    ano_do_veiculo = int(input('Informa o ano de fabricação do veiculo: '))
    ipva = valor_do_veiculo + (2.5*100)
    ano_de_pagamento = int(2020)
    desconto = ano_do_veiculo - ano_do_veiculo
    desconto2 = valor_do_veiculo - (15*100)
    if ano_do_veiculo > desconto:
        print('Você está isento!')
    if ano_do_veiculo <= desconto2:
        print('Seu desconto é: ', desconto2)

main()