#!python
# encoding: utf-8
import requests
import common
import time


testData=common.getData()

def getTodoTaskId(headers):
    url = common.getUrl("/view/FView20221Q0V7XZK002/view?FLOW_SEQ="+testData['resource_flowSeq'])
    req=requests.get(url=url,headers=headers,verify = False)
    # print(req.text)
    assert len(req.json()['data']['datas']) > 0,'查询任务结果为空'
    return req.json()['data']['datas'][0]['WTASK_ID']

def todo(username,currentStepName,dealFormData):
    time.sleep(testData['timeSleep'])
    print("当前流程环节:"+currentStepName+"，"+username+" to do!")
    headers=common.login(username,common.commonPwd)
    wtaskId=getTodoTaskId(headers)
    # print(wtaskId)
    url = common.getUrl("/wf/task/"+wtaskId+"/complate")
    data = {
        "dlForm": {
            "DEAL_OPT": "",
            "AID": "",
            "assignees": "",
            "nextStep": "",
            "sendSms": "0",
            "formId": "Form20226Q0V7Z10001"
        },
        "bsForm": {"formId": "Form20221U0PXKMY004"}
    }
    data['dlForm'].update(dealFormData);
    req=requests.post(url=url,json=data,headers=headers,verify = False)
    # print(req.text)
    data=req.json()
    if data['code'] == 0:
        print(username+' success to do!')
    else:
        print(username+' fail to do!')

# 正式资源申请需要补充数据库用户信息
dbname=common.getNewDbName()

todo("xiangdk","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
todo("zhongxq","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
todo("xuyl","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
todo("zhangf","运维部领导审批",{"DEAL_OPT":"符合规范，拟同意","nextStep": "serverGrant"})
todo("xuyl","服务器资源发放",{"DEAL_OPT":"服务器资源已发放","nextStep": "dbGrant"})
todo("zhongxq","数据库资源发放",{"DEAL_OPT":"数据库资源已发放","nextStep": "appGrant","PORT": 5236,"UNAME":dbname,"PASSWORD":"szzj@2022","DATABASE_TYPE":"1","DBNAME":"itom","IP":"192.168.99.109","CONNECTION_STRING":"testSqlStr"})
todo("xiangdk","应用资源发放",{"DEAL_OPT":"应用资源已发放","nextStep": "nodeConfirm"})
todo("liudk","资源确认",{"DEAL_OPT":"确认成功","nextStep": "endEvent"})

















