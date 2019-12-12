def main():
    preco_carro = int(input('digite o valor do carro:'))
    ano = int(input('digite o ano do carro:'))
    if ano >= 15:
        print(preco_carro)
    elif ano > 5 and ano < 10:
        soma = preco_carro - (preco_carro * 0.15)
        print(soma)
        desconto = preco_carro - soma
        print('seu desconto foi de 'desconto)
    elif ano > 11 and ano < 20:
        v = preco_carro - (preco_carro * 0.20)
        print(v)
        desconto = preco_carro - v
        print('seu desconto foi de',desconto)


main()