from flask import Blueprint, request, Response
from model import userModel
import json
# from coder import MyEncoder
from flask import app
from model.db import mongo

from .util import checkParm, ret

userProfile = Blueprint("user", __name__, url_prefix="/user")


@userProfile.route("/login", methods=["POST"])
def login():
    content = request.json
    account = content['account']
    password = content["password"]
    data = userModel.login(account, password)
    print((data))
    result = {"success": False, "data": data}
    if len(data) == 1:
        result["mes"] = "登入成功"
        result["success"] = True
    elif len(data) == 0:
        result["mes"] = "登入失敗"
    else:
        result["mes"] = "登入異常"
    return ret(result)


@userProfile.route("/sign", methods=["POST"])
def sign():
    content = request.json
    cond = ["account", "password", "age", "sex",
            "areaid", "name", "degree", "phone"]
    result = {"success": False, "mes": ""}
    t = checkParm(cond, content)

    if(isinstance(t, dict)):
        data = userModel.sign(t["account"], t["password"],
                              t["age"], t["sex"], t["areaid"], t["name"], t["degree"], t["phone"])
        if(data["success"]):
            result["mes"] = "註冊成功"
            result["success"] = True
        else:
            hasUser = userModel.hasUser(t["account"])["data"][0]["c"]
            if hasUser > 0:
                result["mes"] = f"註冊異常 - 重複帳號"
            else:
                result["mes"] = "註冊異常"

    else:
        result["mes"] = "請填畢所有資料"
    return ret(result)


@userProfile.route("/<u_id>", methods=["GET"])
def getUser(u_id):
    return ret(userModel.user(u_id))


@userProfile.route("/", methods=["POST"])
def user():
    content = request.json
    return ret(userModel.user(content["user_id"]))


@userProfile.route("/psw", methods=["POST"])
def edit():
    content = request.json
    print(content)
    cond = ["account", "oldPassword", "password", "passwordConfire"]
    result = {"success": False, "mes": ""}
    t = checkParm(cond, content)

    if(isinstance(t, dict)):
        oldPasswordFromDB = userModel.findPasswordByAccount(
            content["account"], t["oldPassword"])
        print(oldPasswordFromDB)
        if(oldPasswordFromDB["success"]):
            oldPasswordFromDB = oldPasswordFromDB["data"]
            if(len(oldPasswordFromDB) > 0):
                if(content["password"] != content["passwordConfire"]):
                    result["mes"] += "密碼和確認密碼不同\n"
                if(result["mes"] == ""):
                    data = userModel.changePassword(
                        content["account"], content["password"])
                    result["mes"] = "更換密碼成功"
                    result["success"] = True
                    result["data"] = data
            elif(len(oldPasswordFromDB) == 0):
                result["mes"] = "輸入舊密碼錯誤"
            else:
                result["mes"] = "帳號異常"
    return ret(result)


@userProfile.route("/", methods=["PATCH"])
def changeProfile():
    content = request.json
    account = content["account"]
    cond = ["area_id", "name"]
    data = {}
    for i in cond:
        if(i in content.keys()):
            data[i] = content[i]
    data = userModel.changeProfile(data, account)
    result = {"success": False, "mes": "修改異常", "data": data}
    if(data["success"]):
        result["success"] = True
        result["mes"] = "修改成功"
    return ret(result)



    