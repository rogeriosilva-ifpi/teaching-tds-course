n1=int(input("nota?"))
n2=int(input("nota?"))
n3=int(input("nota?"))
n4=int(input("nota?"))
media=int(input("media? "))


m_aluno=(n1+n2+n3+n4)/4

if media and m_aluno >= 7:
    print('aprovado')
else:
    print('reprovado')