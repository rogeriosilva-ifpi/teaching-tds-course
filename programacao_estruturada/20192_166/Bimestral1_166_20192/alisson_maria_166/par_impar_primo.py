def programa():
    n = int(input('quantos numeros quer digitar\n>>> '))
    numero = 0
    par = 0
    impar = 0
    primo = 0
    while n > 0:
        numero = int(input('digite um numero\n>>> '))
        if numero % 2 ==0:
            par += 1
        else:
            impar += 1
        if e_primo(numero) == True:
            primo += 1
        n -= 1
    print(f'tantos de numeros pares {par}, tantos de numeros impares {impar}, tantos de numeros primos {primo}')

def e_primo(numero):
    contador = 0
    inicio = 0
    while inicio <= numero:
        if inicio % numero == 0:
            contador += 1
        inicio += 1
    if contador == 2:
        return True
    else:
        return False

programa()