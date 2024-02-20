from flask import Blueprint,render_template,request
from database.database import  db,Filme

db.connect()
db.create_tables ([Filme])

filmes_route = Blueprint('filmes', __name__)


##------------lista de filmes X-----------##
@filmes_route.route('/')
def lista_filmes():
    return render_template('lista_filmes.html',filmes=Filme.select())

##---------------------------------------##






##------------inserir filme X----------------##
@filmes_route.route('/', methods=['POST'])
def inserir_filme():
    nome = request.form.get("nome")
    nota = request.form.get("nota")
    filme_novo=Filme.create(nome=nome,nota=float(nota))
    print(filme_novo.nome,type(filme_novo.nota))
    
    
    return render_template("item_filme.html",filme=filme_novo)

   
    
##---------------------------------------##






##------------novo filme X----------------##
@filmes_route.route('/new')
def form_filme():
    filme=False
    return render_template('form_filme.html',filme=filme)

##---------------------------------------##






##------------detalhes filme----------------##
@filmes_route.route('/<int:filme_id>')
def detalhe_filmes(filme_id):
     filme = Filme.get_by_id(filme_id)
     return render_template('detalhe_filmes.html',filme=filme)

##---------------------------------------##





##------------editar filme----------------##
@filmes_route.route('/<int:filme_id>/edit')
def form_edit_filme(filme_id):
    filme = Filme.get_by_id(filme_id)
    return render_template("form_filme.html",filme=filme)
##----------------------------------------------------------##




##------------Atualizar filme X----------------##
@filmes_route.route('/<int:filme_id>/uptade',methods =['PUT'])
def altualizar_filme(filme_id):
    filme = Filme.get_by_id(filme_id)
    data=request.json
    filme.nome=data["nome"]
    filme.nota=float(data["nota"])
    filme.save()
            
    return render_template('item_filme.html',filme=filme)
##------------------------------------------------------------------##






##----------------------deletar filme X------------------------------##
@filmes_route.route('/<int:filme_id>/delete', methods=['DELETE'])
def deletar_filme(filme_id):
    filme = Filme.get_by_id(filme_id)
    filme.delete_instance()
    return{'deleted':'ok'}   



