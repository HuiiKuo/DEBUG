import json
from model.util import group
from model.db import mongo

# name,gender,birth,height,weight

def getpeople():
    return list(mongo.db.people.find())

