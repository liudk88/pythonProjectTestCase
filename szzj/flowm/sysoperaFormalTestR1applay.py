#!python
# encoding: utf-8
import requests

import common

testData=common.getData()

print('==> test apply testResource <===')
url = common.getUrl("/wf/sysoperaFormalTestR/startProcess")
data = {
    "pkv": testData['testResource_flowSeq'],
    "AID": testData['testResource_flowSeq']+"FLOWM",
    "MSG_SYSTEM": common.getNewSysName(),
    "UP_TIME": "2023-03-07T16:00:00.000Za",
    "CONTENT": "这是一条测试的“测试资源申请审批”单",
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
    "FMT_ID": "b2c330f17e6c11ecbb65000c29ac6004",
    "nextStep": "operaAudit",
    "bsFormId": "Form20221U0P5KWR002"
}
req=requests.post(url=url,json=data,headers=common.headers)
print(req.text)
data=req.json()
if data['code'] == 0:
    print('test success!')
else:
    print('test fail!')











