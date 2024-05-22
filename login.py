import config as g
import common as c
import requests

import sys
args=sys.argv[1:]
# 指定登录的项目
project=''
if len(args)>0:
    project=args[0]

def getLoginPostData():
    if project == 'ynwxb' or project == 'szzj':
        # uname="admin"
        uname="liudk"
        # uname="kmAdmin"
        return {"username":uname,"password":"SGN4YTIwMTkh"}
    else:
        # admin
        username="SckY4x8ZKcXREQLYphA63UfVxg8C+b51BXNqyOSuSBF/OGbrqxrJT56ZOrivquf8HqWooqhbLzESZNFN2bUQdQgLRroUYep1hfFj3eGj2GRxRYEAWLZ58zT3DEfeRo1jYi+UBSJsncRBoDpIHQA4fkgTAFqxWXvpcfuvCn/gOn4="
        # zhengquanjun2
        # username="jIqGjdYdDjUHMxxgGazgOsCfUcjElGEnhDJ/Uv647frb9dapJos9PAKRqab2QcIkqxKSaZt4kjHaPDY5yN68uMT6HUn6bTsz3qdAw8fAu6aGrTyGgG8YRdHsbmLCRo1oHzjuUUhJ92JjaLD2uyRos7kBQjPsRbWKJg+dYu5zXnE="
        password="cdD4jBcXaI0GAuqik10zdnEpi7ZGDDYMXjNNleRb4TRoJkaTAhjkLfgnXI6XUWKGfMR124fYDDBE0rOw8yZzNSDxWtwDhd+O0fYt+v5XdkK8iHRXC5G6m6YHbGTGDZRO2GyzKaIdK1INUa1ZM0ZFcEOcPp7Hi7BCXSnYTe8oj5E="
        return {"username":username,"password":password}

def login(loginData):
    print("=> login into system! (account = "+loginData['username']+")")
    req=requests.post(g.domain + "/login/login",json=loginData,verify = False)
    c.jprint(req.json())
    access_token=req.json()['data']['access_token']
    return access_token

# 获取指定用户的请求头
def getLoginHeader(username,password):
    token=login({"username":username,"password":password})
    return {"Authorization":token}


if __name__ == "__main__":  #直接运行文件时执行（如果文件是被导入到其他文件中，`__name__`将被设置为文件名）
    access_token=login(getLoginPostData())
    c.put('config.py','access_token',access_token) #更新全局令牌，方便在后面的请求中带上token
