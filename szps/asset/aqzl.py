#  ===> 安全总览 <===
import sys
sys.path.append("../..")
import common as c
from FunClass import FunClass
import json

# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="0"

funList=[]
funList.append(FunClass("assetCheck","【资产盘点统计】")) #0



def assetCheck():
    req=c.pget("/asset/perspective/assetCheck")
    records=req.json()['data']
    print(json.dumps(records,indent=4))

# def ywgl():
#     headers = {
#         "Authorization":common.testData['access_token']
#     }
#     params = {
#         "type":"1"
#     }
#     url = common.getUrl("/operator/perspective/workList")
#     req=requests.get(url=url,params=params,headers=headers)
#     records=req.json()['data']
#     print(json.dumps(records,indent=4))



# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())

