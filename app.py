# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Cauã" # escreva seu nome
    idade = "15" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route('/pagina_pai')
def pag_pai():

    return render_template("pai.html", nome = alexandre, idade = 40)



# defina a rota para a página da mãe
@app.route('/pagina_mae')
def pag_mae():

    return render_template("mae.html", nome = anapaula, idade = 42)



# defina a rota para a página do amigo
@app.route('/pagina_amigo')
def pag_amg():

    return render_template("amigo.html", nome = victor, idade = 14)


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
   
