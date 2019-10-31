def programa():
    quantidade = int(input("Quantos numeros quer digitar: "))
    contador = 0
    contador_p = 0
    contador_i = 0
    contador_primo = 0

    while quantidade != contador :
        numero = int(input("Digite um numero: "))
        contador = contador + 1
        
        if numero % 2 == 0:
            contador_p = contador_p + 1
            
        elif numero % 2 != 0:           
            contador_i = contador_i + 1
            
        elif numero % numero == 0 and numero % 1 == 0:    
            
            contador_primo = contador_primo + 1
            
    print("Quantidade pares, " , contador_p)
    print("Contador impar, ", contador_i)
    print("Contador primo, " , contador_primo)

programa()
