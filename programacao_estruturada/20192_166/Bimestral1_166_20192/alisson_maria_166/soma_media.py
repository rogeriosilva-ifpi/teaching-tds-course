def programa():
    n = 0
    soma = 0
    contador = 0
    while n >= 0:
        n = int(input('insira quantos valores você quiser ^~^\n>>> '))
        if n >= 0:
            soma = soma + n
            contador += 1
    media = soma / contador
    print(f'tantos numeros {n},a soma referente aos numeros que você digitou é {soma}, e a media dessa soma é {media}')

programa()