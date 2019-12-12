def main():
    valor_veiculo = float(input('Digite o valor: '))
    ano_fabricaçao = int(input('Digite o ano: '))

    anos = 2020 - ano_fabricaçao

    if anos >= 5 and anos < 18:
        desconto = (2.5 - (15/100))
        valor_total = valor_veiculo - desconto

        print('Desconto' , desconto)
        print('Valor Total' , valor_total)

    elif anos > 15:
        print('Isento de Taxa')
        print('Voce vai pagar' , valor_veiculo)

    else:
        valor_Total = valor_veiculo - (valor_veiculo - (2.5/100))
        print('Valor_Total' , valor_total)


main()
