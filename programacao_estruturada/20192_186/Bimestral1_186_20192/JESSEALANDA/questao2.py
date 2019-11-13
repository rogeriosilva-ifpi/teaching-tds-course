# SEGUNDA QUESTÃO
def salario(regime):
    if salario == 20:
        return 2500
    else:
        return 4500


'''E = 0.3
M = 0.52
D = 0.7'''


def titulo(qualificacao):
    if qualificacao == E:
        return 0.3
    elif qualificacao == M:
        return 0.52
    else:
        return 0.7


def porcentagem(salario, titulo):

    porcentagem = salario * titulo

    return porcentagem


nome = str(input('ola eu sou a Dilma, digite seu nome\n>>>'))

regime = int(input('ola de novo, informe sua carga horaria (20 ou 40)'))

while regime != 20 and regime != 40:
    regime = int(
        input('ola de novo, opçao invalida, informe sua carga horaria (20 ou 40)'))

qualificacao = input(
    'chega de ola, informe sua qualificaçao ( E para especialista, M para mestre e  D para doutor.):\n>>>').upper()

while qualificacao != 'M' and qualificacao != 'E' and qualificacao != 'D':
    qualificacao = input(
        'ola de novo, informe sua qualificaçao novamente ( E para especialista, M para mestre e  D para doutor.):\n>>>').upper()

salario_bruto = regime * porcentagem(qualificacao) + regime

print(nome, 'seu salario bruto é\nR$:', salario_bruto)
