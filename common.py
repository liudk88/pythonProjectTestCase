# encoding: utf-8
import config as g
import json
import requests
import time
import os
import random
import sys
import re

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
    req=requests.get(url=url,params=params,headers=headers)
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


# ============= 20240314 add =============

headers = {"Authorization":g.access_token}

mdTdLen=15

def get_len(string: str):
    """
    获取字符串的长度, 中文是两个字符, 英文是一个字符
    :param string:
    :return:
    """
    length = 0
    for ch in string:
        if '\u4e00' <= ch <= '\u9fa5':  # 是中文字符
            length += 2
        else:
            length += 1
    return length

# 把字符串全部转换为“-”
def repalceToFg(str):
    pattern = "."
    return re.sub(pattern,"-",str)

# 把数组按模板右补充空格
def ljust(arr,templateLens):
    i=0
    rarr=[];
    for key in arr:
        key=key.ljust(templateLens[i]," ")
        rarr.append(key)
        i=i+1

    return rarr
#用竖线分隔符打印数组
def printArrWithFg(arr):
    synx=" | "
    arrlen=len(arr)
    parr=arr[0:mdTdLen]
    str_arr=synx.join(parr)
    str_arr="| "+str_arr+" |"
    if arrlen > mdTdLen:
        str_arr=str_arr + "······ |"
    print(str_arr)

def printTable(jobj,printTitle,level):
    colLen={}
    title=[]
    fgs=[]
    valStrs=[]
    i=0
    objs={}
    for key, value in jobj.items():
        title.append(key)
        n=get_len(key)
        if type(value) != dict and type(value) != list:
            s=str(value)
            valStrs.append(s)
            if n < get_len(s):
                n = get_len(s)
        else:
            if type(value) == dict:
                valStrs.append("{}")
            else:
                valStrs.append("[]")

            objs[key]=value
        colLen[i]=n
        i=i+1


    title=ljust(title,colLen)
    valStrs=ljust(valStrs,colLen)

    for key in title:
        fgs.append(repalceToFg(key))

    if printTitle == '1':
        printArrWithFg(title)
        printArrWithFg(fgs)
    printArrWithFg(valStrs)

    for key, value in objs.items():
        print()
        print("# "+key +" L"+str(level))
        if type(value) == dict:
            if len(value)!=0:
                printTable(value,"1",level+1)
        elif type(value) == list:
            pt="1"
            for v in value:
                printTable(v,pt,level+1)
                pt="0"


# -- begin 重新封装get请求
def get(url,params):
    print("请求地址： "+url)
    return requests.get(url=g.domain+url,params=params,headers=headers,verify = False)

def get(url):
    print("请求地址： "+url)
    return requests.get(url=g.domain+url,headers=headers,verify = False)

def post(url,params):
    print("请求地址： "+url)
    return requests.post(url=g.domain+url,json=params,headers=headers,verify = False)
# 以formData的方式提交参数
def postf(url,params):
    return requests.post(url=g.domain+url,data=params,headers=headers,verify = False)

#--
def pget(url,params):
    res=get(url,params)
    jprint(res.json())
    return res

def pget(url):
    res=get(url)
    print("返回信息：")
    jprint(res.json())
    printTable(res.json(),"1",0)
    return res

def ppost(url,params):
    res=post(url,params)
    print("返回信息：")
    jprint(res.json())
    return res

def ppostf(url,params):
    res=postf(url,params)
    print("返回信息：")
    jprint(res.json())
    return res
# -- end
# 获取命令行参数（去掉命令文件名本身）
def args():
    return sys.argv[1:]

# 格式化打印json对象
def jprint(jsonData):
    formatted_json = json.dumps(jsonData, indent=2, ensure_ascii=False)
    print(formatted_json)

# charset参数可以限制文件编码格式
def post_file_req(url,fileDatas,data):
    res = requests.post(g.domain+url,headers=headers, files=fileDatas, data=data)
    print("返回信息：")
    jprint(res.json())
    return res



