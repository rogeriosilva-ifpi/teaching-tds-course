frase = input('escreva uma frase: ')
vogais = 'aeiouáãâéíõôóúü'
nova_frase = ' '

for i in frase:
    if ord(i) in range(48,58):
        i = '@'
    elif ord(i) not in range(65,91) and ord(i) not in range(97,123):
        i = ' '
    nova_frase = nova_frase + i

print(nova_frase)

#nao conseguir tranformar a vogal para maiuscula

