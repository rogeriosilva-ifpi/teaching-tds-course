def main():
    notaI = float(input("DIGITE A 1° NOTA:"))
    notaII = float(input("DIGITE A 2° NOTA: "))
    notaIII = float(input("DIGITE A 3° NOTA: "))
    notaIIII = float(input("DIGITE A 4° NOTA: "))
    aprov = float(input("DIGITE A media aprovativa: "))
    media =(notaI+notaII+notaIII+notaIIII)//4
    if media >= aprov :
        print("aluno aprovado")
    else:
        print("aluno reprovado")
    
main()
