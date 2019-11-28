def main():
    data = input('Digite uma data: ')
    partes = data.split('/')
    dia = partes[0]
    mes = int(partes[1])
    ano = partes[2]

    mes_por_extenso = obter_nome_mes(mes)

    nova_data = dia + ' de ' + mes_por_extenso + ' de ' + ano
    print(nova_data)


def obter_nome_mes(numero):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    mes = meses[numero-1]
    return mes


main()
