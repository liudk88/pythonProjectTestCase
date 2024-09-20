#  ===> 流程任务 <===
import sys
sys.path.append("../..")
import common as c
import json
import login
import time

def getHeader(username):
    logurl="/login/login"
    # 以当前请求人登录系统获得登录请求头
    req=login.getHeader(logurl,username,{"username":username,"password":"SGN4YTIwMTkh"})
    return {"Authorization":req.json()['data']}

#获取自定用户、指定流程id的任务
def getTodoTaskId(headers,flowId):
    req = c.get("/sysOperaView/FView20221Q0V7XZK002/view?FLOW_SEQ="+flowId,headers=headers)
    print(req.json()['data']['datas'])
    assert len(req.json()['data']['datas']) > 0,'查询任务结果为空'
    return req.json()['data']['datas'][0]['WTASK_ID']

def getData():
    with open('./data.json','r') as fp:
        return json.load(fp)

testData=getData()
t_commonPwd="SGN4YTIwMTkh"

# 处理流程，可以通过dealFormData更新提交表单
def dealWf(username,currentStepName,flowId,bsFormId,dealFormData):
    time.sleep(testData['timeSleep'])
    print("当前流程环节:"+currentStepName+"，"+username+" to do!")
    # 以当前请求人登录系统获得登录请求头
    headers=login.getLoginHeader(username,t_commonPwd)

    wtaskId=getTodoTaskId(headers,flowId)
    # 默认提交的表单
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

    req=c.ppost("/wf/task/"+wtaskId+"/complate",data,headers)
    data=req.json()
    if data['code'] == 0:
        print(username+' success to do!')
    else:
        print(username+' fail to do!')


