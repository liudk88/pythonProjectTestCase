#!python
# encoding: utf-8
import requests

import common

testData=common.getData()

print('==> test apply Resource <===')

sysname=common.getNewSysName()
# 单独测试上线流程，指定系统名称
# sysname="XC-运维管理平台";
sysData=common.getSystemByName(sysname)

url = common.getUrl("/wf/sysoperaFormalRR/startProcess")
data = {
    "pkv": testData['resource_flowSeq'],
    "AID": testData['resource_flowSeq']+"FLOWM",
    "MSG_SYSTEM": sysname,
    "DB_USER": "aaaaa",
    "ASSET_ID": sysData['pkv'],
    "UP_TIME": "2023-03-17T16:00:00.000Za",
    "CONTENT": "这是一条测试的“正式资源申请审批”单",
    "LINE_CONTEXT": "测试数据，没有要求",
    "LINK_PHONE": "刘邓康/83781022",
    "APPLY_DETAIL": [{
        "DEPLOY_TYPE": "0",
        "COUNT_CPU": 4,
        "COUNT_MEMORY": "4",
        "STATE_CLUSTER": "0",
        "STATE_AID": "0",
        "rowIndex": 0,
        "VERSION_SYSTEM": "1",
        "VSESION_DB": "1",
        "MIDDIN_TOOL": "1",
        "SIZE_AID": "12G",
        "SIZE_TABLE": "144",
        "JDNI_NAME": "web",
        "RANG_VISIT": "0",
        "NON_REL_DB": "mogodb"
    },{
        "DEPLOY_TYPE": "0",
        "COUNT_CPU": 8,
        "COUNT_MEMORY": "16",
        "STATE_CLUSTER": "0",
        "STATE_AID": "0",
        "rowIndex": 0,
        "VERSION_SYSTEM": "1",
        "VSESION_DB": "1",
        "MIDDIN_TOOL": "1",
        "SIZE_AID": "32G",
        "SIZE_TABLE": "144",
        "JDNI_NAME": "web",
        "RANG_VISIT": "0",
        "NON_REL_DB": "redis"
    }],
    "ORGID": "201606051113025150015",
    "FMT_ID": "b2c330f17e6c11ecbb65000c29ac6005",
    "nextStep": "operaAudit",
    "bsFormId": "Form20221U0PXKMY004"
}
req=requests.post(url=url, json=data, headers=common.g_headers, verify = False)
print(req.text)
data=req.json()
if data['code'] == 0:
    print('test success!')
else:
    print('test fail!')











