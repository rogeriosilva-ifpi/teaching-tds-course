def salario():
    ch =int(input("digite sua carga horaria : "))
    nome =input("nome do professor:")
    q = input("digite sua qualificação , em : e,m,d: ")
    if ch==20 and q=="e":
        x =(2500 * (30/100))+2500
        print(x)
    elif ch==20 and q=="m":
         y =(2500 * (52/100))+2500
         print(y)
    elif ch==20 and q=="d":
         z =(2500 * (70/100))+2500
         print(z)
    elif ch==40 and q=="e":
        x =(4500 * (30/100))+4500
        print(x)
    if ch==40 and q=="m":
         x =(4500 * (52/100))+4500
        print(x)
    if ch==40 and q=="d":
         x =(4500 * (70/100))+4500
        print(x)
 
salario()
