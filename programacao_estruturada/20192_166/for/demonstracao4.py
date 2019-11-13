def principal():
    inicio = int(input('A0: '))
    limite = int(input('Limite: '))
    razao = int(input('Razao: '))

    for i in range(inicio, limite, razao):
        print(i)


principal()
