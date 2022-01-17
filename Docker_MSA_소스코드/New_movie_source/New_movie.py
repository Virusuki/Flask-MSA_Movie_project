from flask import Flask, request, Response
from flask_restx import Resource, Api, fields
from flask import abort, jsonify


app = Flask(__name__)
api = Api(app)

ns_Movie = api.namespace('ns_Movie', description='Movie APIs')

movie_data = api.model(
    'Movie Data',
    {
      "Movie title": fields.String(description="Movie name", required=True),
      "Jenre": fields.String(description="Jenre type", required=True),
      "year": fields.Integer(description="year", required=True),
    }
)

movie_info = {}
number_of_movies = 0

@ns_Movie.route('/Movies')
class movies(Resource):
  def get(self):
    return {
        'number_of_movies': number_of_movies,
        'movie_info': movie_info
    }


@ns_Movie.route('/Movies/<string:jenre>')
class movies_jenre(Resource):
  def get(self, jenre):
    if not jenre in movie_info.keys():
      abort(404, description=f"jenre {jenre} doesn't exist")
    data = movie_info[jenre]

    return {
        'number_of_movies': len(data.keys()),
        'data': data
    }

  
  def post(self, jenre):
    if jenre in movie_info.keys():
      abort(409, description=f"jenre {jenre} already exists")

    movie_info[jenre] = dict()
    return Response(status=201)


  
  def delete(self, jenre):
    if not jenre in movie_info.keys():
      abort(404, description=f"jenre {jenre} doesn't exists")
      
    del movie_info[jenre]
    return Response(status=200)


  
  def put(self, jenre):
    # todo
    return Response(status=200)
    

@ns_Movie.route('/Movies/<string:jenre>/<int:jenre_id>')
class movies_jenre_model(Resource):
  def get(self, jenre, jenre_id):
    if not jenre in movie_info.keys():
      abort(404, description=f"jenre {jenre} doesn't exists")
    if not jenre_id in movie_info[jenre].keys():
      abort(404, description=f"Car ID {jenre}/{jenre_id} doesn't exists")

    return {
        'jenre_id': jenre_id,
        'data': movie_info[jenre][jenre_id]
    }

  @api.expect(movie_data) # body
  def post(self, jenre, jenre_id):
    if not jenre in movie_info.keys():
      abort(404, description=f"jenre {jenre} doesn't exists")
    if jenre_id in movie_info[jenre].keys():
      abort(409, description=f"Car ID {jenre}/{jenre_id} already exists")

    params = request.get_json() # get body json
    movie_info[jenre][jenre_id] = params
    global number_of_movies
    number_of_movies += 1
  
    return Response(status=200)
  

  def delete(self, jenre, jenre_id):
    if not jenre in movie_info.keys():
      abort(404, description=f"jenre {jenre} doesn't exists")
    if not jenre_id in movie_info[jenre].keys():
      abort(404, description=f"Car ID {jenre}/{jenre_id} doesn't exists")

    del movie_info[jenre][jenre_id]
    global number_of_movies
    number_of_movies -= 1

    return Response(status=200)


  @api.expect(movie_data)
  def put(self, jenre, jenre_id):
    global movie_info

    if not jenre in movie_info.keys():
      abort(404, description=f"jenre {jenre} doesn't exists")
    if not jenre_id in movie_info[jenre].keys():
      abort(404, description=f"Car ID {jenre}/{jenre_id} doesn't exists")
    
    params = request.get_json()
    movie_info[jenre][jenre_id] = params
    
    return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
