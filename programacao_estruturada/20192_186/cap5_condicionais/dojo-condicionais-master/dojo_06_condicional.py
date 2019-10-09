# Exercícios by Nick Parlante (CodingBat)
# Papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
from Testes import teste, msg_sucesso, msg_inicio


def papagaio(falando, hora):
    return falando and (hora < 7 or hora > 20)


msg_inicio('Papagaio')
teste(papagaio(True, 6), True)
teste(papagaio(True, 7), False)
teste(papagaio(False, 6), False)
teste(papagaio(True, 21), True)
teste(papagaio(False, 21), False)
teste(papagaio(True, 23), True)
teste(papagaio(True, 20), False)
msg_sucesso()
