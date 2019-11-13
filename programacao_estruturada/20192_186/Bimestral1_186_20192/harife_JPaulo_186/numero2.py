qtd_de_numeros = int(input('Quantos numero vc quer digitar?: \n >>> '))
contador_tempo = 0
contador_par = 0
contador_impar = 0

while contador_tempo < qtd_de_numeros:
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        contador_par = contador_par + 1
    elif numero % 2 == 1:
        contador_impar = contador_impar + 1

    contador_tempo = contador_tempo + 1

print(contador_par)
print(contador_impar)
