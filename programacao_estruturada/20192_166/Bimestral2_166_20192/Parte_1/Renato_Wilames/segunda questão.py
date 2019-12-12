def main():
    senha = input('digite sua senha: ')
    cara = 8
    maiu = 1
    minu = 1
    nume = 1
    quanti = len(senha)
    lma = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
    lmi = 'abcdefghijklmnopqrstuvxwyz'
    if quanti >= 8:
        print('sua senha é segura')
    elif quanti < 8:
        print('sua senha não é segura, faltou a quantidade de caracteres maior que oito(8)')
    elif senha == lma:
        print('sua senha é segura')
    
    
    
main()    