def main():
    cd = int(input('digite quantas corridas voçê fez ao dia: '))
    for i in range(cd):
        qt = float(input('quanto voçê ganhou com essa corrida?:  '))
        vap = (25/100)*qt
        vm = (75/100)*qt
        vta = qt*2
        vtap = vap*2
        vtf = vm*2
    print(vta)
    print(vtap)
    print(vtf)


main()