import flow
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import common as c

g_id=1826150625033961473

addData={
    "planId":"123", # 计划主键
    "selfCheckWay":"自查形式(0:日常检查;1:专项检查;2:其他检查)", # 自查形式(0:日常检查;1:专项检查;2:其他检查)
    "checkManageDept":"123", # 局方检查单管理部门
    "checkProfessional":"局方检查单专业名称", # 局方检查单专业名称
    "checkOrg":"123", # 检查对象
    "executive":"position", # position
    "checkItem":"检查项目", # 检查项目
    "numbers":"1", # 条目数(条)
    "planCheckFrequency":"计划检查频次", # 计划检查频次
    "planCheckTime":"2024-08-13", # 计划检查时间
    "implState":"实施状态(0:未实施;1:实施中;2:已实施)", # 实施状态(0:未实施;1:实施中;2:已实施)
    "implPeriod":"实施期限", # 实施期限
}

def commitApply(postData={"id":"1825779965802602497","planReviewTime":"2024-08-22",
                          "assigneeList":["1631112777659588611","15012889770"]}):
    print("【提交复查】")
    return c.ppost("/asi/self/inspection/org/commitReview",postData)

def getTaskInfo(id=g_id,taskId="d5f9da5c-5f92-11ef-95e3-0050569cb713"):
    return c.pget("/asi/self/inspection/org/"+str(id)+"/task/"+taskId)

def dealWf(username,currentStepName,comment,selfParams={}):
    task=flow.findToDoTask(username)[0]
    taskId=task['taskId']
    businessKey=task['businessKey']
    postData={"taskId":taskId,"comment":comment,"entityId":businessKey,"passed":"true"}
    postData.update(selfParams)
    header=flow.getHeader(username)
    flow.dealWfWithHeader(username,currentStepName,postData,header)

def deal():
    print("处理复查")
    dealWf('anjianzhiban','上传复查结果',"ok",{"id":1825779965802602497,"reviewResult":"reviewResult001",
                'taskId': 'b15bd04a-5ec4-11ef-8805-525400123456',"entityId":"1825779965802602497",
                "attachments":[{"name":"fcResulttime1.png","url":"url1"},{"name":"fcResultaaaa1.xlsx","url":"url2"}]})

def remove():
    print("remove")
    c.pget("/asi/self/inspection/org/remove/1825729762123956225",{});

funs=""

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())