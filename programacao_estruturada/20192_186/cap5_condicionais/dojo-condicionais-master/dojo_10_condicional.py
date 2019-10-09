# Exercícios by Nick Parlante (CodingBat)
# Troca Letras
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
from Testes import teste, msg_sucesso, msg_inicio


def troca(s):
    pass


msg_inicio('Troca Letras')
teste(troca('code'), 'eodc')
teste(troca('a'), 'a')
teste(troca('ab'), 'ba')
teste(troca('abc'), 'cba')
teste(troca(''), '')
teste(troca('Chocolate'), 'ehocolatC')
teste(troca('nythoP'), 'Python')
teste(troca('hello'), 'oellh')
msg_sucesso()
