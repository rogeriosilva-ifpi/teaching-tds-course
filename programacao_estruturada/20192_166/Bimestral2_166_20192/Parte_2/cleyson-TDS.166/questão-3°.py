def main():
    partidas  = int(input("digite de partidas: "))
    resultado = 0

    for i in range(partidas):
        resultado = input("digite o resultado: ")

        if resultado == "v":
            resultado += 3
            total = resultado + resultado
            
            print("numero de pontos",total)

        elif resultado == "e":
            resultado += 1
            total = resultado + resultado
            
            print("numero de pontos:",total)



        else:
            pass
       
































main()
