def notas():
    a = 0
    soma = 0
    while a <=3:
        nota = float(input("Digite uma nota: "))
        soma = soma + nota
        a = a + 1
    print(soma)
    med = soma/4
    media = int(input("Digite a media praticada na escola: "))
    print("A media do aluno foi:",med)
    if med >= media:
        print("Foi aprovado!")
    else:
        print("Foi reprovado!")

notas()
        
