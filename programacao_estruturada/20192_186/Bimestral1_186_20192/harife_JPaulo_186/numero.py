numero = int(input('Digite um numero: '))
contador_soma = 0
contador_media = 0
contador_tempo = 0


while numero >= 0:
    contador_soma = contador_soma + numero
    contador_media = contador_media + 1
    media = contador_soma / contador_media
    numero = int(input('Digite um novo numero: '))
print('Essa é a soma de todos os numeros',contador_soma)
print('Essa é a media dos numeros',media)