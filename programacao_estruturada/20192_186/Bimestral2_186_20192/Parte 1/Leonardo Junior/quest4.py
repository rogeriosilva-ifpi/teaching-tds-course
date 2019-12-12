def vertebrado():
    print('Escolha 3 palavras; vertebrado, ave, mamifero, carnivoro, onivoro,herbivoro')
    ave_1 = aguia
    ave_2 = pomba
    mamifero_1 = homem
    mamifero_2 = vaca
    if vertebrado + ave + carnivoro:
        return ave_1
    else:
        return ave_2
    if vertebrado + mamifero + onivoro:
        return mamifero_1
    else:
        return mamifero_2

vertebrado()

def invertebrado():
    print('Escolha 3 palavras; invertebrado, inseto, anelideo, hematofago, herbivoro, onivoro')
    inseto_1 = pulga
    inseto_2 = lagarta
    anelideo_1 = sanguessuga
    anelideo_2 = minhoca
    if invertebrado + inseto + hematofago:
        return inseto_1
    else:
        return inseto_2
    if invertebrado + anelideo + hematofago:
        return anelideo_1
    else:
        return anelideo_2

invertebrado()