numero = int(input("Digite um número positivo, digite negativo para terminar: "))
soma = 0
quantidade_de_numeros = 0

while(numero >= 0):
    soma = soma + numero
    quantidade_de_numeros = quantidade_de_numeros + 1

    numero = int(input("Digite um número positivo, digite negativo para terminar: "))

media = soma / quantidade_de_numeros

print(soma)
print(media)