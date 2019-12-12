
n = int(input('qual a media anual da sua escola: '))
a = int(input('qual sua nota 1: '))
b = int(input('qual sua nota 2: '))
c = int(input('qual sua nota 3: '))
d = int(input('qual sua nota 4: '))

soma = (a + b + c + d)-n

def media_anual():
    if soma < 0:
        print ('aluno reprovado')
    else:
        print ('passou')

media_anual()
