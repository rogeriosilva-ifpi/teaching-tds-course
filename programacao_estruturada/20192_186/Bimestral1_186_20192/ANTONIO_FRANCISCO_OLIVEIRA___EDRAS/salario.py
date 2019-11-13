def progama():
    professor = input('Digite o nome do professor:')
    regime = int(input('Digite o regime de trabalho:'))
    qualificacao = input('Digite sua qualificação: ')
    print('Professor', professor, 'com salario de: ',
          salario(professor, regime, qualificacao))


def salario(professor, regime, qualificacao):
    if (regime == 20):
        salabrut = 2500
    elif(regime == 40):
        salabrut = 4500

    if (qualificacao == 'E') or (qualificacao == 'e'):
        salabrut = salabrut + (salabrut * 0.3)
    elif(qualificacao == 'M')or (qualificacao == 'm'):
        salabrut = salabrut + (salabrut * 0.52)
    elif(qualificacao == 'D') or (qualificacao == 'd'):
        salabrut = salabrut + (salabrut * 0.7)

    salario = salabrut - (salabrut * 0.385)
    return salario


progama()
