# Exercícios by Nick Parlante (CodingBat)
# Soma Dobro
# dados dois números inteiros retorna sua soma,
# porém se os números forem iguais,
# retorna o dobro da soma.
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8
from Testes import teste, msg_sucesso, msg_inicio


def soma_dobro(a, b):
    return a+b if a != b else 2*(a+b)


msg_inicio('Soma Dobro')
teste(soma_dobro(1, 2), 3)
teste(soma_dobro(3, 2), 5)
teste(soma_dobro(2, 2), 8)
teste(soma_dobro(-1, 0), -1)
teste(soma_dobro(0, 0), 0)
teste(soma_dobro(0, 1), 1)
msg_sucesso()
