corrida = int(input("Digit o numero da corrida"))
total = int(0)
app = float(0)
moto = float(0)
for i in range(corrida):
    valordacorr = int(input("Digite o valo da corrida"))
    total = total + valordacorr
    
    app = app + (0.25 * valordacorr)
    moto = moto + (0.75 * valordacorr)
    
print('Valor total é: ',total)
print('Valor final do motorista é ',moto)
print('Valor final do aplicativo é ',app)