# Fizz-buzz
# Esta função responsável por converter múltiplos
# de 3 em 'fizz', múltiplos de 5 em 'buzz' e
# múltiplos de ambos em 'fizz-buzz'.
# Números não divisíveis, são retornados normalmente.
from Testes import teste, msg_sucesso, msg_inicio


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizz-buzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return n


msg_inicio('FizzBuzz')
teste(fizzbuzz(1), 1)
teste(fizzbuzz(2), 2)
teste(fizzbuzz(3), 'fizz')
teste(fizzbuzz(4), 4)
teste(fizzbuzz(5), 'buzz')
teste(fizzbuzz(15), 'fizz-buzz')
teste(fizzbuzz(30), 'fizz-buzz')
teste(fizzbuzz(148), 148)
msg_sucesso()
