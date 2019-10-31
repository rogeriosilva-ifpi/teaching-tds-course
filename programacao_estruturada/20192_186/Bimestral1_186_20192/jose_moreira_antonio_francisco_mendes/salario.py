def programa():
    professor = str(input("Digite o nome do professor: "))
    salario_base = int(input("Digite a carga horaria: "))
    ch = carga_horaria(salario_base)
    formação = str(input("Digite a qualificação: ")) 
    quali = gradu(formação)

    salario_sem_desconto = ch * quali
    salalario_total = salario_sem_desconto * 0.385

    print("Seu " , professor ," salario Sera R$ ", salalario_total)

def carga_horaria(n):
    if n == 20:
        return 2500
    elif n == 40:
        return 4500

def gradu (x):
    if x == "E":
        return 1.30
    elif x == "M":
        return 1.52
    elif x == "D":
        return 1.70

programa()

