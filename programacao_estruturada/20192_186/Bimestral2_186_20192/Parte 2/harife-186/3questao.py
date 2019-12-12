ano_atual = int(input("qual e o ano atual? "))
ano_carro = int(input("qual o ano do seu carro? "))
preco_carro = float(input("qualo preco do seu carro? "))

ipva = preco_carro * 0.25
idade_carro = ano_atual - ano_carro

if idade_carro > 15:
    print("seu carro foi isento do pagamento do IPVA")


elif idade_carro > 5 and idade_carro < 11:
    print("voce recebeu um desconto no IPVA")
    desconto_ipva = ipva * 0.15
    print("esse e o preco a ser pago", desconto_ipva)


elif idade_carro > 11 and idade_carro < 16:
    print("voce recebeu um desconto no IPVA de 20%")
    desconto_ipva = ipva * 0.20
    print("esse e o preco a ser pago",desconto_ipva)

