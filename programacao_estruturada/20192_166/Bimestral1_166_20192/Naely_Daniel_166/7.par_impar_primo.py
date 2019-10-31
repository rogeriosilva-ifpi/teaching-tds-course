#Calulcar pares, impares e primos
print('')
quantidade = int(input('Quantidade de números: '))
c = 0

def e_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def primo(n):
    if (n % 2 == 0) and not(n == 2):
        pass
    elif(n % 3 == 0) and not(n == 3):
        pass
    else:
        return True

quant_pares = 0
quant_impares = 0
quant_primos = 0

while c < quantidade:
    n = int(input('Digite um número: '))
    if not(e_par(n)) and primo(n):
        quant_primos = quant_primos + 1
    elif e_par(n) and primo(n):
        quant_primos = quant_primos + 1
    if e_par(n):
        quant_pares = quant_pares + 1
    elif not(e_par(n)):
        quant_impares = quant_impares + 1
    elif primo(n):
        quant_primos = quant_primos + 1
    

    c = c + 1
print('')

print('-------Valores--------')
print(f'{quant_pares} são pares.')
print(f'{quant_impares} são impares.')
print(f'{quant_primos} são primos.')