senha = input("coloque uma senha: ")

def tamanho():
    if len(i) == range(8):
        return True
    else:
        return False

def maiuscula():
    if ord(i) in range(65,90):
        return True
    else:
        return False

def miniscula():
    if ord(i) in range(97, 122):
        return True
    else:
        return False

def numeral():
    if ord(i) in range(48, 57):
        return True
    else:
        return False

for i in senha:
    if tamanho() == True:
        print("tamanho estao ok")
        continue
    else:
        print("tamanho nao estao bom, por favor reinicie o programa e tente novamente")
        
    if maiuscula() == True:
        print("as letras maiusculas estao ok")
        continue
    else:
        print("as letras maiusculas nao estao boas o suficiente, por favor reinicie o programa e tente novamente")
        
    if miniscula() == True:
        print("as letras minusculas estao ok")
        continue
    else:
        print("as letras minusculas nao esta boas o suficiente, por favor reinicie o programa e tente novamente")
        
    if numeral() == True:
        print("os numeros esta bons")
        continue
    else:
        print("os numeros nao estao bons o suficiente, por favor reinicie o programa e tente novamente")

    