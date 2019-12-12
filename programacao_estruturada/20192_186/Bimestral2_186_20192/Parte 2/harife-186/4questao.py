codigo_produto = int(input("qual o codigo do produto?: "))
total_compra = 0

finalizador = 0

while finalizador < 1:
    codigo_produto = int(input("qual o codigo do produto?: "))
    if codigo_produto == 0:
       finalizador = finalizador + 1
    elif codigo_produto == 1:
        total_compra = 4.00 + total_compra
    elif codigo_produto == 2:
        total_compra = 4.50 + total_compra
    elif codigo_produto == 3:
        total_compra = 5.00 + total_compra
    elif codigo_produto == 4:
        total_compra == 2.00 + total_compra
    elif codigo_produto == 5:
        total_compra = 1.50 + total_compra
    else:
        total_compra = 0 + total_compra
taxa_de_servicos = total_compra * 0.10

print("esse e o preco total",total_compra,"esse e a taxa de servicos", taxa_de_servicos)
troco = input("precisa de troco? sim ou nao: ")
if troco == "sim":
    dinheiro = int(input("quanto e seu dinheiro? "))
    troco = dinheiro - total_compra
    print("aqui esta seu troco", troco)
if troco == "nao":
    print("obrigado por comprar")
