from flask import Flask
from flask_restful import Api
from resources.movies import Movies

app = Flask(__name__)
api = Api(app)


api.add_resource(Movies, "/movies/<int:id>" , "/movies")

# @app.route('/movies')
# def list():
#     return 'Primeira rota'

# @app.route('/movies/<int:id>')
# def show():
#     return 'Buscar 1 filme'

# @app.route('/movies', methods=["POST"])
# def create():
#      return 'Criado 1 filme'

# @app.route('/movies/<int:id>', methods=["PUT"])
# def update():
#     return 'Atualizar 1 filme'

# @app.route('/movies/<int:id>', methods=["DELETE"])
# def delete():
#     return 'Deletar 1 filme'

if __name__ == '__main__':
    app.run(debug=True)
