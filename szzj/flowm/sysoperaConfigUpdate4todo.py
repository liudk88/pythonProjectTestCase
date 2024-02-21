#!python
# encoding: utf-8
import common

testData=common.getData()

def todo(username,currentStepName,dealFormData):
    common.todo(username,currentStepName,"configUpdate_flowSeq","Form2023BR13NL3R001",dealFormData)

print('==> test 配置更新审批流程 审批 <===')

# todo("xiangdk","业务主管部门审批",{"DEAL_OPT":"拟同意","nextStep": "nodeServerAudit"})
todo("xuyl","服务器管理员审核",{"DEAL_OPT":"拟同意","nextStep": "nodeSaudit"})
todo("zhangf","运维部负责人审批",{"DEAL_OPT":"同意","nextStep": "nodeSupdate"})
todo("xuyl","运维部更新",{"DEAL_OPT":"已按需配置","nextStep": "nodeConfirm"})
todo("liudk","更新结果确认",{"DEAL_OPT":"已确认修复","nextStep": "endEvent"})




















