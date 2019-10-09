# Exercícios by Nick Parlante (CodingBat)
# Alunos Problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos estão sorrindo ou ambos não estão sorrindo
# retorne True quando houver problemas
from Testes import teste, msg_sucesso, msg_inicio


def alunos_problema(a_sorri, b_sorri):
    pass


msg_inicio('Alunos Problema')
teste(alunos_problema(True, True), True)
teste(alunos_problema(False, False), True)
teste(alunos_problema(True, False), False)
teste(alunos_problema(False, True), False)
msg_sucesso()
