#!python
# encoding: utf-8
import requests

import common

testData=common.getData()

print('==> test goOnLine <===')

sysname=common.getNewSysName()
sysData=common.getSystemByName(sysname)

url = common.getUrl("/wf/sysoperaGoOnline/startProcess")
data = {
    "pkv": testData['goOnline_flowSeq'],
    "MSG_SYSTEM": sysname,
    "ASSET_ID": sysData['pkv'],
    "DB_USER": "1082101423421784064",
    "TEST_LINK": "https://zjjtest.sz.gov.cn/itom/#/login",
    "TEST_USER_PWD": "admin / szzj@2022",
    "CONTENT": "这是一条测试的“系统上线申请审批”单",
    "DEAL_MAN": "12",
    "ORGID": "201606051113025150015",
    "systemChargers": {},
    "PACK_TYPE": "manual",
    "CREATOR": "2209154te15h8sz8g27869",
    "SEND_SMS": "0",
    "UPDATE_TYPE": "1",
    "APPER_ACCOUNT": "liudk",

    "FMT_ID": "b2c330f17e6c11ecbb65000c29ac6001",
    "AID": testData['goOnline_flowSeq']+"FLOWM",
    "assignees": "12",
    "nextStep": "nodeBAudit",
    "bsFormId": "Form20221Q0V7Z10002",
    "sendSms": "0"
}
req=requests.post(url=url,json=data,headers=common.headers)
print(req.text)
data=req.json()
if data['code'] == 0:
    print('test success!')
else:
    print('test fail!')











