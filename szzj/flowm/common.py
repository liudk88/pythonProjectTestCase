# encoding: utf-8
import json
import requests
import time
import os

headers={}

def getData():
    with open('./data.json','r') as fp:
        return json.load(fp)

testData=getData()

def getUrl(uri):
    global headers
    headers = {
        "Authorization":testData['liudk_access_token']
    }
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
    req=requests.get(url=url,headers=headers)
    assert len(req.json()['data']['datas'])==1,('没有找到信息系统:'+sysname)
    return req.json()['data']['datas'][0]

def getDbByName(dbname):
    headers=login("admin","SGN4YTIwMTkh")
    url = getUrl("/view/AssetView-DS/view?flag=1&UNAME="+dbname)
    req=requests.get(url=url,headers=headers)
    assert len(req.json()['data']['datas'])==1,('没有找到数据库密码簿:'+dbname)
    return req.json()['data']['datas'][0]

# 根据当前测试资源申请生成新的信息系统名称
def getNewSysName():
    return "ldktestSys_"+testData['testResource_flowSeq']

# 根据当前正式资源申请生成新的数据库用户
def getNewDbName():
    return "ldktestDb_"+testData['resource_flowSeq']

#查询待办任务
def getTodoTaskId(headers,flowmSeqKey):
    url = getUrl("/view/FView20221Q0V7XZK002/view?FLOW_SEQ="+testData[flowmSeqKey])
    req=requests.get(url=url,headers=headers)
    # print(req.text)
    assert len(req.json()['data']['datas']) == 1,'查询任务结果为空'
    return req.json()['data']['datas'][0]['WTASK_ID']

def todo(username,currentStepName,flowmSeqKey,bsFormId,dealFormData):
    time.sleep(testData['timeSleep'])
    print("当前流程环节:"+currentStepName+"，"+username+" to do!")
    headers=login(username,"SGN4YTIwMTkh")
    wtaskId=getTodoTaskId(headers,flowmSeqKey)
    # print(wtaskId)
    url = getUrl("/wf/task/"+wtaskId+"/complate")
    data = {
        "dlForm": {
            "DEAL_OPT": "",
            "AID": "",
            "assignees": "",
            "nextStep": "",
            "sendSms": "0",
            "formId": "Form20226Q0V7Z10001"
        },
        "bsForm": {"formId": bsFormId}
    }
    data['dlForm'].update(dealFormData);
    req=requests.post(url=url,json=data,headers=headers)
    # print(req.text)
    data=req.json()
    if data['code'] == 0:
        print(username+' success to do!')
    else:
        print(username+' fail to do!')

# 为新系统建立新的应用服务器
def createApplaySystem(createUserId,systemId):
    url = getUrl("/form/AssetForm-AS")
    data = {
        "INFORMATION_SYSTEM": systemId,
        "IP": "10.224.198.202",
        "CONSOLE_USER_NAME": "app",
        "PASSWORD": "Hcxa2019!",
        "APPLICATION_LIST": "itom,nisg,esg",
        "ASSET_TYPE": "AS",
        "ASSET_TYPEH": "AS"
    }
    headers=login(createUserId,"SGN4YTIwMTkh")
    # !!! 如果是从测试资源开始申请，打开
    req=requests.post(url=url,json=data,headers=headers)

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

# 提交数据库更新申请
def post_db_update_applay(flowSeq,sysname,systemId,dbUser,fileToken):
    data = {
        "pkv": flowSeq,
        "MSG_SYSTEM": sysname,
        "ASSET_ID": systemId,
        "DB_USER": dbUser,
        "CONTENT": "这是一条测试的“数据库更新审批”单",
        "DEAL_MAN": "12",
        "ORGID": "201606051113025150015",
        "CREATOR": "2209154te15h8sz8g27869",
        "SEND_SMS": "0",
        "FMT_ID": "b2c330f17e6c11ecbb65000c29ac6003",
        "AID": fileToken,
        "assignees": "12",
        "nextStep": "nodeBaudit",
        "bsFormId": "Form20221U0MPA52001",
        "sendSms": "0"
    }
    post_applay("sysoperaDbUpdate",data)

# 提交应用更新申请
def post_app_update_applay(flowSeq,sysname,systemId,projectName,fileToken):
    data = {
        "pkv": flowSeq,
        "MSG_SYSTEM": sysname,
        "ASSET_ID": systemId,
        "PROJECT_NAME": projectName,
        "TEST_LINK": "https://zjjtest.sz.gov.cn/itom/#/login",
        "TEST_USER_PWD": "admin / szzj@2022",
        "CONTENT": "这是一条测试的“应用更新审批”单",
        "DEAL_MAN": "12",
        "ORGID": "201606051113025150015",
        "PACK_TYPE": "manual",
        "CREATOR": "2209154te15h8sz8g27869",
        "SEND_SMS": "0",
        "UPDATE_TYPE": "1",
        "APPER_ACCOUNT": "liudk",
        "FMT_ID": "b2c330f17e6c11ecbb65000c29ac6006",
        "AID": fileToken,
        "assignees": "12",
        "nextStep": "nodeBAudit",
        "bsFormId": "Form20221Q0V7Z10002",
        "sendSms": "0"
    }
    post_applay("sysoperaUpdate",data)

def post_applay(modkey,postData):
    url = getUrl("/wf/"+modkey+"/startProcess")
    req=requests.post(url=url,json=postData,headers=headers)
    print(req.text)
    data=req.json()
    if data['code'] == 0:
        print('test success!')
    else:
        print('test fail!')