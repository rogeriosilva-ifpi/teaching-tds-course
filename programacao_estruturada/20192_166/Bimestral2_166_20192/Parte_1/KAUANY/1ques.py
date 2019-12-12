def programa():
    n1 = float(input("Digite sua 1 nota: "))
    n2 = float(input("Digite sua 2 nota: "))
    n3 = float(input("Digite sua 3 nota: "))
    n4 = float(input("Digite sua 4 nota: "))
    media = float(input("Digite sua media: "))
    
    soma = (n1 + n2 + n3 +n4)/ 4
    nota_final = soma
    
    if soma >= media:
        print("Aprova",nota_final) 
            
    else: 
        print("Reprovado",nota_final)


programa()
