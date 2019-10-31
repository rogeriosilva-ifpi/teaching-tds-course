
q = int(input('Quantos numero quer digitar?' ))

c = 0
while c < q:
    numero = int(input('digite um numero : '))
    if numero % 2 == 0:
        print('é par' , numero)
    else:
        print('é impar' , numero)

    c = c + 1
        
