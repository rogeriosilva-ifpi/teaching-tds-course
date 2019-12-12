nota_geral = 0
for nota in range(0,4):
    nota = float(input("Digite sua nota: "))
    nota_geral += nota

media = float(input("Digite a média da sua escola"))

media_da_nota = nota_geral / 4

if media_da_nota > media:
    print("Sua média é {} e você foi aprovado, parabéns!!!".format(media_da_nota))
else:
    print("Sua média é {} e você infelizmente não foi aprovado, estude mais!!!".format(media_da_nota))