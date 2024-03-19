import sys
sys.path.append("../..")
import common as c

def list():
    c.pget("/ynwxb/asset/headupdate")

def add():
    params={
        # "headUpdateId": "",
        "assetId": "assetId001",
        "assetType": "SO",
        "fileToken": "fileToken001",
        # "applyMan": "admin",
        # "applyOrg": "",
        "updateHead": "xiaozhang",
        "updateHeadPhone": "13905555555",
        # "state": 0,
        # "workId": "",
        # "taskScopeId": ""
    }
    c.ppost('/ynwxb/asset/headupdate/add', params)

def info():
    c.pget("/ynwxb/asset/headupdate")
# 核查指定信息系统
def listSystem():
    c.ppost("/ynwxb/asset/view/AssetView-BS/list",{})

args=c.args()

if(len(args) == 0):
    args.append("0")
    # args.append("1")




if len(args)==0 or args[0]=='0':
    list()
elif args[0]=='1':
    add()
elif args[0]=='4':
    info()
