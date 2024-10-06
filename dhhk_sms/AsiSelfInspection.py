import flow
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import common as c

addData={
    "planName":c.ftime+"自查计划的名称", # 自查计划的名称
    # "applicantId":"123", # 申请人
    # "applyTime":"2024-08-13", # 申请时间
    # "department":"123", # 自查部门
    "num":"id0001", # 编号
    # "level":"0", # 级别(0:公司级;1:部门级)  //todo?
    # "implPeriod":"2024-08-13", # 实施期限
    "compilationTime":"2024-08-13 12:12", # 编制时间
    # "implState":"0", # 实施状态(0:未实施;1:实施中;2:已实施)

    "checkOrgList":[
        {
        # "planId":"123", # 计划主键
        "selfCheckWay":"01", # 自查形式(0:日常检查;1:专项检查;2:其他检查)
        "checkManageDept":124, # 局方检查单管理部门
        "checkProfessional":"01", # 局方检查单专业名称
        "checkOrg":111, # 检查对象
        "checkOrgLabel":"检查对象001", # 检查对象中文名
        "executivePosition":"执行岗位1", # position
        "checkItem":"检查项目", # 检查项目
        "numbers":"1", # 条目数(条)
        "planCheckFrequency":"计划检查频次", # 计划检查频次
        "planCheckTime":"2024-08-13", # 计划检查时间
        # "implState":"1", # 实施状态
        "implPeriod":"01", # 实施期限
    },{
            # "planId":"123", # 计划主键
            "selfCheckWay":"02", # 自查形式(0:日常检查;1:专项检查;2:其他检查)
            "checkManageDept":456, # 局方检查单管理部门
            "checkProfessional":"02", # 局方检查单专业名称
            "checkOrg":222, # 检查对象
            "checkOrgLabel":"检查对象001", # 检查对象中文名
            "executivePosition":"执行岗位2", # position
            "checkItem":"检查项目", # 检查项目
            "numbers":"2", # 条目数(条)
            "planCheckFrequency":"计划检查频次", # 计划检查频次
            "planCheckTime":"2024-08-13", # 计划检查时间
            # "implState":"1", # 实施状态
            "implPeriod":"02", # 实施期限
        }]
}

g_id=1828976646845202434
g_taskId="0eab87b1-65ab-11ef-a927-3609eeccf9dd"

#【新增】
def add(postData=addData):
    print("【新增】")

    # postData['id']=1828238462876160002;

    # 测试空值情况
    # postData['planName']='';


    # 增加附件
    postData['attachments']=[{"name":"time.png","url":"url1","uid":1721353181741,"status":"success"},
                             {"name":"aaaa.xlsx","url":"url2","uid":1721353187096,"status":"success"}]

    return c.ppost("/asi/self/inspection/saveDraft",postData)

def commitApply(postData=addData):
    print("【（新增时）提交申请】")
    # 增加附件
    postData['attachments']=[{"name":"time.png","url":"url1","uid":1721353181741,"status":"success"},
                             {"name":"aaaa.xlsx","url":"url2","uid":1721353187096,"status":"success"}]

    return c.ppost("/asi/self/inspection/commitApply",postData)

def update(postData=addData):
    print("【更新】")

    # 测试空值情况
    # postData['planName']='';
    # postData['id']=""

    postData['id']="1826083803646513154"
    return c.pput("/asi/self/inspection",postData)

def list(postData={"pageNum":1,"pageSize":10}):
    print("【查询所有列表】")
    # postData['implPeriodStart']='2024-08-10'
    # postData['implPeriodEnd']='2024-08-12'
    return c.ppost("/asi/self/inspection/findPage",postData)

def listSelf(postData={"pageNum":1,"pageSize":10}):
    print("【查询带权限列表】")
    return c.ppost("/asi/self/inspection/findSelf",postData)

def commit(id=str(g_id)):
    print("【直接提交申请】")
    return c.ppost("/asi/self/inspection/"+id+"/submit",{})

def getInfo(id=g_id):
    return c.pget("/asi/self/inspection/"+str(id))

def getTaskInfo(id=g_id,taskId=g_taskId):
    return c.pget("/asi/self/inspection/"+str(id)+"/task/"+taskId)

# def findToDoTask(username="sqr",postData={"page":{"limit":10,"offset":0}}):
#     return flow.findToDoTask(username,postData)

def dealWf(username,currentStepName,comment,selfParams={}):
    task=flow.findToDoTask(username,{"page":{"limit":10,"offset":0},"businessKey":str(g_id)})[0]
    taskId=task['taskId']
    businessKey=task['businessKey']
    postData={"taskId":taskId,"comment":comment,"entityId":businessKey,"passed":"true"}
    postData.update(selfParams)
    header=flow.getHeader(username)
    flow.dealWfWithHeader(username,currentStepName,postData,header)

def audit():
    # print("审核")

    # A01453 A02226
    dealWf('A02226','部门总审核',"通过",{"passed":"true"
        ,"attachments":[{"name":"flowTime.png","url":"url1","uid":1721353181741,"status":"success"},
        {"name":"flowAaaa.xlsx","url":"url2","uid":1721353187096,"status":"success"}]
    })

    dealWf('A04955','安监',"ok",{})
    #
    # sqr A03383
    # dealWf('A03383','发起者填写结果并归档',"ok",{"implResultList":[
    #     {"id":1828614231976697857,"implResult":"implResult001","attachments":[{"name":"implResulttime1.png","url":"url1"},{"name":"implResultaaaa1.xlsx","url":"url2"}]}
    #     # ,{"id":1825779965806796801,"implResult":"implResult002","attachments":[{"name":"implResulttime2.png","url":"url2"},{"name":"implResultaaaa2.xlsx","url":"url2"}]}
    # ]})

def commitCheckResult():
    return c.ppost("/asi/self/inspection/commitCheckResult",{"implResultList":[
        {
            "id":1828614231905394690,"implResult":"implResult001","attachments":[{"name":"implResulttime1.png","url":"url1"},{"name":"implResultaaaa1.xlsx","url":"url2"}]}
        # ,{"id":1825779965806796801,"implResult":"implResult002","attachments":[{"name":"implResulttime2.png","url":"url2"},{"name":"implResultaaaa2.xlsx","url":"url2"}]}
    ]})

def init():
    return c.pget("/asi/self/inspection/init")

def permissionAdd(planId=1825822343720660993,deptIdList=[111],userIdList=[1003]):
    print("增加权限范围")
    postData={"planId":planId,"deptIdList":deptIdList,"userIdList":userIdList}
    # postData={"planId":planId,"open":"true"} # 设置公开
    return c.ppost("/asi/self/inspection/permission/save",postData)

def queryExportableColumn():
    c.pget("/asi/self/inspection/xls/queryExportableColumn")

def downExcel(fileName="fdzc.xlsx"):
    output="/home/liudk/Downloads/"+fileName
    c.downLoadPost("/asi/self/inspection/xls/expExcel",output,{"exportPptionList":["planName"]})
    print('导出的文件：'+output)

def test():
    # c.pget("/sys/position/findUsersByPositionId?id=14")
    # c.ppost("/sys/user/position/manage/batchAdd",{"positionId":10,"userId":1010,"deptIdList":[1]})
    c.ppost("/processInst/findProcessManage",{"pageSize":15,"pageNum":1,"currentAssigneeNameOrEno":"A01933"})
    # c.ppost("/processInst/findTaskAssigeeeUpdateLog",{"pageSize":10,"pageNum":1,"procInstId":"00276f06-6f22-11ef-99b3-0050569cb713"})
    # c.ppost("/processInst/updateTaskAssigeee",{"taskIdList":["46f5cdeb-6f22-11ef-99b3-0050569cb713","e549ee7b-725c-11ef-b6b8-005056c00001"],"afterContent":"1001"})

# funs="init"
# funs="add"
# funs="list"
# funs="listSelf"
funs="getInfo"
# funs="commit"

# funs="getTaskInfo"
# funs="findToDoTask"
# funs="audit"
# funs="permissionAdd"



# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())