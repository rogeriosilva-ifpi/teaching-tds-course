def main():
    qt = 3
    vertebrado = 'vertebrado'
    ave = 'ave'
    mamifero = 'mamifero'
    carnivoro = 'carnivoro'
    onivoro = 'onivoro'
    aguia = 'aguia'
    pomba = 'pomba'
    herbivoro = 'herbivoro'
    invertebrado = 'invertebrado'
    inseto = 'inseto'
    anelideo = 'anelideo'
    hematofago = 'hematofago'
    aguia = 'aguia'
    homem = 'homem'
    vaca = 'vaca'
    pulga = 'pulga'
    lagarta = 'lagarta'
    sanguesuga = 'sanguesuga'
    minhoca = 'minchoca'
    primeirapalavra = input('digite a primeira palavra :')
    segundapalavra = input('digite a segunda palavra: ')
    terceirapalavra = input('digite a terceira palavra: ')

    if primeirapalavra == vertebrado:
        if segundapalavra == mamifero:
            if terceirapalavra == onivoro:
                print(homem) 
    if primeirapalavra == vertebrado:
        if segundapalavra == mamifero:
            if terceirapalavra == herbivoro:
                print(vaca)
    if primeirapalavra == vertebrado:
        if segundapalavra == ave:
            if terceirapalavra == carnivoro:
                print(aguia)
    if primeirapalavra == vertebrado:
        if segundapalavra == ave:
            if terceirapalavra == onivoro:
                print(pomba)
    if primeirapalavra == invertebrado:
        if segundapalavra == inseto:
            if terceirapalavra == hematofago:
                print(pulga) 
    if primeirapalavra == invertebrado:
        if segundapalavra == inseto:
            if terceirapalavra == herbivoro:
                print(lagarta)
    if primeirapalavra == invertebrado:
        if segundapalavra == anelideo:
            if terceirapalavra == hematofago:
                print(sanguesuga)
    if primeirapalavra == invertebrado:
        if segundapalavra == anelideo:
            if terceirapalavra == onivoro:
                print(minhoca)            

main()    
