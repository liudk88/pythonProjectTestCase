import common
import requests
import json

def ywgl():
    headers = {
        "Authorization":common.testData['access_token']
    }
    params = {
        "type":"1"
    }
    url = common.getUrl("/operator/perspective/workList")
    req=requests.get(url=url,params=params,headers=headers)
    records=req.json()['data']
    print(json.dumps(records,indent=4))

def assetCheck():
    headers = {
        "Authorization":common.testData['access_token']
    }
    params = {}
    url = common.getUrl("/asset/perspective/assetCheck")
    req=requests.get(url=url,params=params,headers=headers)
    records=req.json()['data']
    print(json.dumps(records,indent=4))

#ywgl()
assetCheck()

