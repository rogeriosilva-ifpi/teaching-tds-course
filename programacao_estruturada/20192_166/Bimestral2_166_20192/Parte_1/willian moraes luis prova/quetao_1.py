def main():
    nota1 = float(input("digite a nota1: "))
    nota2 = float(input('digite a nota2:'))
    nota3 = float(input('digite a nota3:'))
    nota4 = float(input('digite a nota4:'))
    media = float(input('qual a media da sua escola?: '))
    todas_notas = (nota1 + nota2 + nota3 + nota4)
    if todas_notas >= media:
        print('voce esta aprovado')
    else:
        print('voce esta reprovado') 


main()
