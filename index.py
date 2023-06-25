from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pegar_fotos')
def pegar_fotos():
    diretorio = "D:\Fotos"
    fotos = []

    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.lower().endswith(('.jpg')):
                caminho_completo = os.path.join(root, file)
                fotos.append(caminho_completo)

    return render_template('fotos.html', fotos=fotos)

if __name__ == '__main__':
    app.run()
