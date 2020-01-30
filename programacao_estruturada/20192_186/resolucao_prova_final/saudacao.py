def main():
    nome = input('Digite seu nome:')
    hora = int(input('Qual hora do dia(0-23): '))

    if hora >= 6 and hora <= 12:
        saudacao = 'Bom dia'
    elif hora >= 13 and hora <= 18:
        saudacao = 'Boa tarde'
    else:
        saudacao = 'Boa noite'

    print(f'Olá {saudacao} {nome}!')


main()
