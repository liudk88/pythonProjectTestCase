#!python
# encoding: utf-8
import requests
import common
import time


testData=common.getData()

def getTodoTaskId(headers):
    url = common.getUrl("/view/FView20221Q0V7XZK002/view?FLOW_SEQ="+testData['testResource_flowSeq'])
    req=requests.get(url=url,headers=headers)
    # print(req.text)
    assert len(req.json()['data']['datas']) == 1,'查询任务结果为空'
    return req.json()['data']['datas'][0]['WTASK_ID']

def todo(username,currentStepName,dealFormData):
    time.sleep(testData['timeSleep'])
    print("当前流程环节:"+currentStepName+"，"+username+" to do!")
    headers=common.login(username,"SGN4YTIwMTkh")
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
        "bsForm": {"formId": "Form20221U0P5KWR002"}
    }
    data['dlForm'].update(dealFormData);
    req=requests.post(url=url,json=data,headers=headers)
    # print(req.text)
    data=req.json()
    if data['code'] == 0:
        print(username+' success to do!')
    else:
        print(username+' fail to do!')

# 测试资源发放时，徐工需要补充信息系统信息
sysname=common.getNewSysName()


todo("xiangdk","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "serverGrant"})
todo("zhongxq","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "serverGrant"})
todo("xuyl","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "serverGrant"})
# todo("xuyl","服务器资源发放",{"DEAL_OPT":"服务器资源已发放","nextStep": "dbGrant","REAL_SYS_NAME": sysname,"SYS_TYPE": "1"})

# 测试有生成信息系统，当前只验证存在即可
sysData=common.getSystemByName(sysname)
# 正式资源申请的时候测试自动带出
dbname=common.getNewDbName()

# todo("zhongxq","数据库资源发放",{"DEAL_OPT":"数据库资源已发放","nextStep": "appGrant","DB_USER":dbname})
# todo("xiangdk","应用资源发放",{"DEAL_OPT":"应用资源已发放","nextStep": "nodeConfirm"})
# todo("liudk","资源确认",{"DEAL_OPT":"确认成功","nextStep": "endEvent"})


















