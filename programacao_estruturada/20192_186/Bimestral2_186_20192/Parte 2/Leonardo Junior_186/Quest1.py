def main():
    nota1 = float(input('Digite a nota: '))
    nota2 = float(input('Digite a nota: '))
    nota3 = float(input('Digite a nota: '))
    nota4 = float(input('Digite a nota: '))
    media_escola = float(input('Qual a media da sua escola? '))
    media_aprovativa = media_escola
    media1 = nota1 + nota2
    media2 = nota3 + nota4

    media_final = (media1 + media2) // 4

    if media_final >= media_aprovativa:
        print('APROVADO')
    else:
        print('REPROVADO')

main()
 