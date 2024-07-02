from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar_livro")
def listar_livro():
    with db_session:
        # obtém os livros
        livros = Livro.select() 
        return render_template("listar_livro.html", livros=livros)

@app.route("/form_adicionar_livro")
def form_adicionar_livro():
    return render_template("form_adicionar_livro.html")

@app.route("/adicionar_livro")
def adicionar_livro():
    # obter os parâmetros
    nome = request.args.get("nome")
    editora = request.args.get("editora")
    autor = request.args.get("autor")
    genero = request.args.get("genero")
    classificacaoIndicativa = request.args.get("classificacaoIndicativa")
    anoDeEdicao = request.args.get("anoDeEdicao")
    # salvar
    with db_session:
        # criar a pessoa
        l = Livro(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_livro") 

'''
# criar o ambiente virtual:
python3 -m venv venv

# ativar o ambiente virtual:
source venv/bin/activate

# desativar o ambiente virtual:
deactivate

# instalar pacotes python:
python3 -m pip install nomePacote

# instalar flask:
python3 -m pip install flask

# instalar pacotes de um arquivo de texto:
python3 -m pip install -r requirements.txt

# rodar um projeto flask:
python3 app.py
'''

# git config --global user.email "you@example.com"
#   git config --global user.name "Your Name"

if __name__ == '__main__':
    app.run(debug=True)