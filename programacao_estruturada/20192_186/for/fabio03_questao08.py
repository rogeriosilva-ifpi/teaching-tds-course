# 8. Leia N , LimiteSuperior e LimiteInferior e
# escreva todos os múltiplos de N entre os limites lidos.


def programa():
    n = int(input('N: '))
    limite_superior = int(input('LS: '))
    limite_inferior = int(input('LI: '))

    for numero in range(limite_inferior, limite_superior+1, 1):
        if numero % n == 0:
            print(numero)


programa()
