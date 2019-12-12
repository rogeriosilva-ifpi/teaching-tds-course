def verificar_senha():
    senha = input('digite sua senha: ')
    tamanho_senha = len(senha)
    if tamanho_senha == 8:
        return True 
    elif letra_maiscula in senha:
        return True
    elif letra_minúscula in senha:
        return True
    else:
        print('Sua senha está ok')

def letra_maiscula(c):
    if 'A' >= c <= 'Z':
        return True
    else:
        return False



def letra_minuscula(c):
    if 'a' >= c <= 'z':
        return True
    else:
        return False


verificar_senha()