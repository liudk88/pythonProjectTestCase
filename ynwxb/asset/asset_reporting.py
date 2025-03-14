#  ===> 资产核查填报 <===
import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
import common as c

# 获取当前时间
now = datetime.datetime.now()
# 格式化时间为指定字符串格式，这里按照年、月、日、时、分拼接并格式化

g_workId=7329311683170304 
# 工作台-待办工作
def workbenchTodoWorkList():
    c.pget("/workbench/workList?page=1&limit=5")

# 工作台-待办工作-处理(资产任务)列表
def assetTaskList():
    c.pget("/ynwxb/asset/view/taskList?workId="+str(g_workId)+"&page=1&limit=10")

# 工作台-待办工作-处理(资产任务)列表-核查资产（查看单位任务信息）
def assetOrgTaskInfo():
    c.pget("/domain/app/orgRange/"+str(g_workId))

# 工作台-待办工作-处理(资产任务)列表-核查资产列表
def checkAssetList():
    taskScopeId="7329311684415488"
    c.pget("/view/AssetView-AU/view?flag=1&taskScopeId="+taskScopeId+"&isAuditBack=1")

# 提交资产核查工作
def submitAssetWork():
    c.ppost("/asset/work/publishScope",{"scopeId":"7329311684415499","commitDes":"已经完成核查"})

# 已办任务
def completedWorkList():
    c.pget("/workbench/finishList?page=1&limit=5")

# 查询域名日志
def domainLogList():
    c.pget("/domain/log/selectLogs?appId=7187852635820032")

# 资产日志
def assetLogList():
    c.pget("/assetLog/queryList/1044911935537020928")

# 资产日志入库
def assetStore():
    c.ppost("/assetLog/store?assetId=1044911935537020928&storeDesc=测试入库",{})

# 资产日志批量入库
def assetBatchStore():
    # c.ppost("/assetLog/batchStore?assetIds=1044911935537020928&assetIds=1054781728947699712&storeDesc=测试入库",{})
    c.ppost("/assetLog/batchStore",{"storeDesc":"测试入库","assetIds":["1044911935537020928","1054781728947699712"]})

# 资产填报详情
def assetFillList():
    c.ppost("/ynwxb/asset/view/queryReportDatas?workId=7347691315253248",{})

# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="2"


# 单位范围id，资产核查后面的功能都关联此参数
g_scopeId="5986985363296256"

def taskList():
    c.pget("/ynwxb/asset/view/taskList?workWay=1&page=1&limit=1")

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

if __name__ == "__main__":
    c.callSelfFun(globals())

