#!python
# encoding: utf-8
import common

testData=common.getData()

def todo(username,currentStepName,dealFormData):
    common.todo(username,currentStepName,"offline_flowSeq","Form20221U0PXKMY003",dealFormData)

print('==> test 系统下线申请 审批 <===')

todo("xiangdk","业务主管部门审批",{"DEAL_OPT":"拟同意","nextStep": ""})
todo("xuyl","服务器注销",{"DEAL_OPT":"系统网络访问已关，服务器关机回收","nextStep": "nodeConfirm"})
todo("xiangdk","应用注销",{"DEAL_OPT":"服务器已经关闭，应用无需操作","nextStep": "nodeConfirm"})
todo("zhongxq","数据库注销",{"DEAL_OPT":"已锁定对应数据库用户","nextStep": "nodeConfirm"})
todo("liudk","资源注销结果确认",{"DEAL_OPT":"确认已经注销","nextStep": "endEvent"})




















