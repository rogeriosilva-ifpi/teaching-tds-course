senha = (input("Digite sua senha aqui: "))

for i in range(senha):
    if len(senha) >= 8:
        if senha == '1234567890':
            if senha == ord(senha.upper):
                if senha == ord(senha.lower):
                    print("Sua senha é segura!!!")
                else:
                    print("sua senha é fraca, pois não possui letras minúsculas!")
            else:
                print("sua senha é fraca, pois não possui letras maiúsculas!")
        else:
            print("sua senha é fraca, pois não possui nenhum número!")
    else:
        print("sua senha é fraca, pois possiu menos de oito dígitos")        