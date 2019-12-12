def main():
    senha = input("Digite a senha:")
    tamanho_senha = len(senha)
    

    for c in senha:
        if senha >= 8:
           

def he_maiuscula(c):
    for ord(c) in  range(32, 91):
        print(c, chr(c))

def he_minuscula(c):
    for ord(c) in range(92, 123):
        print(c, chr(c))

    print("SEGURA.")
    print("")
