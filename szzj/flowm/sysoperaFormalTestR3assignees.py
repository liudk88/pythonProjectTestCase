#!python
# encoding: utf-8
import requests
import common

testData=common.getData()

print('==> test 测试资源提交申请后办理人 <===')
url = common.getUrl("/wf/task?business_id="+testData['testResource_flowSeq'])

req=requests.get(url=url,headers=common.headers)
print(req.text)

datas=req.json()['data']['users']
# print(datas)
if len(datas) == 3:
    # 办理人分别是向东珂,徐玉良,钟晓奇
    if datas[0]['userid'] == '12' and datas[1]['userid'] == '201607151617025430523' and datas[2]['userid'] == '19':
        print('test success!')
    else:
        print('test fail!')
else:
    print('test fail!')













