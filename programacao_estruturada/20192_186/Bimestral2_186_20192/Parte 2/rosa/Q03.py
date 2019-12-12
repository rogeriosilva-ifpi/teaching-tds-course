
a = int(input('qual valor do veiculo: '))
b = int(input('qual a idade do veiculo: '))

calculo = (2.5 // 100)*a 
print ('seu imposto a pagar é: ', calculo)

 
z = (15 // 100)*b
y = (20 // 100)*b  



def desconto_total ():
    if b <= 5:
        print('não tem desconto - que pena')
    if 5 < b > 10:
        print('seu desconto é: ', z)
    if 10 < b > 15:
        print('seu desconto é: ', y)
    else:
        print('nem imposto paga')

desconto_total()
