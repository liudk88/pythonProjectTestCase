#  ===> 应用更新流程 <===
import flowm
import sys
sys.path.append("../..")
import common as c

print('==> 调试 应用更新流程 <===')

testData=flowm.getData()
gt_flowId=testData['resource_flowSeq']
gt_csflowId=testData['testResource_flowSeq']
# gt_newSysName="ldktestSys_"+gt_csflowId #根据当前测试资源申请生成新的信息系统名称


# 提交应用更新申请  -- 未调整
# def apply(flowSeq,sysname,systemId,projectName,fileToken):
#     data = {
#         "pkv": flowSeq,
#         "MSG_SYSTEM": sysname,
#         "ASSET_ID": systemId,
#         "PROJECT_NAME": projectName,
#         "TEST_LINK": "https://zjjtest.sz.gov.cn/itom/#/login",
#         "TEST_USER_PWD": "admin / szzj@2022",
#         "CONTENT": "这是一条测试的“应用更新审批”单",
#         "DEAL_MAN": "12",
#         "ORGID": "201606051113025150015",
#         "PACK_TYPE": "manual",
#         "CREATOR": "2209154te15h8sz8g27869",
#         "SEND_SMS": "0",
#         "UPDATE_TYPE": "1",
#         "APPER_ACCOUNT": "liudk",
#         "FMT_ID": "b2c330f17e6c11ecbb65000c29ac6006",
#         "AID": fileToken,
#         "assignees": "12",
#         "nextStep": "nodeBAudit",
#         "bsFormId": "Form20221Q0V7Z10002",
#         "sendSms": "1"
#     }
#     c.ppost("/wf/sysoperaUpdate/startProcess",data)

def dealWf(username,currentStepName,dealFormData):
    flowm.dealWf(username,currentStepName,gt_flowId,"Form20221U0PXKMY004",dealFormData)

# 上传系统更新包
# projectName="nisg"
# fileToken=gt_flowId+"FLOWM"
# files = {'file': open(projectName+".zip", 'rb')}
# c.post_file_req("/attachment/upload",files,{"fileToken":fileToken})

# <=  应用更新申请  =>
# apply(gt_flowId,"XC-运维管理平台","1024620751153528832","nisg",gt_flowId+"FLOWM")


#  <=  流程处理  =>
# dealWf("xiangdk","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# dealWf("zhongxq","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# dealWf("xuyl","运维部审批",{"DEAL_OPT":"拟同意","nextStep": "operaLeaderAudit"})
# dealWf("zhangf","运维部领导审批",{"DEAL_OPT":"符合规范，拟同意","nextStep": "serverGrant"})
# dealWf("xuyl","服务器资源发放",{"DEAL_OPT":"服务器资源已发放","nextStep": "dbGrant"})

# dealWf("zhongxq","数据库资源发放",{"DEAL_OPT":"数据库资源已发放","nextStep": "appGrant","PORT": 5236,"UNAME":dbname,"PASSWORD":"szzj@2022","DATABASE_TYPE":"1","DBNAME":"itom","IP":"192.168.99.109","CONNECTION_STRING":"testSqlStr"})
dealWf("zhongxq","数据库资源发放",{"DEAL_OPT":"数据库资源已发放","nextStep": "appGrant"})

dealWf("xiangdk","应用资源发放",{"DEAL_OPT":"应用资源已发放","nextStep": "nodeConfirm"})
dealWf("liudk","资源确认",{"DEAL_OPT":"确认成功","nextStep": "endEvent"})























