numero1 = int(input('Digite um numero'))
numero2 = int(input('Digite um numero'))
numero3 = int(input('Digite um numero'))
numero4 = int(input('Digite um numero'))
contadorpar = 0
contadorimpar = 0
contador = 0
if (numero1 % 2) == 0:
    contadorpar += 1

else:
    contadorimpar += 1

if (numero2 % 2) == 0:
    contadorpar += 1

else:
    contadorimpar += 1

if (numero3 % 2) == 0:
    contadorpar += 1

else:
    contadorimpar += 1

if (numero4 % 2) == 0:
    contadorpar += 1

else:
    contadorimpar += 1


print('numeros pares = ', contadorpar, 'numeros ímpares', contadorimpar)
