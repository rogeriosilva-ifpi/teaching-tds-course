def main():
    nota1 = input('Digite sua primeira nota: ')
    nota2 = input('Digite sua segunda nota: ')
    nota3 = input('Digite sua terceira nota: ')
    nota4 = input('Digite sua quarta nota: ')
    media = input('Digite sua mádia escolar: ')
    total = (nota1 + nota2 + nota3 + nota4)
    media1 = 4 * media

    if total == media1:
        print('Aprovado')
    else:
        print('Reprovado') 


main()
