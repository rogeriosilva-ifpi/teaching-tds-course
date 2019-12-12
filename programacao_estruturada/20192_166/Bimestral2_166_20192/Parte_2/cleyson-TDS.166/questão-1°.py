def main():
    corridas  = int(input("digite a quantidade de voltas: "))
    total = 0
    
    for i in range(corridas):
        preço = float(input("digite o valor da corrida: "))
        total = total + preço
        print("preço total:",total)
        por = total/100
        uber = por*25
        motorista = por*75
        print("dinheiro para da uber:",uber)
        print("dinheiro do motorista:",motorista)
        
        
        
        








main()
