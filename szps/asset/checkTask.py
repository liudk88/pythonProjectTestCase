import common
import requests

def assetOverview():
    headers = {
        "Authorization":common.testData['access_token']
    }
    params = {
        "query.taskNameLike":"K00032"
    }
    url = common.getUrl("/ass/check/task")
    req=requests.get(url=url,params=params,headers=headers)
    records=req.json()['data']['records']
    print(records)

def rfidCheck():
    headers = {
        "Authorization":common.testData['access_token']
    }
    params = {"UHF_data":[{"id":0, "epc":"TG-201703242020059xx","count":14, "rssi":-53}, {"id":1, "epc":"abc1000000000219312e3051xx", "count":7, "rssi":-72}]};

    url = common.getUrl("/ass/rfid/outterCheck")
    print(url)
    req=requests.post(url=url,json=params,headers=headers)
    records=req.json()['data']
    print(records)


#assetOverview()
rfidCheck()
