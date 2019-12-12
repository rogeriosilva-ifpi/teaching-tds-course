def main():
    partidas  = int(input("digite de partidas: "))
    total = 0
    
    for i in range(partidas):
        resultado = int(input("digite o resultado: "))
        if resultado == "v":
            total = total + 3 
        if resultado == "e":
            total = total + 1
        print(total)


































main()
