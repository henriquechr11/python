from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def curriculo():
    dados = {
        "nome": "Henrique Santos Tavares",
        "email": "henriquestv18@gmail.com",
        "escola": "Escola Técnica do COTEMIG",
        "tecnologias": ["MySQL", "C#", "N8N", "Python", "React"]
    }
    return render_template('index.html', **dados)

@app.route('/cotemig')
def rota_cotemig():
    nome_escola = "Escola Técnica do COTEMIG"
    return f"<h1>{nome_escola}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
