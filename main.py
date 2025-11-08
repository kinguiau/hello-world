import os
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='src/static', template_folder='src/templates')

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota que processa o formulário de IMC
@app.route('/imc', methods=['POST'])
def calcular_imc_form():
    try:
        peso = float(request.form.get('peso', 0))
        altura = float(request.form.get('altura', 0))

        if altura <= 0 or peso <= 0:
            return render_template('error.html', error_message="Peso ou altura inválidos!", status_code=400), 400

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        return render_template('imc.html', peso=peso, altura=altura, imc=round(imc, 2), classificacao=classificacao)

    except Exception as e:
        return render_template('error.html', error_message=f"Erro ao calcular o IMC: {str(e)}", status_code=500), 500

# Início do servidor
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)