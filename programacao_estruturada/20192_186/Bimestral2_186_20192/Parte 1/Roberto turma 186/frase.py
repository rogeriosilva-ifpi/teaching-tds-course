def programa():
    frase=str(input('frase: '))
    n_frase=' '
    for l in frase:
        if eh_numero(frase):
            n_frase+='@'
        elif eh_vogal(frase):
            n_frase+=chr(ord(l)-32)
    print(n_frase)

def eh_numero(frase):
    if 'l' in '1234567890':
        return True
def eh_vogal(frase):
    if 'l' in 'AaEeIiOoUu':
        return True

programa()
