objetivo = float(input("qual e o objetivo a ser acumulado?: "))
taxa_anual = (input("qual e a taxa mensal, poupanca ou cdi ?: "))
valor_mensal = float(input("qual o valor de deposito mensal?: "))
total_de_meses = 0
if taxa_anual == "poupanca":
    taxa_anual = 0.35/12
elif taxa_anual == "cdi":
    taxa_anual = 0.49/12

total_mensal = 0

while total_mensal < objetivo:
    arrecadado = valor_mensal * taxa_anual
    total_mensal = total_mensal + arrecadado
    total_de_meses = 1 + total_de_meses


anos = total_de_meses // 12
meses = total_de_meses % 12
print("esse e o total acumulado mensalmente", total_mensal)
print("essa e a quantidade de anos para cumprir o objetivo", anos,"anos e",meses,"meses")