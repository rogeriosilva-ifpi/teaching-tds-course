
def programa():
    peso = float(input('Digite seu peso:'))
    altura = float(input('Digite sua altura:'))

    peso = peso / altura ** 2
    

    if peso <= 17:
        print("Muito abaixo do peso","seu peso é ",peso)
    elif peso <= 18.49:
        print("Abaixo do peso""seu peso é ",peso)
    elif peso <= 24.99:
        print('Peso normal'"seu peso é ",peso)
    elif peso == 25 <= 29.99:
        print(" Acima do peso""seu peso é ",peso)
    elif peso == 30 <= 34.99:
        print('Obesidade 1'"seu peso é ",peso)
    elif peso == 35 <= 39.99:
        print("Obesidade 2 (severa)""seu peso é",peso)
    else:
        print("Obesidade 3 (Mórbida)")

    


 

    

programa()
