def main():
    codigo = float(input('digite o codigo do produto '))
    
    valor = '0'
    
    if codigo == 1:
        valor += '4.00'
    elif codigo == 2:
        valor += '4.50'
    elif codigo == 3:
        valor += '5.00'
    elif codigo == 4:
        valor += '2.00'
    elif codigo == 5:
        valor += '1.50' 
    elif valor == 0:
        print('voçê pagara o valor de ',valor)
    
main()
