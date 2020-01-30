def programa():
    # Entrada
    inscritos_antes = int(input('Quantos inscritos antes: '))
    visualizacoes_antes = int(input('Quantas visualizações antes: '))

    inscritos_depois = int(input('Quantos inscritos depois: '))
    visualizacoes_depois = int(input('Quantas visualizações depois: '))

    # Processamento
    diff_inscritos = (
        (inscritos_depois - inscritos_antes) / inscritos_antes)*100
    diff_visualizacoes = ((visualizacoes_depois / visualizacoes_antes) - 1)*100

    # Saída
    print('Aumento percentual em Inscritos: ', diff_inscritos)
    print('Aumento percentual em Visualizações: ', diff_visualizacoes)


programa()
