Chave_de_segurança =  str(input('Informe sua senha: '))

def tamanho(string):
    if len(string) >= 8:
        return True
    else:
        return False

def maiusculas(string):
    maiusculas = ['A', 'B',','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',T','U','V','X','Y','Z']
    for i in senha:
        if i in maiusculas:
            return True
        else:
            return false

def numerais(string):
    numerais = ['0','1','2','3','4','5','6','7','8','9']
    for i in senha:
        if i in numerais:
            return True
        else:
            return False
if tamanho(senha) and maiusculas(senha) and numerais(senha):
        print('Chave segura!')
elif tamanho(senha) == False:
        print('Chave deve conter no minimo 8 caracteres.')
elif tamanho(senha) == False:
        print('Chave deve conter no minimo caractere maiusculo.')
elif tamanho(senha) == False:
        print('Chave deve conter no minimo um numero.')

programa()
        
