from flask import Flask, render_template, jsonify, Response, request
import requests
import os

app = Flask(__name__)

movie_informer_ip = os.environ.get("movie-informer-ip")

@app.route("/")
def muvie():
  dic = {}
#  data = requests.get('http://192.168.35.79:5001/ns_Movie/Movies').json()
  data = requests.get('http://' + movie_informer_ip+ ':5001/ns_Movie/Movies').json()
  num = 1       
  each_movie_info = {}
  i = 0
  # (movie info) json file parsing
  for w in data:                                   # w  ->  'number_of_movies', 'movie_info'
      if type(data[w]) is dict:
          for two_w in data[w]:                    # two_w -> romance, sf            
              if type(data[w][two_w]) is dict:
                  for three_w in data[w][two_w]:   # three_w -> 1,2,3
                      each_movie_info[i] = data[w][two_w][three_w]
                      each_movie_info[i]['num'] = num
                      i += 1
                      num += 1

  for z in range(len(each_movie_info), 14):
      each_movie_info[z]  = 'Unscreened'                    
  return render_template('index.html', dic = each_movie_info )

@app.route("/movie_info/<string:dic>")
def movie_info(dic):
  get_detail_movie_info = dic.split(',')

  movie_detail_info = requests.get('http://'+movie_informer_ip+':5001/ns_Movie/Movies/'+get_detail_movie_info[0]+'/'+get_detail_movie_info[1]).json()

  return render_template('movie_info.html', info=movie_detail_info)  
    

@app.route("/about")
def mouvie_about():
  return render_template('about.html')

@app.route("/upload")
def mouvie_upload():
#  movie_informerip = 'http://'+movie_informer_ip+':31234'
  movie_informerip = 'http://172.30.4.174:31234' # IP replace (domain info)
#  movie_informerip = 'http://192.168.35.79:5001/' # IP replace (domain info)

  return render_template('upload.html', movie_informer=movie_informerip)


if __name__=="__main__":
  app.run(host="0.0.0.0", port="5000", debug=True)
