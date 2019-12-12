def organizar():
    registro = int(input("Digite quantos registores de amostras voce quer : "))
    a = 1
    soma =r=s=c= 0
    while a <= registro:
                   amostra = input("Digite sua amostra: ").lower()
                   print(amostra)
                   a = a + 1
                   numero = int(amostra[0])
                   if "r" in amostra:
                       r = r + numero
                   if "c" in amostra:
                       c = c + numero
                   if "s" in amostra:
                       s = s + numero
                   soma = soma + numero
    pc = (c/soma) *100
    ps = (s/soma)*100
    pr = (r/soma)*100
    print("Total Geral de animais eh: ",soma)
    print("Ratos:",r)
    print("Sapos:",s)
    print("Coelhos:",c)
    print("Percentual de Coelhos",pc,"%")
    print("Percentual de Sapos",ps,"%")
    print("Percentual de Ratos",pr,"%")

organizar()
