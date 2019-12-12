def principal():
    n = int(input('quantos numeros voce vai digitar?'))
    pares = 0
    impares = 0


    for i in range(n):
        numero = int(input('numero: '))
        if numero % 2 == 0:
            pares = pares + 1
        else:
           impares = impares + 1
    
    print('Pares:', pares)
    print('Impares:', impares)


principal()

