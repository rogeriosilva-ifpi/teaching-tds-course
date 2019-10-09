# Exercícios by Nick Parlante (CodingBat)
# Dista 10
# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
from Testes import teste, msg_sucesso, msg_inicio


def dista10(n):
    pass


msg_inicio('Dista 10')
teste(dista10(93), True)
teste(dista10(90), True)
teste(dista10(89), False)
teste(dista10(110), True)
teste(dista10(111), False)
teste(dista10(121), False)
teste(dista10(0), False)
teste(dista10(5), False)
teste(dista10(191), True)
teste(dista10(189), False)
teste(dista10(190), True)
teste(dista10(200), True)
teste(dista10(210), True)
teste(dista10(211), False)
teste(dista10(290), False)
msg_sucesso()
