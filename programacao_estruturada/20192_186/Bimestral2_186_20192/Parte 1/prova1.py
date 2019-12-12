


#questao 2
def nota():
    print("============================")
    nota = float(input(" NOTA :"))
    if nota == 9 or nota == 10 :
        print(" nota da prova : A")

    if nota == 8 or  nota == 8.9 or nota == 8.999:
        print(" nota da prova : B")
    
    if nota == 7 or nota == 7.999 or nota ==7.9:
        print(" nota da prova : C")
    if nota < 7:
    
        print(" nota da prova : E")
    print("=============================")
#questao 3
def bissexto():      
    print("ANOS BISSEXTO")    
    for i in range(2004, 2098):
        if i % 4 == 0:
        
            print(i)


#lista = []

#for i in range(1,11):
    #n = int(input(" informe o {}° numero :".format(i)))
    #lista.append(n)

#for k in lista:
 #   n1 = k[0] / k[9]
#print(n1)


#questao 6
def nasc():
 ano = {}

 qt = 0
 aluno = int(input("quantidades de alunos da turma :"))
 for i in range(aluno):
    nasc = int(input("ano da nascimento do aluno :"))
    if nasc in ano:
        qt += 1
    ano[nasc]=qt
    
        
  
     
         
        
    
    
    print(ano)
print("questao 2,3,6")
ques = int(input("numero da questao:"))
if ques == 2:
    nota()
if ques == 3:
    bissexto()
if ques == 6:
    nasc()   
