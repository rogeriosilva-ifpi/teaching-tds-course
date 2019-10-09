# Fizz-buzz
# Esta função responsável por converter múltiplos
# de 3 em 'fizz', múltiplos de 5 em 'buzz' e
# múltiplos de ambos em 'fizz-buzz'.
# Números não divisíveis, são retornados normalmente.
from Testes import teste, msg_sucesso, msg_inicio


def fizzbuzz(n):
    pass


msg_inicio('FizzBuzz')
teste(fizzbuzz(1), 1)
teste(fizzbuzz(2), 2)
teste(fizzbuzz(3), 'fizz')
teste(fizzbuzz(4), 4)
teste(fizzbuzz(5), 'buzz')
teste(fizzbuzz(15), 'fizzbuzz')
teste(fizzbuzz(30), 'fizzbuzz')
teste(fizzbuzz(148), 148)
msg_sucesso()
