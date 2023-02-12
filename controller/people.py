from flask import Blueprint, request, Response
from model import peopleModel
import json
# from coder import MyEncoder
from flask import app
from model.db import mongo

from .util import checkParm, ret

peopleProfile = Blueprint("people", __name__, url_prefix="/people")

@peopleProfile.route("/show", methods=["GET"])
def get():
    data = peopleModel.getpeople()
    print((data))
    print(type(data))
    result = {"success": False, "data": data}
    return ret(result)



# @peopleProfile.route("/add", methods=["POST"])
# def add(name,gender,birth,height,weight):
#     data = {"name":name,"gender":gender,"birth":birth,"height":height,"weight":weight}
#     print((data))
#     result = {"success": False, "data": data}
#     peopleModel.addpeople(data)

@peopleProfile.route("/add", methods=["POST"])
def add():
    content = request.json
    print(content)
    name = content["name"]
    gender = content["gender"]
    birth = content["birth"]
    height = content["height"]
    weight = content["weight"]
    data = peopleModel.addpeople(name, gender, birth, height, weight)
    print((data))
    result = {"success": False, "data": data}
    return ret(result)