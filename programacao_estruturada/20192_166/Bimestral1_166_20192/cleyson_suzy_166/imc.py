def imc ( ):
    altura = float(input("digite sua altura: "))
    peso =float(input("digite seu peso em kg:" ))
    imc = peso//(altura*altura)
    if imc <17:
        print("muito abaixo do peso")
    elif imc >=17 or  imc<=18.49:
        print("abaixo do peso")
    elif imc >=18.5 or imc<=24.99:
        print("peso normal")
    elif imc >=25 or imc<=29.99:
        print("acima do peso")
    elif imc >=30 or imc<=34.99:
        print("obesidade I")
    elif imc >=35 or imc<=39.99:
        print("obesidade II(SEVERA)")
    else :
        print("obesidade III(MÓRBIDA)")
    
imc( )
 
