import os
import json
from flask import Flask, render_template, request, flash, redirect, url_for
if os.path.exists('env.py'):
    import env
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_drinks')
def get_drinks():
    return render_template('drinks.html', drinks=mongo.db.drinks.find())


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/recipes')
def recipes():
    return render_template('recipes.html', page_title='Recipes')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we'll get back to you shortly!".format
            (request.form["name"]))
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["message"])
    return render_template('contact.html', page_title='Contact')


if __name__ =='__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)