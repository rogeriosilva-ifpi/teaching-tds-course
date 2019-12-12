def programa():
    print('Olá, vamos verificar se vc foi APROVADO OU REPROVADO!!!')
    print('PRIMEIRO, DIGA-ME QUAL A MÉDIA EXIGIDA NA SUA ESCOLA:')
    m=  float(input('média escola:'))
    n1= float(input('digite sua primeira:'))
    n2= float(input('digite sua segunda:'))
    n3= float(input('digite sua terceira nota:'))
    n4= float (input('digite sua quarta nota:'))
    soma= n1+n2+n3+n4
    media= soma/4
    if media >= m:
        print("PARABÉNS, VC FOI APROVADO",media)
    else:
        print("SINTO MUITO VC FOI REPROVADO", media)
programa()
