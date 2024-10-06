import sys
import flow
sys.path.append("../..")
import common as c

# 新增信息报告-草稿
def saveDraft(postData={"type":"002","title":"测试资源报告ldk1111","flightDate":"2024-07-08","address":"地点","acReg":"飞机号","flightNo":"航班号","msgType":"1",
                        "departure":"起飞点","arrival":"落地点","aircraftNo":"航空器","carNo":"车辆","groundEquipment":"地面设施","aircraftDamage":"1",
                        "carDamage":"1","groundDamage":"1","otherReason":"其他原因","edescription":"事件经过","category":"1","appendFiles":"None",
                        "occurDate":"2024-07-09 14:00","otherReasonDamage":"1","otherReason":"其他原因"}):
    # postData['id']=6470111007289344
    # postData['title']='编辑后保存草稿222'

    postData['attachments']=[{"name":"time.png","url":"url1","uid":1721353181741,"status":"success"},
                       {"name":"aaaa.xlsx","url":"url2","uid":1721353187096,"status":"success"}]

    postData['applicantId']=1536269127272902700  # 不允许修改的字段
    postData['deptId']='1536266007977406500'  # 不允许修改的字段
    print("提交报告")
    return c.ppost("/asi/inform/saveDraft",postData)

# 提交报告
def submitMsgReport(postData={"type":"001","title":"信息报告001","flightDate":"2024-07-08","address":"地点","acReg":"飞机号","flightNo":"航班号","msgType":"1",
                              "departure":"起飞点","arrival":"落地点","aircraftNo":"航空器","carNo":"车辆","groundEquipment":"地面设施","aircraftDamage":"1",
                              "carDamage":"1","groundDamage":"1","edescription":"事件经过","category":"1","appendFiles":"None",
                              "occurDate":"2024-07-09 10:30","otherReasonDamage":"1","otherReason":"其他原因"}):
    print("提交报告")
    # postData['id']=6480612416696320
    return c.ppost("/asi/inform/apply",postData)

# 匿名提交报告
# curl 'http://127.0.0.1:8080/asi/inform/anonyApply' \
#      -H 'Accept: application/json, text/plain, */*' \
#      -H 'Content-Type: application/json' \
#      --data-raw '{"type":"003","title":"安全举报002","flightDate":"2024-07-24","address":"地点","acReg":"","flightNo":"","msgType":"","departure":"","arrival":"","aircraftNo":"","carNo":"","groundEquipment":"","aircraftDamage":"2","carDamage":"2","groundDamage":"2","otherReason":"","edescription":"事件经过","category":"10","applicantId":1001,"deptId":1,"appendFiles":null}' \
#      --compressed
def submitAnony(postData={"type":"003","title":"测试安全举报","flightDate":"2024-07-08","address":"地点","acReg":"飞机号","flightNo":"航班号","msgType":"1",
                              "departure":"起飞点","arrival":"落地点","aircraftNo":"航空器","carNo":"车辆","groundEquipment":"地面设施","aircraftDamage":"1",
                              "carDamage":"1","groundDamage":"1","otherReason":"其他原因","edescription":"事件经过","category":"1","appendFiles":"None"}):
    postData['code']=5
    postData['uuid']="273571fe-fd49-49a3-b24c-6e901b2936cc"
    print("提交报告-未验证退出登录时提交")
    return c.ppost("/asi/inform/anonyApply",postData)

def findEventPage(postData={"pageNum":1,"pageSize":10,"applyTimeStart":"2024-07-24 12:30","applyTimeOrderBy":"0"}):
    print("查询事件列表")
    # return c.ppost("/asi/inform/findPage",postData)
    return c.ppost("/asi/inform/findSelf",postData)

def get(id=6474674215661568):
    print("查看事件")
    return c.pget("/asi/inform/"+str(id))

def delete():
    print("删除事件")
    return c.pget("/asi/inform/remove/6474326467489792")

def submit():
    print("直接提交报告")
    return c.pget("/asi/inform/6480277652320256/submit")

def mergeReport():
    print("直接提交报告")
    return c.pget("/asi/inform/mergeReport?mainReportId=6509482026348544&subReportIds=6509482026348544,6509473975054336")

def findPage(postData={"page":{"limit":10,"offset":0}}):
    print("查询待办任务")
    return c.ppost("/task/findRuntimeTasks",postData)

def findAwaits(postData={"page":{"limit":10,"offset":0}}):
    print("查询待办任务")
    return c.ppost("/processInst/findAwaits",postData)

def getTask():
    print("查看详情及流程任务信息")
    return c.pget("/asi/inform/1823255592252329985/task/0336f9d1-5943-11ef-9965-525400123456")


def dealWf(username,currentStepName,comment,selfParams={}):
    header=flow.getHeader(username)
    # 先查询任务
    req=c.post("/task/findRuntimeTasks",{"page":{"limit":100,"offset":0}},header)
    row=req.json()['data']['rows']
    if len(row) == 0:
        print("没有待办任务")
    else:
        task=row[0]
        # print(task)
        taskId=task['taskId']
        businessKey=task['businessKey']
        postData={"taskId":taskId,"comment":comment,"entityId":businessKey,"passed":"true"}
        postData.update(selfParams)
        flow.dealWfWithHeader(username,currentStepName,postData,header)

def auditInformation():
    print("审核-信息报告")
    # dealWf('zrb_zb-jl','责任部门值班经理',"ok")

    # dealWf('zrb_aj-jl','责任部门安质经理',"ok，启动调查、不上报安监",{"startCheck":"false","report":"false"})
    # dealWf('zrb_aj-jl','安质经理归档',"审核通过")
    #---------------------------------------------------------------------
    ajdata={"startCheck":"true","report":"true"};
    # 上传附件
    # ajdata['attachments']=[{"name":"time.png","url":"url1","uid":1721353181741,"status":"success"},
    #                        {"name":"aaaa.xlsx","url":"url2","uid":1721353187096,"status":"success"}]
    # dealWf('zrb_aj-jl','责任部门安质经理',"ok，启动调查、上报安监",ajdata)

    # aj-jb  anjianzhiban
    # dealWf('aj-jb','安监值班',"ok")   # aj-jb

    aqjcy="aj-jcy"
    # aqjcy="A00372"
    dealWf(aqjcy,'安监监察员',"第一次审核不通过",{"passed":"false"})  # aj-jcy
    # dealWf(aqjcy,'安监监察员',"第二次审核通过 ",{"passed":"true"})  # aj-jcy
    # dealWf(aqjcy,'安监监察员',"第二次审核通过 ",{"passed":"true","status":"1","otherReason":"其它原因aa","type":"100","id":"1823275910589108225"})  # aj-jcy 审核加更新

    ajld="ajld"
    # ajld="A01933"
    # dealWf(ajld,'安监领导',"ok，启动调查、通过",{"passed":"true"})
    # dealWf(ajld,'安监副总/安全总监',"ok，启动调查、通过",{"passed":"false"})

    aqxxy="aqxxy"
    # aqxxy="A03792"
    dealWf(aqxxy,'安全信息员归档',"ok")

def auditVoluntary():
    print("审核-自愿报告")
    # dealWf('zrb_aj-jl','安质经理归档',"审核通过",{"report":"true"})

    dealWf('A00372','安监监察员',"第一次审核不通过",{"passed":"false"})  # aj-jcy
    # dealWf('A00372','安监监察员',"第二次审核通过 ",{"passed":"true"})  # aj-jcy

    # dealWf('A01933','安监领导',"ok，通过",{"passed":"true"})

    # dealWf('A03792','安全信息员归档',"ok")

def auditSecurity():
    print("审核-安全举报")
    # 匿名
    # dealWf('A00372','安监监察员',"第一次审核不通过",{"passed":"false"})  # aj-jcy
    # dealWf('A00573','安监监察员',"第二次审核通过 ",{"passed":"true"})  # aj-jcy
    #
    # dealWf('A01933','安监副总/安全总监',"ok，通过",{"passed":"true"})
    #
    # dealWf('A03792','安全信息员归档',"ok")


    # 非匿名
    dealWf('A00573','安监监察员',"第二次审核通过 ",{"passed":"true"})  # aj-jcy

    dealWf('A01933','安监副总/安全总监',"ok，通过",{"passed":"true"})

    dealWf('A03792','安全信息员归档',"ok")

def getCode():
    print("获取验证码")
    c.pget("/auth/code");

def permissionAdd(eventId=6776042860064768,deptIdList=[111],userIdList=[1003]):
    print("事件增加权限范围")
    postData={"eventId":eventId,"deptIdList":deptIdList,"userIdList":userIdList}
    # postData={"eventId":eventId,"open":"true"} # 设置公开
    return c.ppost("/asi/inform/permission/save",postData)

def copyto(businessId=1822820474794590210,deptIdList=[1536265612618117121],userIdList=[1001]):
    print("抄送")
    postData={"processDefKey":"information","businessId":"6481679049568256","deptIdList":["1536265646474539010","1536265646608756737","1536265646713614338"],"copiedUserIdList":["1557649583822098433","1689184274680451074"],"taskDefKey":"Activity_0i7ea2w","taskId":"8caadf87-4a67-11ef-aaa0-0050569cb713"}
    # postData={"eventId":eventId,"deptIdList":deptIdList,"userIdList":userIdList}
    # postData={"businessId":businessId,"copiedUserIdList":userIdList,"deptIdList":deptIdList,"processDefKey":"information"}
    return c.ppost("/asi/act/ru/copyto/copyto",postData)

    # c.ppost("/asi/act/ru/copyto/findSelf",{"pageNum":1,"pageSize":10,"readed":"0"})

def revokeTask(processId="bf47f264-459d-11ef-b8a1-0050569cb713"):
    print("撤回任务")
    return c.ppost("/task/revokeTask?processId="+processId,{})

def backTask(taskId="e89f643a-5f5a-11ef-b92b-525400123456"):
    print("回退任务")
    return c.ppost("/task/"+taskId+"/backTask",{})

def test():
    print("test")
    # c.ppost("/asi/act/ru/copyto/findPage",{"businessKey":"6481679049568256","page":{"limit":"10","offset":"0"}});
    # c.ppost("/asi/act/ru/copyto/read/1819275273552531458,1819275273741275138",{});
    c.pget("/task/findCommentsById?id=1825767146983112705",{});
    # c.pget("/task/getReviewedTaskCount");

def queryExportableColumn():
    c.pget("/asi/inform/xls/queryExportableColumn")

def downExcel(fileName="sjgl.xlsx"):
    output="/home/liudk/Downloads/"+fileName
    c.downLoadPost("/asi/inform/xls/expExcel",output,{"exportPptionList2":["title","deptIdLabel","typeLabel","flightDate"]})
    print('导出的文件：'+output)

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())