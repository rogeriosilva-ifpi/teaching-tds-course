def progama():
    peso = float(input('Digite o peso'))
    altura = float(input('Digite a altura'))

    print(imc(peso,altura))

def imc (peso,altura):
    imc = peso / (altura ** 2)
    if (imc < 17):
        return 'Muito abaixo do peso' 
    elif((imc >17) and (imc < 18.49)):
        return 'Abaixo do peso'
    elif((imc > 18.5) and (imc < 24.99)):
        return 'Peso normal'
    elif((imc > 25) and (imc < 29.99)):
        return 'Acima do peso'
    elif((imc > 30) and (imc < 34.99)):
        return 'Obsidade I'
    elif((imc > 35) and (imc < 39.99)):
        return 'Obsidade II'
    elif(imc > 40):
        return "obsidade III"
progama()