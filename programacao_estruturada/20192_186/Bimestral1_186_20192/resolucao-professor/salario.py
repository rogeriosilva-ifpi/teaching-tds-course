def principal():
    print('Digite sua CH semanal')
    ch = int(input('20 ou 40: '))
    qualificacao = input('E - Especialista, M - Mestre ou D - Doutor')

    # define o salario fixo
    if ch == 20:
        salario_fixo = 2500
    elif ch == 40:
        salario_fixo = 4500

    # o adicional de qualificacao
    if qualificacao == 'E':
        adicional = salario_fixo * (30/100)
    elif qualificacao == 'M':
        adicional = salario_fixo * (52/100)
    elif qualificacao == 'D':
        adicional = salario_fixo * (70/100)

    # computando o salario final
    salario_bruto = salario_fixo + adicional

    # descontos
    previdencia = salario_bruto * (11/100)
    ir = salario_bruto * (27.5/100)
    descontos = previdencia + ir

    # salario liquido
    salario_liquido = salario_bruto - descontos

    # Saída
    print(f'Salário Bruto R$ {salario_bruto}')
    print(f'Previdência: R$ {previdencia}')
    print(f'Imposto Renda: R$ {ir}')
    print(f'Salário Líquido R$ {salario_liquido}')


principal()
