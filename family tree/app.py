# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def son():

    name = "Durgesh" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def dad():

    name = "Krishna yadav" # write your name
    age = "35" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/Mother")
def mom():

    name = "manuj yadav" # write your name
    age = "33" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/dudes")
def dude():

    name = "MEHUL GHEEK" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
