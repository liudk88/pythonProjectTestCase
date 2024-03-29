#!python
# encoding: utf-8
import requests
import common
import time


testData=common.getData()

def getTodoTaskId(headers):
    url = common.getUrl("/view/FView20221Q0V7XZK002/view?FLOW_SEQ="+testData['goOnline_flowSeq'])
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
        "bsForm": {"formId": "Form20221Q0V7Z10002"}
    }
    data['dlForm'].update(dealFormData);
    req=requests.post(url=url,json=data,headers=headers,verify = False)
    # print(req.text)
    data=req.json()
    if data['code'] == 0:
        print(username+' success to do!')
    else:
        print(username+' fail to do!')

print('==> test 系统上线申请 审批 <===')
# v202402 拆分审批环节，余豪（yuh）分三个角色处理
todo("xiangdk","业务部门项目负责人审批",{"DEAL_OPT":"拟同意","nextStep": "nodeAqjc"})
todo("elinkaqsm","安全扫描审批",{"DEAL_OPT":"完成扫描，未发现中高危漏洞","nextStep": "xxx"})
todo("zhongxq","运维部数据库审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
todo("xuyl","运维部服务器审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
todo("xiangdk","运维部应用审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
todo("zhangf","运维部负责人审批",{"DEAL_OPT":"拟同意","nextStep": "nodeHAudit"})
todo("pengxj","城建档案馆馆长审批",{"DEAL_OPT":"同意","nextStep": "serverDeploy"})
todo("zhongxq","数据库部署",{"DEAL_OPT":"数据库已经完成更新","nextStep": "appGrant"})
todo("xiangdk","应用更新",{"DEAL_OPT":"已经更新完成，请检查结果，并确认。","nextStep": "nodeConfirm"})
todo("xuyl","服务器部署",{"DEAL_OPT":"服务器已经部署完成","nextStep": "dbDeploy"})
todo("xiangdk","确认更新结果",{"DEAL_OPT":"上线成功","nextStep": "endEvent"})

# v0
# todo("xiangdk","业务部门项目负责人审批",{"DEAL_OPT":"拟同意","nextStep": "nodeAqjc"})
# todo("elinkaqsm","安全扫描审批",{"DEAL_OPT":"完成扫描，未发现中高危漏洞","nextStep": "nodeSAudit"})
# todo("zhongxq","运维部人员审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# todo("xuyl","运维部人员审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# todo("xiangdk","运维部人员审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# todo("zhangf","运维部负责人审批",{"DEAL_OPT":"拟同意","nextStep": "nodeHAudit"})
# todo("pengxj","馆领导审批",{"DEAL_OPT":"同意","nextStep": "nodeDeploy"})
# todo("xiangdk","应用更新",{"DEAL_OPT":"已经更新完成，请检查结果，并确认。","nextStep": "nodeConfirm"})
# todo("xuyl","应用更新",{"DEAL_OPT":"已经更新完成","nextStep": "nodeConfirm"})
# todo("zhongxq","应用更新",{"DEAL_OPT":"数据库已经完成更新","nextStep": "nodeConfirm"})
# todo("xiangdk","确认更新结果",{"DEAL_OPT":"上线成功","nextStep": "endEvent"})
















