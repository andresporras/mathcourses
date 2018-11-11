"""
Routes and views for the flask application.
"""
#http://api.mongodb.com/python/current/tutorial.html
#https://dzone.com/articles/top-10-most-common-commands-for-beginners
#https://flask-restful.readthedocs.io/en/latest/api.html
#edit app.py comment options.setdefault('use_reloader', self.debug) int order to allow debugging
#https://mongoosejs.com/docs/guide.html how to connect to database with password and username


from datetime import datetime
from flask import render_template
from flask import Flask, request #import main Flask class and request object
from FlaskWebProject1 import app
from pymongo import MongoClient
import pprint
from flask_restful import Resource, Api


client = MongoClient('localhost', 27017)

db = client['demo']

collection = db['first']

c=collection.find_one()

d=collection.find({})


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/json-example')
def json_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    return '''<h1>The language value is: {}</h1>'''.format(language)

@app.route('/mongodb-example')
def mongodb_example():
    return '''{}'''.format(c)



