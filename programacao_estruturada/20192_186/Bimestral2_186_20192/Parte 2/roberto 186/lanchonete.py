def programa():
    while True: 
        codigo=int(input('codigo do produto:[1/2/3/4/5] '))
        cachorro_quente=2
        x_salada=4.5
        x_bacon=5
        torrada_simples=2
        refrigerante=1.5
        soma=c=0

        if codigo == 1:
            produto=cachorro_quente                       
        elif codigo == 2:
            produto=x_salada          
        elif codigo == 3:
            produto=x_bacon           
        elif codigo ==4:
            produto=torrada_simples            
        elif codigo ==5:
            produto=refrigerante           
        c+=1
        soma+=produto

        resposta=' '
        while resposta == 12345:
            codigo=int(input('mais produtos?[1/2/3/4/5]'))                          
        if codigo == 0:
            break               
    
    print(soma)
programa()
          
