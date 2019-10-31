peso = float(input('coloque seu peso: '))
altura = float(input('coloque sua altura: '))


def imc():
    imc = peso / (altura ** 2)
    if imc < 17 :
        print('O imc é ', imc)
        print('Muito abaixo do peso')
    elif imc <= 18.49 :
        print('O imc é ', imc)
        print('Abaixo do peso')
    elif imc <= 24.99 :
        print('O imc é ', imc) 
        print('Peso normal')   
    elif imc <= 29.99 :
        print('O imc é ', imc)  
        print('Acima do peso')     
    elif imc <= 34.99 :
        print('O imc é ', imc)
        print('Obesidade 1')    
    elif imc <= 39.99 :
        print('O imc é ', imc)
        print('Obesidade 2')    
    elif imc >= 40 :
        print('O imc é ', imc)
        print('Obesidade 3')
        
    
    

imc()

