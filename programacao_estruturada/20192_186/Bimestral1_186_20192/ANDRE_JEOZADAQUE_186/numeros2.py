'Quantos numeros irá digitar?'
numero = int(input('Digite o número:'))
quantidade_pares=0
quantidade_impar=0
quantidade_primos=0
while numero <= quantidade:
    numero = int(input('Digite o número'))
    if numero % 2 == 0:
        quantidade_pares = quantidade_pares + 1
    else:
        quantidade_impar = quantidade_impar + 1
    
    if numero % numero == 0 and numero % 1 == 0:
        quantidade_primos = quantidade_primos + 1
    
    
    