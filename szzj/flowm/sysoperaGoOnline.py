#  ===> 系统上线申请 <===
import sys
sys.path.append("../..")
import common as c
import login
import time
import task
from FunClass import FunClass

print('==> test goOnLine <===')
# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="10"
funList=[]
funList.append(FunClass("apply","【申请】"))

gt_flowId="2024051700008"

def apply(applyData={}):
    t_sysname="XC-运维管理平台";
    t_assetId="1024620751153528832" #XC-运维管理平台
    t_dbUserId="1024620276719026176" #itom
    t_dealManId="12" #处理人，12是向工
    t_depOrgId="201606051113025150015" #开发单位
    postData={
        "pkv": gt_flowId,
        "MSG_SYSTEM": t_sysname,
        "ASSET_ID": t_assetId,
        "DB_USER": t_dbUserId,
        "TEST_LINK": "https://zjjtest.sz.gov.cn/itom/#/login",
        "TEST_USER_PWD": "admin / szzj@2022",
        "CONTENT": "这是一条测试的“系统上线申请审批”单",
        "DEAL_MAN": t_dealManId,
        "ORGID": t_depOrgId,
        "PACK_TYPE": "manual",
        "CREATOR": "2209154te15h8sz8g27869",
        "SEND_SMS": "0",
        "UPDATE_TYPE": "1",
        "APPER_ACCOUNT": "liudk",
        "FMT_ID": "b2c330f17e6c11ecbb65000c29ac6001",
        "AID": gt_flowId+"FLOWM",

        "assignees": t_dealManId,
        "nextStep": "nodeBAudit",
        "bsFormId": "Form20221Q0V7Z10002",
        "sendSms": "0"
    }
    if len(applyData)>0:
        postData.update(applyData); # 有传入参数，就以传入的为准
    c.ppost("/wf/sysoperaGoOnline/startProcess",postData)

t_commonPwd="SGN4YTIwMTkh"

# def dealWf(username,currentStepName,dealFormData):
def dealWf(username,flowId,dealFormData):
    time.sleep(1)
    # print("当前流程环节:"+currentStepName+"，"+username+" to do!")

    # 以当前请求人登录系统获得登录请求头
    headers=login.getLoginHeader(username,t_commonPwd)
    # wtaskId=task.getTodoTaskId(headers,gt_flowId)
    wtaskId=task.getTodoTaskId(headers,flowId)
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

    req=c.ppost("/wf/task/"+wtaskId+"/complate",data,headers)
    data=req.json()
    if data['code'] == 0:
        print(username+' success to do!')
    else:
        print(username+' fail to do!')

# dealWf("xiangdk","业务部门项目负责人审批",{"DEAL_OPT":"拟同意","nextStep": "nodeAqjc"})
# dealWf("elinkaqsm","安全扫描审批",{"DEAL_OPT":"完成扫描，未发现中高危漏洞","nextStep": "xxx"})
# dealWf("zhongxq","运维部数据库审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# dealWf("xuyl","运维部服务器审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# dealWf("xiangdk","运维部应用审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# dealWf("zhangf","运维部负责人审批",{"DEAL_OPT":"拟同意","nextStep": "nodeHAudit"})
# dealWf("pengxj","城建档案馆馆长审批",{"DEAL_OPT":"同意","nextStep": "serverDeploy"})
# dealWf("zhongxq","数据库部署",{"DEAL_OPT":"数据库已经完成更新","nextStep": "appGrant"})
# dealWf("xiangdk","应用更新",{"DEAL_OPT":"已经更新完成，请检查结果，并确认。","nextStep": "nodeConfirm"})
# dealWf("xuyl","服务器部署",{"DEAL_OPT":"服务器已经部署完成","nextStep": "dbDeploy"})
# dealWf("xiangdk","确认更新结果",{"DEAL_OPT":"上线成功","nextStep": "endEvent"})

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())













