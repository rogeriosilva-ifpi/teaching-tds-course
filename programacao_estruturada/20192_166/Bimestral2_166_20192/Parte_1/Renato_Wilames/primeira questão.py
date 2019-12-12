def main():
    pnota = float(input('digite sua nota:  '))
    snota = float(input('digite sua nota:  '))
    tnota = float(input('digite sua nota:  '))
    qnota = float(input('digite sua nota:  '))
    media = float(input('digite qual e a media de aprovação da sua escola: '))

    nota = (pnota+snota+tnota+qnota)/4
    if nota >= media:
        print('voçê esta aprovado')
    else:
        print('voçê esta reprovado')





main()
