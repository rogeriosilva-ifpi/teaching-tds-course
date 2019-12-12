def main():
    média_aprovativa = float(input('digite a média aprovativa da sua escola: '))
    nota1 = float(input('digite sua 1º nota: '))
    nota2 = float(input('digite sua 2º nota: '))
    nota3 = float(input('digite sua 3º nota: '))
    nota4 = float(input('digite sua 4º nota: '))
    soma = nota1 + nota2 + nota3 + nota4
    quantidade_notas = 4
    média_notas = soma / quantidade_notas
    if média_notas >= média_aprovativa:
        print('APROVADO')
    else:
        print('REPROVADO')

main()