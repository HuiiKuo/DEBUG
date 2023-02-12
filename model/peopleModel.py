import json
from model.util import group
from model.db import mongo

# name,gender,birth,height,weight

def getpeople():
    return list(mongo.db.people.find({},{"_id":0}))

def addpeople(name,gender,birth,height,weight):
    return list(mongo.db.people.insert_one({"name":name,"gender":gender,"birth":birth,"height":height,"weight":weight}))

