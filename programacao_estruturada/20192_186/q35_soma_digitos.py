numero = int(input('Hey cara! Qual é o número? '))

m = numero // 1000
resto = numero % 1000

c = resto // 100
resto = resto % 100

d = resto // 10
u = resto % 10

soma = m + c + d + u

print('A Milhar é', m)
print('A Centena é', c)
print('A Dezena é', d)
print('A Unidade é', u)
print('A soma do dígitos é: ', soma)
