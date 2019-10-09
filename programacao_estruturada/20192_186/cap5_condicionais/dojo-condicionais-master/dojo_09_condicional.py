# Exercícios by Nick Parlante (CodingBat)
# Apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
from Testes import teste, msg_sucesso, msg_inicio


def apaga(s, n):
    pass


msg_inicio('Apaga')
teste(apaga('kitten', 1), 'ktten')
teste(apaga('kitten', 0), 'itten')
teste(apaga('kitten', 4), 'kittn')
teste(apaga('Hi', 0), 'i')
teste(apaga('Hi', 1), 'H')
teste(apaga('code', 0), 'ode')
teste(apaga('code', 1), 'cde')
teste(apaga('code', 2), 'coe')
teste(apaga('code', 3), 'cod')
teste(apaga('chocolate', 8), 'chocolat')

teste(apaga('chocolate', 8), 'chocola')  # Erro proposital

msg_sucesso()
