def programa():
    nota1=int(input("digite a primeira nota:"))
    nota2=int(input("digite a segunda nota:"))
    nota3=int(input("digite a terceira nota:"))

    notas = nota1+nota2+nota3
    media_bimestral = notas//3
    if media_bimestral < 7:
        print("reprovado")
    else:
        print("arovado")

programa()