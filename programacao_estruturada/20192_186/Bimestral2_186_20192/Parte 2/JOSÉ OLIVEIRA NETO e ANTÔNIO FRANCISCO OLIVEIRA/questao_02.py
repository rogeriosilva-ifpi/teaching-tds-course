senha = str(input('Digite uma senha: '))

def tamanho(string):
    if len(string) >= 8:
        return True
    else:
        return False
            
def maiusculas(string):
    maisculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in senha:
        if i in maisculas:
            return True
        else:
            return False
                
def numerais(string):
    numerais = ['0','1','2','3','4','5','6','7','8','9']
    for i in senha:
        if i in numerais:
            return True
        else:
            return False

if tamanho(senha) and maiusculas(senha) and numerais(senha):
    print('Senha segura!')
elif tamanho(senha) == False:
    print('Senha deve conter no mínimo 8 caracteres.')
elif maiusculas(senha) == False:
    print('Senha deve conter no mínimo um caracter maiúsculo.')
elif numerais(senha) == False:
    print('Senha deve conter no mínimo um número.')
