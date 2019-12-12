mt=int(input("quantas coridas vc fez hoje? "))


for i in range(mt):
    v = int(input("valor da corrida?"))
    contador = v + v
valor_uber = contador * (25/100)
valor_motorista = contador * (75/100)

print("valor do uber e: ",valor_uber)  
print("valor do motirista e: ",valor_motorista)

