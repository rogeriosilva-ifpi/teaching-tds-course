nome = input(' Nome do Professor:  ')
regime = int(input('Qual o regime de trabalho do professor de 20 ou 40 horas ?  '))
qualificacao = input('Qual a qualificação do professor ( digite E, M ou D)? ')


print('Professor: ' , nome)
print('Qualificação', qualificacao)

if regime == 20:
    salario = 2500
    print('$', salario)
else:
    salario = 4500
    print('$', salario)
    
if qualificacao == 'E':
    adicional = 30/100   
elif qualificacao == 'M':
    adicional = 52/100
elif qualificacao == 'D':
    adicional = 70/100    
else:
    print('XXXXXComando para qualificação do professor invalido!!!!!!!!!!!!!!!')

salario_bruto = salario + (salario * adicional)
previdencia = salario_bruto * (11/100)
imposto_renda= salario_bruto*(27.5/100)
descontos = imposto_renda + previdencia
salario_liquido = salario_bruto - descontos

print('salario bruto:', salario_bruto)
print('Previdencia', previdencia)
print('Imposto de Renda', imposto_renda)
print('Salario Líquido', salario_liquido)
