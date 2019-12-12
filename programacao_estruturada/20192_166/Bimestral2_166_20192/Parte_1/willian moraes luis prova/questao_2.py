def main():
    senha = input('digite')
    if senha in tamanho():
        return true
    elif senha in maiusculo():
        return true
    elif senha in minusculo():
        return true
    elif senha in numeral():
        return true
    






def tamanho(t):
    return len(t)

    
def maiuscula(w):
    return 'A' <=W<='Z'


def minuscula(d):
    return 'a' <=d<= 'z'


def numeral(n):
    return n in '0123456789'
    








main()
