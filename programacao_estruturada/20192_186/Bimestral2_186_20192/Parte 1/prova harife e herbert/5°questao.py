quantidade_de_experimentos = int(input('qual a quantidade de experimentos: '))
ratos = 0
sapos = 0
coelhos = 0
total_de_animais = 0
contador = 0
while contador < quantidade_de_experimentos:
    contador = contador + 1
    animais = input('qual é o animal do experimento(sapos,ratos ou coelhos:)')
    if animais == 'sapos':
        quantidade = int(input('quantos sapos?: '))
        sapos = quantidade + sapos
    elif animais == 'ratos':
        quantidade = int(input('quantos ratos?: '))
        ratos = quantidade + ratos
    elif animais == 'coelhos':
        quantidade = int(input('quantos coelhos?: '))
        coelhos = quantidade + coelhos
    

total_de_animais = ratos + sapos + coelhos
percetagem_sapos = sapos/total_de_animais
percetagem_ratos = ratos/total_de_animais
percetagem_coelhos = coelhos/total_de_animais

print('esse é o total de animais usados',total_de_animais,'\n esse o total de coelhos',coelhos,'\n esse é o total de sapos',sapos,'\n esse é o total de ratos',ratos,)
print('essa é a percentagem de sapo, ratos e coelhos na ordem descrita',percetagem_sapos, percetagem_ratos, percetagem_coelhos )