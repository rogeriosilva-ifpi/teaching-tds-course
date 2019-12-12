def programa():
    frase = str(input('Digite uma frase: '))
    for i in range(len(frase) - 1):
        caractere = frase[i]
        if caractere == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
