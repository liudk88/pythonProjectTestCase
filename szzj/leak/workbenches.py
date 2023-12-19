import common
import requests

def assetOverview():
    headers = {
        "Authorization":common.testData['access_token']
    }
    params = {
        # "assetId":333
    }
    url = common.getUrl("/leak/workbenches/index")
    req=requests.get(url=url,params=params,headers=headers)
    dimensions=req.json()['data']['dimensions']
    print(dimensions)


assetOverview()

