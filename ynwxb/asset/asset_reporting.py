#  ===> 资产核查填报 <===

import sys
sys.path.append("../..")
import common as c
from FunClass import FunClass
import json

l=[]
l.append(FunClass("taskList","【任务列表】"))
l.append(FunClass("orgRange","【任务列表:核查/提交(查看单位工作)】"))
l.append(FunClass("commit","【任务列表:提交】"))
l.append(FunClass("toAddSystem","【任务列表:核查|信息系统列表：进入新增】"))
l.append(FunClass("addSystem","【任务列表:核查|信息系统列表：新增保存】"))
l.append(FunClass("expDatas","【任务列表:核查|信息系统列表：导出】"))
l.append(FunClass("impDatas","【任务列表:核查|信息系统列表：导入】"))

# 单位范围id，资产核查后面的功能都关联此参数
g_scopeId="5986985363296256"
# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="2"

def taskList():
    c.pget("/ynwxb/asset/view/taskList?workWay=1&page=1&limit=10")

def orgRange():
    t_workId="5986985362247680"
    res=c.pget("/domain/app/orgRange/"+t_workId)
    c.put("asset_reporting.py","g_scopeId",res.json()['data']['scopeId']) #修改本文件参数

def commit():
    c.post("/domain/app/publishScopeV2",{"workId":"5986985362247680","commitDes":"已经完成核查","commitFile":"eafkmm40pcpfgcrl4g1a"})

def toAddSystem():
    res=c.get("/form/AssetForm-BS/view?scopeId="+g_scopeId)
    jsonData=res.json()
    datas=jsonData['data']['datas']
    coms=jsonData['data']['coms']
    #验证单位选项的范围：系统所有单位
    orgCompOpts=coms[0]['options']
    formatted_json = json.dumps(orgCompOpts, indent=2, ensure_ascii=False)
    print(formatted_json)
    #验证带有返回scopeId组件
    scopeIdCom=list(filter(lambda x:x['id']=='scopeId',coms))
    print(scopeIdCom)
    assert len(scopeIdCom)==1, "没有找到id为scopeId的组件！"
    #验证有返回scopeId的值
    print(datas['scopeId'])
g_scopeId="5986985363296256"

def addSystem():
    c.post("/form/AssetForm-MR",{
        "SERVER_CENTER_NAME": "jf001",
        "LONGITUDE": "22",
        "LATITUDE": "22",
        "LOCATION": "test",
        "OPERATE_ORGANIZATION": "test",
        "CONTACT_NAME": "zhangsan",
        "CONTACT_PHONE": "13988888888",
        "SERVER_CENTER_MEASURE": "",
        "ORGID": "980022",
        "ASSET_TYPE": "MR",
        "ASSET_TYPEH": "MR",
        "SERVER_CENTER_STATUS": "0",
        "scopeId":g_scopeId
    })

def expDatas():
    c.downLoad("/view/excel/FXls20225243KCXS0BS/exp?flag=1&scopeId="+g_scopeId+"&viewId=AssetView-BS&isTemplate=0","/home/liudk/Downloads/信息系统.xlsx")
    #tocheck: 需要验证数据范围是否和列表一致，单位选项是否是所有单位

def impDatas():
    files = {'excelFile': open("/home/liudk/Downloads/信息系统-tb.xlsx", 'rb',)}
    data={"viewId":"AssetView-BS"}
    r=c.post_file_req("/view/excel/FXls20225243KCXS0BS/imp?scopeId="+g_scopeId,files,data)
    jsonData=r.json()
    invaildNum=jsonData['data']['invaildNum']
    #tocheck: 不合法数据和预期一样
    if invaildNum>0:
        print("不合法数据"+str(invaildNum)+"条！")
        errorXlsToken=jsonData['data']['errorXlsToken']
        print("下载不合法的数据xlsx")
        c.downLoad("/view/exportInvaildDatas/"+errorXlsToken,"/home/liudk/Downloads/信息系统invaild.xlsx")

# =================
#如果gt_lastExeFunIndex有值，那么就以gt_lastExeFunIndex为执行目标
#如果没有，那么提示输入，按输入执行，并更新gt_lastExeFunIndex的值
funlist=''
if len(gt_lastExeFunIndex)==0:
    for index,f in enumerate(l):
        print(f"{index}. {f.toString()}")
    funlist = input("请输入需要执行的方法序号，多个以英文逗号隔开:")
    if len(funlist)>0:
        c.put("asset_reporting.py","gt_lastExeFunIndex",funlist) #记住下标，下次直接回车使用
else:
    funlist=gt_lastExeFunIndex

indexArr=funlist.split(",")
for index,f in enumerate(l):
    if str(index) in indexArr:
        print(f"执行方法=> {f.name}")
        func = globals()[f.name]
        func()
