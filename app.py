from flask import Flask, jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./movies.json').read())
data=jData["Movies"]

# Intial request Ex: http://192.168.99.100:5000/
@app.route('/')
def route_main():
    return render_template("Home.html")

# Returns JSON which containes all movies
@app.route('/getmovies/')
def movies_all():
    return render_template("index.html",items=data)

# Returns movies JSON which matches the id
@app.route('/getmovies/<string:id>/')
def movie_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the movies JSON with particualr game type
@app.route('/getmovies/type/<string:type>/')
def movie_type(type=''):
    myList=[]
    for element in data:
        if element["type"].lower() == type.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
