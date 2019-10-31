#quinta QUESTÃO
angulo = float(input('informe um angulo entre 0° e 360° para saber em qual quadrante se encontra\n>>>'))

if angulo <= 90:
    print ('primeiro quadrante')
    
elif angulo > 90 and angulo <= 180:
     print ('segundo quadrante')
    
elif angulo > 180 and  angulo <= 270:
    print ('terceiro quadrante')
    
else:
    print ('quarto quadrante')