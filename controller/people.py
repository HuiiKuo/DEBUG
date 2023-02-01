from flask import Blueprint, request, Response
from model import peopleModel
import json
# from coder import MyEncoder
from flask import app
from model.db import mongo

from .util import checkParm, ret

peopleProfile = Blueprint("people", __name__, url_prefix="/people")

@peopleProfile.route("/show", methods=["GET"])
def getpeople():
    # content = request.json
    # account = content['account']
    # password = content["password"]
    data = peopleModel.get()
    # print((data))
    result = {"success": False, "data": data}
    # if len(data) == 1:
    #     result["mes"] = "登入成功"
    #     result["success"] = True
    # elif len(data) == 0:
    #     result["mes"] = "登入失敗"
    # else:
    #     result["mes"] = "登入異常"
    return result