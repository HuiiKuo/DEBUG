# app.py
import os
from flask import Flask, Response, request, abort, redirect
# import requests

import json
import sys
from controller import(user)
from controller import(people)
from model.db import mongo

from model import userModel
from model import peopleModel



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://numbone112:i3PO8xrZj1KRwz83@cluster0.5rqnhen.mongodb.net/efu"
mongo.init_app(app) # initialize here!
print(type(mongo))
print((mongo.db.name))
app.register_blueprint(user.userProfile)
app.register_blueprint(people.peopleProfile)



@app.route('/', methods=["POST"])
def line():
    return "ok"


@app.route('/get', methods=["GET","OPTIONS"])
def home():
    return 'good from backend'