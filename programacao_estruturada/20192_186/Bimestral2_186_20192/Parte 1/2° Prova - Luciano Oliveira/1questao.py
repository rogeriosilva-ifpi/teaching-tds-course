def corrida():
    numero = int(input("Digite quantas corridas voce fez no dia: "))
    soma = 0
    for l in numero:
        corrida = int(input("Digite o valor da corrida:"))
        soma = soma + corrida

    print(soma)
corrida()        
    
