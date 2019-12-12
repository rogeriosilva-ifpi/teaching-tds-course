N1=float(input('digite primeira NOTA: '))
N2=float(input('digite segunda NOTA: '))
N3=float(input('digite terceira NOTA: '))
N4=float(input('digite quarta NOTA: '))
media=(N1+N2+N3+N4)/4
print('a sua media e: ', media)

if media>=7:
    print('voce esta APROVADO!!')
elif media <7:
    print('voce foi REPROVADO')
