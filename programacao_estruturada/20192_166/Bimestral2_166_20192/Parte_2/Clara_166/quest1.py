corridas = int(input('Digite a quantidade de corridas realizadas: '))


v_total = 0
for i in range(corridas):
  valor = float(input('Digite o valor da corrida: '))
  v_total = valor + valor


motorista = v_total * (75/100)
uber = v_total * (25/100)
print('Valor total:', v_total) 
print('Porcentagem do motorista:', motorista)
print('Porcentagem do uber:', uber)

