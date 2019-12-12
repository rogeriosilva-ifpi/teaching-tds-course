def futebol():
    numero = int(input("Digite quantas partidas: "))
    a =1
    v=e= 0
    while a <= numero:
        resultado = input("Resultado v ou e : ")
        if resultado == "v":
            v=v+3
        elif resultado == "e":
            e =e +1
        
        a=a+1
    soma = e + v 
    print("O time acumulhou",soma,"pontos ao longo do campeonato")

futebol()
        
