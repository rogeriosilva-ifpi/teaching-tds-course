def regime_salario(regime):
    if regime == 20:
        return 2500
    elif regime == 40:
        return 4500

def qualificacao_adicional(qualificacao):
    if qualificacao == 'E':
        return 0.30
    elif qualificacao == 'M':
        return 0.52
    elif qualificacao == 'D': 
        return 0.70

nome = input("Digite o nome do professor: ")

######## cálculo do salário base pelo regime #########
regime = int(input("Digite se o regime de trabalho é \"20\" para 20h ou \"40\" para 40h: "))

while(regime != 20 and regime != 40):
    print("Carga horária inválida\n")
    regime = int(input("Digite se o regime de trabalho é \"20\" para 20h ou \"40\" para 40h: "))

salario_base = regime_salario(regime)

print()

########### cálculo do adicional pela qualificação ##############
qualificacao = input("Digite se a qualificação \"E\" para Especialista, \"M\" para Mestre ou \"D\" para Doutor: ")
qualificacao = qualificacao.upper()

while(qualificacao != 'E' and qualificacao != 'M' and qualificacao != 'D'):
    print("Entrada inválida\n")
    qualificacao = input("Digite se a qualificação \"E\" para Especialista, \"M\" para Mestre ou \"D\" para Doutor: ")
    qualificacao = qualificacao.upper()

adicional_porcentagem = qualificacao_adicional(qualificacao)

print()

################## Obtenção do salário bruto #####################
salario_bruto = salario_base + (salario_base * adicional_porcentagem)

############################# Deduções ##################################
previdencia = salario_bruto * 0.11
imposto_de_renda = salario_bruto * 0.275

########################### Obtenção do salário líquido ################################
salario_liquido = salario_bruto - (previdencia + imposto_de_renda)

print("Nome do professor: %s" % nome)
print("Regime: %dh" % regime)
print("Qualificação: %s" % qualificacao)
print("Salário bruto: R$%0.2f" % salario_bruto)
print("Salário líquido: R$%0.2f" % salario_liquido)