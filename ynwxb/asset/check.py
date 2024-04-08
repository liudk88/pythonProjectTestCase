import sys
sys.path.append("../..")
import common as c

def list():
    print('list')

def add():
    params={"workId":0,
            "name":"ldktest0317-001",
            "workType":"asset", # domain 表示域名核查，asset是资产核查
            "content":"<p>test</p>",
            # "orgId":null,
            "startDate":"2024-02-29T16:00:00.000Z",
            "endDate":"2024-03-30T16:00:00.000Z",
            # "fileInfos":null,
            # "publishTime":null,
            "state":0,
            # "templateId":null,
            # "remark":null,
            # "createUser":null,
            # "createTime":null,
            # "updateUser":null,
            # "updateTime":null,

            #指定单位或指定具体资产
            # "orgIdList":["980033","980034","980035","980037","980038","980039","980040"],
            "orgIdList": [],
            "assetIdList": ["1200151092629864448", "1194586559236538368", "1052556203122491392"],
            "workWay": "1",

            "publishFlag":1,
            # "assetIdList":null,
            # "planIdList":null,
            "domainWork":"true",
            "assignAssetWork":"false",
            "rangeDate":["2024-02-29T16:00:00.000Z","2024-03-30T16:00:00.000Z"]}
    c.ppost('/domain/task/add', params)

def info():
    c.pget("/domain/task/select?workId=5766790290984960")
# 核查指定信息系统
def listSystem():
    c.ppost("/ynwxb/asset/view/AssetView-BS/list",{})

args=c.args()

if(len(args) == 0):
    # args.append("orgManage")
    # args.append("orgManage2")
    # args.append("workItems")

    # args.append("assetCheckOrgTask")
    # args.append("commitList")
    args.append("assetCheckOrgCheck")
    # args.append("publishScope")

args[0]='4'


if len(args)==0:
    list()
elif args[0]=='1':
    add()
elif args[0]=='4':
    info()
elif args[0]=='listSystem':
    listSystem()
elif args[0]=='allSystemIds':
    c.ppost("/ynwxb/asset/view/AssetView-BS/allSystemIds",{})
elif args[0]=='orgManage': #查找工作及其范围(返回的scopeId用来继续调用workItems接口，所以可以调用两次，第一次查出想看的工作，再通过工作找出scopeId)
    c.pget("/domain/app/orgManage") # 不指定工作默认使用第一个
elif args[0]=='orgManage2':
    c.pget("/domain/app/orgManage?workId=5778034524082176") # 指定工作

# 重点域名调试
elif args[0]=='workItems':  #填报列表
    c.pget("/domain/app/workItems?workId=5789140244484096&scopeId=5789140245401600&page=1&limit=10")
elif args[0]=='publishScope':
    c.ppostf("/domain/app/publishScope",{"scopeId":"5751453370142731"})

# 资产核查
elif args[0]=='assetCheckOrgTask':
    c.pget("/ynwxb/asset/view/assetCheckOrgTask")
elif args[0]=='commitList':
    c.pget("/ynwxb/asset/view/commitList?workId=5790056386449408&scopeId=5790068600000524&page=1&limit=10")
# 模拟前端资产核查上报页面
elif args[0]=='assetCheckOrgCheck':
    # data=c.pget("/ynwxb/asset/view/assetCheckOrgTask");
    data=c.pget("/ynwxb/asset/view/assetCheckOrgTask?workId=5778034524082176");
    viewData=data.json()['data']['view']
    scopeId=str(viewData['scopeId'])
    workId=str(viewData['workId'])
    print("查询任务核查资产信息")
    c.pget("/ynwxb/asset/view/commitList?workId="+workId+"&scopeId="+scopeId+"&page=1&limit=10")
