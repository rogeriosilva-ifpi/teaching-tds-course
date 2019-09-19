def potencia(numero, expoente):
    resultado = numero ** expoente
    return resultado


valor = int(input('Valor: '))
exp = int(input('Expoente: '))
retorno = potencia(valor, exp)
print(valor, 'elevado a', exp, '=', retorno)
