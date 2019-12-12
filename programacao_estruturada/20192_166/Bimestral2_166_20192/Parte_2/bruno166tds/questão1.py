def main():
    corridas_motorista = int(input('quantas corridas você fez motorista: '))
    total = 0
    for i in range(corridas_motorista):
        preço_corrida = float(input('informe o preço da corrida: '))
        total = total + preço_corrida
        total_aplicativo = preço_corrida * 0.25
        total_motorista = preço_corrida * 0.75

    print('valor total da corrida:','R$',total)
    print('esse é o total do aplicativo:','R$',total_aplicativo)
    print('essse é o total do motorista:','R$',total_motorista)
        

main()