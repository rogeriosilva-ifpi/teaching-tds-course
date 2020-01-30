def main():
    qtd_familias = int(input('Quantas familias: '))
    renda_total = 0
    contador_familia_bolsa_social = 0
    contador_pessoas = 0
    contador_fem = 0
    contador_mas = 0

    for i in range(qtd_familias):
        print('>>> Familia', i)
        qtd_pessoas = int(input('Quantas pessoas: '))
        contador_pessoas += qtd_pessoas
        renda_familiar = 0

        for j in range(qtd_pessoas):
            renda = float(input('Renda: '))
            sexo = input('Sexo: ')

            renda_familiar += renda
            if sexo == 'f':
                contador_fem += 1
            else:
                contador_mas += 1

        renda_percapita_familia = renda_familiar / qtd_pessoas
        renda_total += renda_familiar

        # dados da familia
        print(f'Renda da Família {renda_familiar}')
        print(f'Essa família tem {qtd_pessoas} pessoas')
        print(f'Com renda percapita de R$ {renda_percapita_familia}')

        if renda_percapita_familia <= 170:
            print(f'Esta família TEM direito a BOLSA SOCIAL')
            contador_familia_bolsa_social += 1

    # resultados gerais
    perc_fem = (contador_fem / contador_pessoas) * 100
    perc_mas = (contador_mas / contador_pessoas) * 100
    renda_familiar_media = renda_total / qtd_familias

    print('\n\nResultados GERAIS:')
    print(f'Das {qtd_familias} famílias digitadas')
    print(f'{contador_familia_bolsa_social} famílias tem direito ao BOLSA SOCIAL')
    print(f'{perc_fem}%% são do sexo feminino')
    print(f'{perc_mas}%% são do sexo masculino')
    print(f'Renda Familiar média {renda_familiar_media}')


main()
