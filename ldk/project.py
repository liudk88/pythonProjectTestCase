# encoding: utf-8
import requests
import json

type = input("请输入您需要测试的接口：0：查询（默认）；1：新增；2：修改；3：查看；4：删除")
if type == '':
    type = '0'

projectId="5661809811271680"

def list():
    res=requests.get(url="http://127.0.0.1:8888/project"
                      ,json={}
                      ,verify = False)
    print(res.text)

def add():
    res=requests.post(url="http://127.0.0.1:8888/project/add"
     ,json={"projectName":"testProject",
            "status":"1",
            }
     ,verify = False)
    print(res.text)

def update():
    res=requests.post(url="http://127.0.0.1:8888/project/update"
                      ,json={"projectId":projectId,
                             "projectName":"testProject2",
                             "status":"2",
                             }
                      ,verify = False)
    print(res.text)

def info():
    res=requests.get(url="http://127.0.0.1:8888/project/"+projectId
                      ,json={}
                      ,verify = False)
    print(json.dumps(res.text))

def remove():
    res=requests.get(url="http://127.0.0.1:8888/project/remove/"+projectId
                     ,json={}
                     ,verify = False)
    print(json.dumps(res.text))

if type == '0':
    list()
elif type == '1':
    add()
elif type == '2':
    update()
elif type == '3':
    info()
elif type == '4':
    remove()