def teste(numero):
    if numero == 2:
        return "par_primo"
    elif numero == 3 or numero == 5:
        return "primo"
    elif (numero % 2 != 0) and (numero % 3 != 0) and (numero % 5 != 0):
        return "primo"
    elif numero % 2 == 0:
        return "par"
    else:
        return "impar"


quantidade = int(input("Digite a quantidade de numeros: "))
contador = 0
par = 0
impar = 0
primo = 0

while(contador < quantidade):
    numero = int(input("Digite numero: "))
    tipo_numero = teste(numero)

    if tipo_numero == "primo":
        primo += 1
        impar += 1
    elif tipo_numero == "par":
        par += 1
    elif tipo_numero == "par_primo":
        par += 1
        primo += 1
    elif tipo_numero == "impar":
        impar += 1

    contador += 1

print("Quantidade de números primos: %d" % primo)
print("Quantidade de números pares: %d" % par)
print("Quantidade de números impares: %d" % impar)
