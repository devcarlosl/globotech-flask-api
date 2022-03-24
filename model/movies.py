
from flask import Flasks

app = Flask(__name__)
api = Api(app) 

#list = Movies("Movies")
#@Movies.route("/movies") 

class Movies:
  _movies_list = list()

  def __init__(self, id, name, synopsis, rate, poster_url, main_cast) -> None:
    self.id = id
    self.name = name
    self.synopsis = synopsis
    self.rate = rate
    self.poster_url = poster_url
    self.main_cast = main_cast

  @classmethod
  def add_movie(cls, movie):
    cls._movies_list.append(movie)