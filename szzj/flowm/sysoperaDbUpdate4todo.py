#!python
# encoding: utf-8
import common

testData=common.getData()

def todo(username,currentStepName,dealFormData):
    common.todo(username,currentStepName,"dbUpdate_flowSeq","Form20221U0MPA52001",dealFormData)

print('==> test 系统上线申请 审批 <===')

todo("xiangdk","业务主管部门审批",{"DEAL_OPT":"拟同意","nextStep": "nodeSqlAudit"})
todo("zhongxq","sql审核",{"DEAL_OPT":"语句符合规范","nextStep": "nodeSaudit"})
todo("zhangf","运维部负责人审批",{"DEAL_OPT":"符合规范，拟同意，呈彭馆示","nextStep": "nodeHAudit"})
todo("pengxj","馆领导审批",{"DEAL_OPT":"同意","nextStep": "nodeSupdate"})
todo("zhongxq","运维部更新",{"DEAL_OPT":"语句执行成功","nextStep": "endEvent"})



















