from json import dumps, loads
from flask_restful import Resource, reqparse
from model.movies import MoviesModel

class Movies(Resource):
    # def get(self, id=None):
    #     if id:
    #         found_post = MoviesModel.find_post(id)
    #         if found_post:
    #             return found_post.to_dict()
    #         return {"message": "Post not found"}, 404
    #     else:
    #         return MoviesModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("name")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("poster_url")
        body_arguments.add_argument("main_cast")

    #     params = body_arguments.parse_args()
    #     new_post = MoviesModel(params["user_name"], params["text"])
    #     MoviesModel.add_post(new_post)
    #     return new_post.to_dict()

    # def put(self, id):
    #     found_post = MoviesModel.find_post(id)
    #     if found_post:
    #         body_arguments = reqparse.RequestParser()
    #         body_arguments.add_argument("text")
    #         params = body_arguments.parse_args()
    #         found_post.text = params.text
    #         return found_post.to_dict()
    #     return {"message": "Post not found"}, 404    
        
    # def delete(self, id):
    #     found_post = MoviesModel.find_post(id)
    #     if found_post:
    #         MoviesModel.remove_post(found_post)
    #         return found_post.to_dict()
    #     return {"message": "Post not found"}, 404
