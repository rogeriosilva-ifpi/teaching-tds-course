def mudar():
    frase = input("Digite uma frase: ")
    nova_frase = " "
    for l in frase:
        if l chr(65) <= l <= chr(90) or  chr(97) <= l <= chr(122) or l in "123456789":
            if l in "123456789":
                l="@"
            if l in "aeiou":
                l=l.upper()
        nova_frase = nova_frase + l
   print(nova_frase)
mudar()
