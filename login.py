import config as g
import common as c
import sys
args=sys.argv[1:]
# 指定登录的项目
project=''
if len(args)>0:
    project=args[0]

def getLoginPostData():
    if project == 'ynwxb':
        uname="admin"
        # uname="kmAdmin"
        return {"username":uname,"password":"SGN4YTIwMTkh"}
    else:
        username="SckY4x8ZKcXREQLYphA63UfVxg8C+b51BXNqyOSuSBF/OGbrqxrJT56ZOrivquf8HqWooqhbLzESZNFN2bUQdQgLRroUYep1hfFj3eGj2GRxRYEAWLZ58zT3DEfeRo1jYi+UBSJsncRBoDpIHQA4fkgTAFqxWXvpcfuvCn/gOn4="
        password="cdD4jBcXaI0GAuqik10zdnEpi7ZGDDYMXjNNleRb4TRoJkaTAhjkLfgnXI6XUWKGfMR124fYDDBE0rOw8yZzNSDxWtwDhd+O0fYt+v5XdkK8iHRXC5G6m6YHbGTGDZRO2GyzKaIdK1INUa1ZM0ZFcEOcPp7Hi7BCXSnYTe8oj5E="
        return {"username":username,"password":password}

def login(loginData):
    print("=> login into system! (account = "+loginData['username']+")")
    req=c.ppost("/login/login",loginData)
    access_token=req.json()['data']['access_token']
    return access_token

username="SckY4x8ZKcXREQLYphA63UfVxg8C+b51BXNqyOSuSBF/OGbrqxrJT56ZOrivquf8HqWooqhbLzESZNFN2bUQdQgLRroUYep1hfFj3eGj2GRxRYEAWLZ58zT3DEfeRo1jYi+UBSJsncRBoDpIHQA4fkgTAFqxWXvpcfuvCn/gOn4="
password="cdD4jBcXaI0GAuqik10zdnEpi7ZGDDYMXjNNleRb4TRoJkaTAhjkLfgnXI6XUWKGfMR124fYDDBE0rOw8yZzNSDxWtwDhd+O0fYt+v5XdkK8iHRXC5G6m6YHbGTGDZRO2GyzKaIdK1INUa1ZM0ZFcEOcPp7Hi7BCXSnYTe8oj5E="
access_token=login(getLoginPostData())

#update access_token
# g.put("access_token",access_token)
c.put('config.py','access_token',access_token)
