def main():
    vdm = float(input('digite o valor de mercado do  veiculo: '))
    idadev = float(input('digite a idade do seu veiculo: '))
    imposto = (2/100*vdm)+(1/2)/100*vdm
    descontoum = imposto-(15/100)*imposto
    descontodois = imposto-(20/100)*imposto
    
    if idadev > 15:
        print('voçê esta isento')
    elif idadev <= 5 and idadev >= 10:
        print('voçê tera que pagar ', descomtoum)
    elif idadev >= 11 and idadev <=15:
        print('voçê tera que pagar ', descontodois)
    else:
        print('voçê tera que pagar ', imposto)
    
    
    

main()
