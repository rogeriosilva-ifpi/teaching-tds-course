def principal():
    custo = float(input('Custo R$: '))

    distribuidor = custo * (28/100)
    imposto = custo * (45/100)

    valor_final = custo + distribuidor + imposto

    print(f'Valor Final R$: {valor_final}')


principal()
