# Média de números com while.
# Obs não consegui somar os valores a cada volta para calcular a média.


n = int(input('Digite um número: '))
c = 1

while n >= 0:
    n2 = int(input('Digite um número: '))
    if not(n < 0):
        soma = n + n2
        proximo = soma + n2
    #incremento de contador 
    c = c + 1

    

media = soma / (c - 1)
print(media)