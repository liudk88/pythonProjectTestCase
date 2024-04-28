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
        # "workId": "",
        # "taskScopeId": ""
    }
    c.ppost('/ynwxb/asset/headupdate/add', params)

def info():
    c.pget("/ynwxb/asset/headupdate/5791089415368704")
# 核查指定信息系统
def listSystem():
    c.ppost("/ynwxb/asset/view/AssetView-BS/list",{})

args=c.args()

if(len(args) == 0):
    args.append("0")
    # args.append("1")
    # args.append("4")
    # args.append("auditPass")
    # args.append("auditNoPass")




if len(args)==0 or args[0]=='0':
    list()
elif args[0]=='1':
    add()
elif args[0]=='4':
    info()
elif args[0]=='auditPass':
    c.pget("/ynwxb/asset/headupdate/auditPass/5807347815165952?auditDes=同意")
elif args[0]=='auditNoPass':
    c.pget("/ynwxb/asset/headupdate/auditNoPass/5794770016284672,5791089415368704?auditDes=不同意")
elif args[0]=='auditPass':
    c.pget("/ynwxb/asset/headupdate/auditPass/5807347815165952?auditDes=同意")
elif args[0]=='auditNoPass':
    c.pget("/ynwxb/asset/headupdate/auditNoPass/5794770016284672,5791089415368704?auditDes=不同意")
