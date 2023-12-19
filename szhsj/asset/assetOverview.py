import common
import requests

def assetOverview():
    headers = {
        "Authorization":common.testData['access_token']
    }
    params = {
        # "assetId":333
    }
    url = common.getUrl("/assetOverview/index")
    req=requests.get(url=url,params=params,headers=headers)
    dimensions=req.json()['data']['dimensions']
    # 验证dimensions在集合[{'id': 'organization', 'label': '组织机构'}, {'id': 'machineRoom', 'label': '机房'}, {'id': 'securityDomain', 'label': '安全域'}]里
    print(dimensions)


assetOverview()

