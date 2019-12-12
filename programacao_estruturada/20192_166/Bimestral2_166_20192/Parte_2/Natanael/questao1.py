def main():
    corrida = int(input('Quantas corridas você fez? '))
    
    valor_total = 0

    for i in range(corrida):
        valor_corrida = float(input('Digite o  valor da corrida: '))
        valor_total = valor_total + valor_corrida


        
        
    valor_uber =  valor_total * (25/100)
    valor_motorista = valor_total - valor_uber


    print('Valor total é: ',valor_total)
    print('Valor para a Uber é: ',valor_uber)
    print('Valor para o motorista é: ',valor_motorista)





main()

