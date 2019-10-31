#sexta QUESTÃO
numero = int(input('digite um numero'))

contador = 1
soma = 0
while numero > 0:
    numero = int(input('digite outro numero'))
    
    contador = contador + 1
    
    soma = soma + numero

media = soma / contador
print (soma, media)