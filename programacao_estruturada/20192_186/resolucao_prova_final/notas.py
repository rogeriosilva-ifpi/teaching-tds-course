def main():
    qtd_aprovativas = 0
    qtd_reprovativas = 0
    somatorio = 0
    qtd = 0
    nota = float(input('Nota >>> '))

    maior_nota = nota
    menor_nota = nota

    while nota >= 0:
        # trabalho
        somatorio += nota
        qtd += 1

        if nota >= 7:
            qtd_aprovativas += 1
        else:
            qtd_reprovativas += 1

        if nota > maior_nota:
            maior_nota = nota

        if nota < menor_nota:
            menor_nota = nota

        nota = float(input('Nota >>> '))

    # apresentar os resultados
    media = somatorio / qtd

    print(f'Voce digitou {qtd} notas')
    print(f'A média das notas é {media}')
    print(f'A maior nota é {maior_nota}')
    print(f'A menor nota é {menor_nota}')
    print(f'Qtd de notas aprovativas: {qtd_aprovativas}')
    print(f'Qtd de notas reprovativas: {qtd_reprovativas}')


main()
