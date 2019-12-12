def programa():
  corridas = int(input("Quantas corridas você fez no dia?  "))
  valor_total =0
 

  for c in range(corridas):
   valor_corriadas = float(input("valor das corridas:"))
   valor_total = valor_corriadas + valor_total
   uber = valor_total * (25/100)
   motorista = valor_total - uber

  print("valor total:", valor_total)
  print("valor do aplicatvo:", uber)
  print("valor do motorista:", motorista)


programa()

  







  