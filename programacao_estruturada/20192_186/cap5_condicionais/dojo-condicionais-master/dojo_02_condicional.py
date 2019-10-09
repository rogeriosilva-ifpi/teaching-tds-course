# Exercícios by Nick Parlante (CodingBat)
# Dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo
#  quando é feriado ou não é dia semana
# retorne True ou False conforme
# você vá dormir ou não
from Testes import teste, msg_sucesso, msg_inicio


def dormir(dia_semana, feriado):
    return not dia_semana or feriado


msg_inicio('Dormir')

teste(dormir(False, False), True)
teste(dormir(True, False), False)
teste(dormir(False, True), True)
teste(dormir(True, True), True)
msg_sucesso()
