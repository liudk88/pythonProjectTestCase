#  ===> 应用更新流程 <===
import flowm
import sys
sys.path.append("../..")
import common as c

print('==> 调试 应用更新流程 <===')

testData=flowm.getData()
gt_flowId=testData['update_flowSeq']
gt_csflowId=testData['testResource_flowSeq']
gt_newSysName="ldktestSys_"+gt_csflowId #根据当前测试资源申请生成新的信息系统名称


def getSystemByName(sysname):
    req=c.get("/view/AssetView-BS/view?flag=1&SYS_NAME="+sysname)
    assert len(req.json()['data']['datas'])==1,('没有找到信息系统:'+sysname)
    return req.json()['data']['datas'][0]


# 提交应用更新申请
def apply(flowSeq,sysname,systemId,projectName,fileToken):
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
        "sendSms": "1"
    }
    c.ppost("/wf/sysoperaUpdate/startProcess",data)

def dealWf(username,currentStepName,dealFormData):
    flowm.dealWf(username,currentStepName,gt_flowId,"Form20221Q0V7Z10002",dealFormData)

# 上传系统更新包
# projectName="nisg"
# fileToken=gt_flowId+"FLOWM"
# files = {'file': open(projectName+".zip", 'rb')}
# c.post_file_req("/attachment/upload",files,{"fileToken":fileToken})

# <=  应用更新申请  =>
# apply(gt_flowId,"XC-运维管理平台","1024620751153528832","nisg",gt_flowId+"FLOWM")


#  <=  流程处理  =>
# dealWf("xiangdk","业务主管部门审批",{"DEAL_OPT":"拟同意","nextStep": "nodeAqjc"})
# dealWf("elinkaqsm","安全检查",{"DEAL_OPT":"完成扫描，未发现中高危漏洞","nextStep": "nodeSAudit","sendSms": "1"})

## ==============
# dealWf("xiangdk","运维部人员审批",{"DEAL_OPT":"所上传文件符合规范","nextStep": "nodeChargeAudit"})  ## 可以测试其他应用管理员“余豪”也能处理
## ----发送给“服务器管理员审批”
# dealWf("xiangdk","运维部人员审批",{"DEAL_OPT":"所上传文件符合规范","nextStep": "serverAudit"})
# dealWf("xuyl","服务器管理员审批",{"DEAL_OPT":"拟同意","nextStep": "nodeChargeAudit"})
## ==============

# dealWf("zhangf","运维部负责人审批",{"DEAL_OPT":"符合规范，拟同意，呈彭馆示","nextStep": "nodeHAudit"})
# dealWf("pengxj","馆领导审批",{"DEAL_OPT":"同意","nextStep": "nodeUpdate"})

## ==============
dealWf("xiangdk","系统更新部署",{"DEAL_OPT":"已经更新完成，请检查结果，并确认。","nextStep": "nodeConfirm"})
## ----
# dealWf("xiangdk","系统更新部署",{"DEAL_OPT":"应用更新完成，请检查结果，并确认，转发给服务器管理员。","nextStep": "serverConfig"})
# dealWf("xuyl","系统更新部署",{"DEAL_OPT":"服务器配置更新完成，请检查结果。","nextStep": "nodeConfirm"})
## ==============

# dealWf("liudk","确认更新结果",{"DEAL_OPT":"确认更新成功","nextStep": "endEvent"})






















