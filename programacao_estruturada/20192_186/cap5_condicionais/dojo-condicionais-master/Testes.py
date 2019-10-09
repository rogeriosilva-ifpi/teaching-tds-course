# Exercícios by Nick Parlante (CodingBat)

# Para entender o uso de cores no terminal, assita a aula do
# professor Guanabara no YouTube. Segue o link direto:
# https://youtu.be/0hBIhkcA8O8
COR = {
    'pa_vm': '\033[7:1:31m',  # cor padrão no fundo vermelho
    'pa_vd': '\033[7:1:32m',  # cor padrão no fundo verde
    'pa_az': '\033[7:1:34m',  # cor padrão no fundo azul
    'vd': '\033[32m',  # verde
    'vm': '\033[31m',  # vermelho
    'fim': '\033[0m',  # fim da cor
}


# Funções com mensagens para inicio dos testes, sucesso e falha.
def msg_inicio(texto):
    print('\n{} Problema: {}. Executando testes... {}\n'.format(
        COR['pa_az'], texto, COR['fim']))


def msg_sucesso():
    print('\n{} Testes finalizados com sucesso. Platéia Participa! {}'.format(
        COR['pa_vd'], COR['fim']))


def msg_falha():
    print('\n{} Falha durante execução dos Testes. Silêncio na Platéia! {}'.format(
        COR['pa_vm'], COR['fim']))


# Uma simples função teste() usada em para imprimir
# o que cada função retorna e o que deveria retornar.

def teste(obtido, esperado):
    if obtido == esperado:
        print('{} [Passou] Esperado {}, {} obtido. Parabéns! {}'.format(
            COR['vd'], repr(esperado), repr(obtido), COR['fim']))
    else:
        print('{} [Falhou] Esperado {}, {} obtido. Tente novamente! {}'.format(
            COR['vm'], repr(esperado), repr(obtido), COR['fim']))
        msg_falha()
        exit(1)  # Encerra a execução dos testes com código 1 (falha)


def main():
    pass


if __name__ == '__main__':
    main()
