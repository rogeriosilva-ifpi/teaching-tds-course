media_escola = int(input("qual a media da sua escola?: "))
contador = 0
pontos_das_notas = 0 
quantidade_de_notas = 4

print("agora coloque suas notas bimestrais")

while contador < 4:
    contador = contador + 1
    notas = int(input("qual sua nota bimestral?: "))
    pontos_das_notas = notas + pontos_das_notas

media_aluno = pontos_das_notas / 4

if media_aluno >= media_escola:
    print("voce foi aprovado")
else:
    print("voce foi reprovado")