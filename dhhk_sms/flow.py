import sys
from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
sys.path.append(str(Path(__file__).resolve().parent.parent))
sys.path.append("../../..")
import common as c
import login

t_commonPwd="111111"

def getHeader(username):
    logurl="/auth/login?username="+username+"&password=111111&code=1&uuid==&loginType=1"
    # 以当前请求人登录系统获得登录请求头
    req=login.getHeader(logurl,username,{})
    return {"Authorization":"Bearer "+req.json()['data']}

def findToDoTask(username="zhangsan",postData={"page":{"limit":10,"offset":0}}):
    header=getHeader(username)
    print("查询待办任务")
    req=c.post("/task/findRuntimeTasks",postData,header)
    row=req.json()['data']['rows']
    if len(row) == 0:
        print("没有待办任务")
    else:
        print(row)
        return row

def dealWf(username,currentStepName,postData):
    print("当前流程环节:"+currentStepName+"，"+username+" to do!")
    req=c.ppost("/asi/inform/auditApply",postData,getHeader(username))
    code=req.json()['code']
    if(code == 500):
        print("error："+req.json()['message'])

def dealWfWithHeader(username,currentStepName,postData,header):
    print("当前流程环节:"+currentStepName+"，"+username+" to do!")
    req=c.post("/asi/inform/auditApply",postData,header)
    
    # 法定自查
    # req=c.post("/asi/self/inspection/auditApply",postData,header)
    # req=c.post("/asi/self/inspection/auditApplyWithUpdate",postData,header)
    
    # req=c.post("/asi/self/inspection/org/deal",postData,header)
    # req=c.post("/asi/inform/auditApplyWithUpdate",postData,header)
    code=req.json()['code']
    if(code == 500):
        print("error："+req.json()['message'])

def findAwaits(postData={"page":{"limit":10,"offset":0}}):
    print("查询待办任务")
    return c.ppost("/processInst/findAwaits",postData)
