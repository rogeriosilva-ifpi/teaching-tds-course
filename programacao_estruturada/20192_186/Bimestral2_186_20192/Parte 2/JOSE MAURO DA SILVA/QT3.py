valor=float(input('qual o valor do veiculo R$: '))
ano_f=int(input('qual o ano de fabricaçao: '))
#ano_f=2019-ano_f
v_ipva=valor*2.5/100
valo_t=valor-ano_f
if ano_f<5:
    print('valor do IPVA e: ',v_ipva)
    
