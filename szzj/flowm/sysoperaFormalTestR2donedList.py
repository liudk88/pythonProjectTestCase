#!python
# encoding: utf-8
import requests
import common

testData=common.getData()

print('==> test 测试资源已办任务列表 <===')
url = common.getUrl("/view/FView20221Q0V7YAG003/view?FLOW_SEQ="+testData['testResource_flowSeq'])

req=requests.get(url=url, headers=common.g_headers, verify = False)
print(req.text)

datas=req.json()['data']['datas']
# print(datas)
if len(datas) == 1:
    print('test success!')
else:
    print('test fail!')













