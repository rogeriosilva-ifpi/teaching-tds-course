# Exercícios by Nick Parlante (CodingBat)
# Dez
# dados dois inteiros a e b
# retorna True se um dos dois é 10 ou a soma é 10
from Testes import teste, msg_sucesso, msg_inicio


def dez(a, b):
    pass


msg_inicio('Dez')
teste(dez(9, 10), True)
teste(dez(9, 9), False)
teste(dez(1, 9), True)
teste(dez(10, 1), True)
teste(dez(10, 10), True)
teste(dez(8, 2), True)
teste(dez(8, 3), False)
teste(dez(10, 42), True)
teste(dez(12, -2), True)
msg_sucesso()
