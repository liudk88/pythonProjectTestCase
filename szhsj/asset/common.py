# encoding: utf-8
import json
import requests
import time
import os
import random

headers={}

def getData():
    with open('./data.json','r') as fp:
        return json.load(fp)

testData=getData()

def getVals(valArr,numberOfTimes):
    result=[]
    for i in range(numberOfTimes):
        index=random.randint(0,len(valArr)-1)
        val=valArr[index]
        if val not in result:
            result.append(val);
    result.sort()
    return result

def getRandomVals(valArr):
    numberOfTimes=random.randint(0, len(valArr))
    return getVals(valArr,numberOfTimes)

def getRandomValsStr(valArr):
    numberOfTimes=random.randint(0, len(valArr))
    result=getVals(valArr,numberOfTimes)
    return ','.join(str(i) for i in result)

def getSingleVal(valArr):
    return getVals(valArr,1)[0]

def getUrl(uri):
    return testData['domain']+uri

def login(username,password):
    url = getUrl("/login/login")
    data = {
        "username": username,
        "password": password,
        "remember": "true",
        "key":"d8a49423-47dd-4dc8-97b0-22cbc0796266"
    }
    req=requests.post(url=url,json=data,verify = False)
    access_token=req.json()['data']['access_token']
    headers = {"Authorization":access_token}
    return headers

def getSystemByName(sysname):
    headers=login("admin","SGN4YTIwMTkh")
    url = getUrl("/view/AssetView-BS/view?flag=1&SYS_NAME="+sysname)
    req=requests.get(url=url,headers=headers,verify = False)
    assert len(req.json()['data']['datas'])==1,('没有找到信息系统:'+sysname)
    return req.json()['data']['datas'][0]

# charset参数可以限制文件编码格式
def post_file_request(url,fileToken,file_path):
    url=getUrl(url)
    data={"fileToken":fileToken}
    if os.path.exists(file_path):
        if url not in [None, ""]:
            if url.startswith("http") or url.startswith("https"):
                files = {'file': open(file_path, 'rb')}
                res = requests.post(url,headers=headers, files=files, data=data)
                return {"code": 0, "res": res}

def down_file(url,params,fileName):
    url=getUrl(url)
    req=requests.get(url=url,params=params,headers=headers,verify = False)
    with open(fileName, "wb") as code:
        code.write(req.content)

def post_asset(assetType,postData):
    url = getUrl("/form/AssetForm-"+assetType)
    req=requests.post(url=url,json=postData,headers=headers)
    print(req.text)
    data=req.json()
    if data['code'] == 0:
        print('test success!')
    else:
        print('test fail!')