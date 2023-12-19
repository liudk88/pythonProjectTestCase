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


assetOverview()

