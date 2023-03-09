#!python
# encoding: utf-8
import common
import json
import requests

def getBugData():
    with open('./bugData.json','r') as fp:
        return json.load(fp)

bugData=getBugData()

# 数据库更新申请	sysoperaDbUpdate
# 正式资源申请	sysoperaFormalRR
# 测试资源申请	sysoperaFormalTestR
# 系统上线申请	sysoperaGoOnline
# 系统下线申请	sysoperaOffline
# 系统更新申请	sysoperaUpdate
# common.post_applay("sysoperaUpdate",bugData)

# url = common.getUrl("/wf/flow/sysoperaFormalTestR/create?objNode=serverGrant&assignees=12")
url = common.getUrl("/runtime/tasks?start=0&size=3")
req=requests.get(url=url,headers=common.headers)
print req.text