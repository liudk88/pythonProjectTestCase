import config as g
import common as c
import requests

import sys

#用来做用户登录，不同项目登录地址、返回对接解析可能都不一样，同一个项目，也有可能通过变化登录用户获取请求头

args=sys.argv[1:]
# 指定登录的项目
project=''
if len(args)>0:
    project=args[0]

logurl="/login/login"
loginPostData={}

def getHeader(logurl='/login/login',username='',loginData={}):
    print("=> login into system! (account = "+username+") (logurl = "+logurl+")")
    return requests.post(g.domain + logurl,json=loginData,verify = False)

if project == 'dhhk':
    logurl="/login"
    loginPostData = {"username":"admin","password":"admin123"}
elif project == 'dhhk_sms':
    # username="A02950"
    # username="admin"
    username="sqr" #申请人
    # username="A03383" #申请人
    # username="zrb_zb-jl" #责任部门值班经理
    # username="zrb_aj-jl" #责任部门安质经理
    # username="anjianzhiban" #安监值班
    # username="A00372" #安监监察员
    # username="A01933" #安监副总/安全总监
    logurl="/auth/login?username="+username+"&password=111111&code=1&uuid=&loginType=1"
    # loginPostData = {"username":username,"password":"111111","uuid":"1305c8ab-95ce-4a3c-9283-baee2b35f28c"}
    loginPostData = {}
    print("=> login into system! (account = "+username+") (logurl = "+logurl+")")
elif project == 'ynwxb' or project == 'szzj':
    # uname="admin"
    uname="liudk"
    # uname="kmAdmin"
    loginPostData = {"username":uname,"password":"SGN4YTIwMTkh"}
else:
    # admin
    # username="SckY4x8ZKcXREQLYphA63UfVxg8C+b51BXNqyOSuSBF/OGbrqxrJT56ZOrivquf8HqWooqhbLzESZNFN2bUQdQgLRroUYep1hfFj3eGj2GRxRYEAWLZ58zT3DEfeRo1jYi+UBSJsncRBoDpIHQA4fkgTAFqxWXvpcfuvCn/gOn4="
    # zhengquanjun2
    # username="jIqGjdYdDjUHMxxgGazgOsCfUcjElGEnhDJ/Uv647frb9dapJos9PAKRqab2QcIkqxKSaZt4kjHaPDY5yN68uMT6HUn6bTsz3qdAw8fAu6aGrTyGgG8YRdHsbmLCRo1oHzjuUUhJ92JjaLD2uyRos7kBQjPsRbWKJg+dYu5zXnE="
    # 坪山 杨涛 sec_yangtao
    username="W2nRLE7cOluk0ZikhsIpIlSMT92WfzWlTUTQvDBpKHoeUcfDYooW7RqZ0zYJhk2vaGXIkB8l03qIWCluBLHGobCbc9QuYpOgjHOPmFWF5XYLlG4kL6wDgqYG0x2480zYh70BpFCaWi+sSVSCChQFGbHkH8tigu2S9ySwX182WVU="
    password="cdD4jBcXaI0GAuqik10zdnEpi7ZGDDYMXjNNleRb4TRoJkaTAhjkLfgnXI6XUWKGfMR124fYDDBE0rOw8yZzNSDxWtwDhd+O0fYt+v5XdkK8iHRXC5G6m6YHbGTGDZRO2GyzKaIdK1INUa1ZM0ZFcEOcPp7Hi7BCXSnYTe8oj5E="
    loginPostData = {"username":username,"password":password}


def login(loginData,pname=project):
    # print("=========="+pname)
    # print("=> login into system! (account = "+loginData['username']+")")
    req=requests.post(g.domain + logurl,json=loginData,verify = False)
    print(req)
    c.jprint(req.json())
    access_token=''
    if project == 'dhhk':
        access_token="Bearer "+req.json()['token']
    elif project == 'dhhk_sms':
        access_token="Bearer "+req.json()['data']
    else:
        access_token=req.json()['data']['access_token']
    return access_token

# 获取指定用户的请求头
def getLoginHeader(username,password,pname=project):
    token=login({"username":username,"password":password},pname)
    return {"Authorization":token}


if __name__ == "__main__":  #直接运行文件时执行（如果文件是被导入到其他文件中，`__name__`将被设置为文件名）
    access_token=login(loginPostData)
    c.put('config.py','access_token',access_token) #更新全局令牌，方便在后面的请求中带上token
