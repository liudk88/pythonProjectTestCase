#!python
# encoding: utf-8
import common

testData=common.getData()

def todo(username,currentStepName,dealFormData):
    common.todo(username,currentStepName,"update_flowSeq","Form20221Q0V7Z10002",dealFormData)

print('==> test 系统上线申请 审批 <===')

todo("xiangdk","业务主管部门审批",{"DEAL_OPT":"拟同意","nextStep": "nodeAqjc"})
todo("elinkaqsm","安全检查",{"DEAL_OPT":"完成扫描，未发现中高危漏洞","nextStep": "nodeSAudit"})

# 发送给“运维部负责人审批”
# todo("xiangdk","运维部人员审批",{"DEAL_OPT":"所上传文件符合规范","nextStep": "nodeChargeAudit"})
# 发送给“服务器管理员审批”
todo("xiangdk","运维部人员审批",{"DEAL_OPT":"所上传文件符合规范","nextStep": "serverAudit"})
todo("xuyl","服务器管理员审批",{"DEAL_OPT":"拟同意","nextStep": "nodeChargeAudit"})

todo("zhangf","运维部负责人审批",{"DEAL_OPT":"符合规范，拟同意，呈彭馆示","nextStep": "nodeHAudit"})
todo("pengxj","馆领导审批",{"DEAL_OPT":"同意","nextStep": "nodeUpdate"})

# todo("xiangdk","系统更新部署",{"DEAL_OPT":"已经更新完成，请检查结果，并确认。","nextStep": "nodeConfirm"})
todo("xiangdk","系统更新部署",{"DEAL_OPT":"已经更新完成，请检查结果，并确认。","nextStep": "serverConfig"})
todo("xuyl","系统更新部署",{"DEAL_OPT":"服务器配置更新完成，请检查结果。","nextStep": "nodeConfirm"})

todo("liudk","确认更新结果",{"DEAL_OPT":"确认更新成功","nextStep": "endEvent"})



















