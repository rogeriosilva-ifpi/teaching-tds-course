nome = str(input('diga seu nome: '))
h = int(input('diga seu regime de trabalho: '))
q = str(input('e sua qualificação: '))


def salario_fixo():
    if h == 20:
        return 2.500
    if h == 40:
        return 4.500


def qualificacao():
    if q == e:
        return 30
    elif q == m:
        return 52
    elif q == d:
        return 70


salario_bruto = (salario_fixo() * qualificacao()) / 100
desconto = 38.5
salario_liquido = (salario_bruto * desconto) / 100
print(name, 'o salario liquido é, ', salario_liquido)
