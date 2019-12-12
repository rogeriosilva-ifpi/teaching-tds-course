def animal():
    nome1 = input("É vertebrado ou invertebrado? ").lower()
    nome2 = input("É ave, mamifero, inseto ou anelideo? ").lower()
    nome3 = input("É carnivoro, onivoro,herbivoro ou hematofago? ").lower()
    if nome1 == "vertebrado":
        if nome2 == "ave":
            if nome3 == "carnivoro":
                print("Aguia")
            if nome3 == "onivoro":
                print("Pomba")
        if nome2 == "mamifero":
            if nome3 == "onivoro":
                print("Homem")
            if nome3 == "herbivoro":
                print("Vaca")
                
    if nome1 == "invertebrado":
        if nome2 == "inseto":
            if nome3 == "hematofago":
                print("Pulga")
            if nome3 == "herbivoro":
                print("Lagarta")
        if nome2 == "anelideo":
            if nome3 == "hematofago":
                print("Sanguessuga")
            if nome3 == "onivoro":
                print("Minhoca")
animal()








#def nome():
    #nome1 = input("É vertebrado ou invertebrado? ")
    #nome2 = input("É ave, mamifero, inseto ou anelideo? ")
    #nome3 = input("É carnívoro, onivoro,herbivoro ou hematofago? ")
    #return true
