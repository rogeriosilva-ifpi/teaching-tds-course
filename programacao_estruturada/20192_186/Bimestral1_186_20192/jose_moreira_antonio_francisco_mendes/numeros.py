def programa():
    numero = int(input("Digite um numero: "))
    contador = 0        
    soma = 0

    while numero > 0:
        numero = int(input("Digite um numero: "))
        soma = soma + numero
        contador = contador + 1

    print("Soma dos numeros, " ,soma )
    
    print("contador", contador)
    
    print("Media sera ", soma/contador)

programa()
        
