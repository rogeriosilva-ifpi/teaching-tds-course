def main():
    nome_aluno = input('Nome: ')
    n1 = int(input('primeira nota: '))
    n2 = int(input('segunda nota: '))
    n3 = int(input('terceira nota '))
    n4 = int(input('quarta nota: '))
    m_a = (n1 + n2 + n3 + n4)/4

    if m_a > 7:
        print("Aprovado")

    else:
        print("Reprovado")

main()            
