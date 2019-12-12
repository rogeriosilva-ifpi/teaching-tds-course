def senha():
    senha = str(input("Digite uma senha: "))
    tamanho = len(senha)
    a = b = c = 0
    for l in senha:
        if chr(65) <= l <= chr(90):
            a = a + 1
        if  chr(97) <= l <= chr(122):
            b = b + 1
        if "123456789":
            c = c + 1
    if tamanho >= 8 :
        if a >= 1:
            if b >= 1:
                if c >= 1:
                    print("A senha é segura! ")
                else:
                    print("Não é segura!\n Não existe nenhum numeral")    
            else:
                print("Não é segura!\n Não existe nenhuma letra minuscula")       
        else:
            print("Não é segura!\n Não existe nenhuma letra maiuscula")            
    else:
        print("Não é segura!\n O tamanho é menor que 8")
       
            
                
senha()
