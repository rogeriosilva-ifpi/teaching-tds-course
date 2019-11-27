from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contar', methods=['POST',])
def contar():
    frase = request.form.get('frase')
    contador_vogal = 0
    contador_consoante = 0

    for caractere in frase:
        if eh_letra(caractere):
            if eh_vogal(caractere):
                contador_vogal += 1
            else:
                contador_consoante += 1

    # retorno "raw" a ser melhoradao
    return '<h1 style="color: red"> Vogais ' + str(contador_vogal) + ' Consoantes ' + str(contador_consoante) +'</h1>'
    
    

def eh_letra(c):
    if eh_letra_maiuscula(c) or eh_letra_minuscula(c):
        return True


def eh_vogal(h):
    vogais = 'AEIOUaeiouÁáÉéÍíÓóÚú'
    if h in vogais:
        return True


def eh_letra_maiuscula(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True


def eh_letra_minuscula(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True

if __name__ == '__main__':
    app.run(debug=True)