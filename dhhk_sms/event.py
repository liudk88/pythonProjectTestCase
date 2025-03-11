import sys
import flow
import datetime
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
sys.path.append("../../..")
import common as c

cfg = {}

with open('/k/codes/ldk/pythonProjectTestCase/dhhk_sms/sms.properties', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()  # 去除首尾空白字符
        if line and not line.startswith('#'):  # 跳过空行和注释行（假设以 # 开头是注释）
            parts = line.split('=', 1)  # 以等号分割，最多分割一次，防止值中也有等号的情况
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                valarr = value.split(',')
                if len(valarr) == 2:
                    value = valarr[0]
                cfg[key] = value

# 获取当前时间
now = datetime.datetime.now()
# 格式化时间为指定字符串格式，这里按照年、月、日、时、分拼接并格式化
time_str = now.strftime('%Y%m%d-%H%M')

print(time_str)
# 新增信息报告-草稿
def saveDraft(
    postData={
        "type": "002",
        "title": "测试自愿报告退回"+time_str,
        "flightDate": "2024-07-08",
        "address": "地点",
        "acReg": "飞机号",
        "flightNo": "航班号",
        "msgType": "1",
        "departure": "起飞点",
        "arrival": "落地点",
        "aircraftNo": "航空器",
        "carNo": "车辆",
        "groundEquipment": "地面设施",
        "aircraftDamage": "1",
        "carDamage": "1",
        "groundDamage": "1",
        "otherReason": "其他原因",
        "edescription": "事件经过",
        "category": "1",
        "appendFiles": "None",
        "occurDate": "2024-07-09 14:00",
        "otherReasonDamage": "1",
        "otherReason": "其他原因",
    },
):
    # postData['id']=6470111007289344
    # postData['title']='编辑后保存草稿222'

    postData["attachments"] = [
        {"name": "time.png", "url": "url1", "uid": 1721353181741, "status": "success"},
        {"name": "aaaa.xlsx", "url": "url2", "uid": 1721353187096, "status": "success"},
    ]

    postData["applicantId"] = 1536269127272902700  # 不允许修改的字段
    postData["deptId"] = "1536266007977406500"  # 不允许修改的字段
    print("提交报告")
    return c.ppost("/asi/inform/saveDraft", postData)


# 提交报告
def submitMsgReport(
    postData={
        "type": "002",
        "title": "测试自愿报告退回"+time_str,
        "flightDate": "2024-07-08",
        "address": "地点",
        "acReg": "飞机号",
        "flightNo": "航班号",
        "msgType": "1",
        "departure": "起飞点",
        "arrival": "落地点",
        "aircraftNo": "航空器",
        "carNo": "车辆",
        "groundEquipment": "地面设施",
        "aircraftDamage": "1",
        "carDamage": "1",
        "groundDamage": "1",
        "edescription": "事件经过",
        "category": "1",
        "appendFiles": "None",
        "occurDate": "2024-07-09 10:30",
        "otherReasonDamage": "1",
        "otherReason": "其他原因",
    },
):
    print("提交报告")
    # postData['id']=6480612416696320
    return c.ppost("/asi/inform/apply", postData)


# 匿名提交报告
def submitAnony(
    postData={
        "type": "002",
        "title": "测试自愿报告知会",
        "flightDate": "2024-07-08",
        "address": "地点",
        "acReg": "飞机号",
        "flightNo": "航班号",
        "msgType": "1",
        "departure": "起飞点",
        "arrival": "落地点",
        "aircraftNo": "航空器",
        "carNo": "车辆",
        "groundEquipment": "地面设施",
        "aircraftDamage": "1",
        "carDamage": "1",
        "groundDamage": "1",
        "otherReason": "其他原因",
        "edescription": "事件经过",
        "category": "1",
        "appendFiles": "None",
    },
):
    postData["code"] = 5
    postData["uuid"] = "273571fe-fd49-49a3-b24c-6e901b2936cc"
    print("提交报告-未验证退出登录时提交")
    return c.ppost("/asi/inform/anonyApply", postData)


def findEventPage(
    postData={
        "pageNum": 1,
        "pageSize": 10,
        "flightDateStart": "2024-07-25 12:30",
        "applyTimeOrderBy": "0",
        "applyTimeEnd": "2025-02-21",
        "applyTimeStart" : "2025-02-13"
    },
):
    print("查询事件列表")
    # return c.ppost("/asi/inform/findPage",postData)
    return c.ppost("/asi/inform/findSelf", postData)


def info(id=7193793692971008):
    print("查看事件")
    return c.pget("/asi/inform/" + str(id))


def delete():
    print("删除事件")
    return c.pget("/asi/inform/remove/7189028047171584")


def submit():
    print("直接提交报告")
    return c.pget("/asi/inform/7193793692971008/submit")


def mergeReport():
    print("直接提交报告")
    return c.pget(
        "/asi/inform/mergeReport?mainReportId=6509482026348544&subReportIds=6509482026348544,6509473975054336"
    )


def findPage(postData={"page": {"limit": 10, "offset": 0}}):
    print("查询待办任务")
    return c.ppost("/task/findRuntimeTasks", postData)


def findAwaits(postData={"page": {"limit": 10, "offset": 0}}):
    print("查询待办任务")
    return c.ppost("/processInst/findAwaits", postData)


def infoTask():
    print("查看详情及流程任务信息")
    return c.pget(
        "/asi/inform/1866831169236090881/task/5148211f-b7c0-11ef-8599-525400123456"
    )


def dealWf(username, currentStepName, comment, selfParams={}):
    header = flow.getHeader(username)
    # 先查询任务
    req = c.post(
        "/task/findRuntimeTasks", {"page": {"limit": 100, "offset": 0}}, header
    )
    row = req.json()["data"]["rows"]
    if len(row) == 0:
        print("没有待办任务")
    else:
        task = row[0]
        # print(task)
        taskId = task["taskId"]
        businessKey = task["businessKey"]
        postData = {
            "taskId": taskId,
            "comment": comment,
            "entityId": businessKey,
            "passed": "true",
        }
        postData.update(selfParams)
        flow.dealWfWithHeader(username, currentStepName, postData, header)


def auditInformation():
    print("审核-信息报告")
    # dealWf(cfg['duty_manager'],'责任部门值班经理',"责任部门值班经理")

    # dealWf(cfg['safe_manage'],'安质经理',"安质经理",{"report": "true"})
    
    # dealWf(cfg['Safety_supervision_duty'],'安监值班',"安监值班",{"passed": "true"})

    # dealWf(cfg['Safety_inspector'],'安监监察员',"安监监察员",{"report": "true","passed":"true"})
    
    # dealWf(cfg['Safety_Leader'],'安监领导',"安监领导",{"passed": "true" , "updateBusinessObj":{"reported": "1"}})

    dealWf(cfg['Security_Information_Officer'],'安全信息员归档',"安全信息员归档",{"passed": "false"})

    # dealWf('A01933','安监副总',"安监副总",{"passed": "false"})
    # dealWf('A01696','安全总监',"安全总监",{"passed": "true"})
    # dealWf('A04950','发起人',"发起人重新提交")

def revokeTask(processId="f1115796-bb83-11ef-9db5-525400123456"):
    print("撤回任务")
    return c.ppost("/asi/task/revokeTask?processId=" + processId, {})

def getCode():
    print("获取验证码")
    c.pget("/auth/code")


def permissionAdd(eventId=6776042860064768, deptIdList=[111], userIdList=[1003]):
    print("事件增加权限范围")
    postData = {"eventId": eventId, "deptIdList": deptIdList, "userIdList": userIdList}
    # postData={"eventId":eventId,"open":"true"} # 设置公开
    return c.ppost("/asi/inform/permission/save", postData)


def copyto(
    businessId=1822820474794590210, deptIdList=[1536265612618117121], userIdList=[1001]
):
    print("抄送")
    postData = {
        "processDefKey": "information",
        "businessId": "6481679049568256",
        "deptIdList": [
            "1536265646474539010",
            "1536265646608756737",
            "1536265646713614338",
        ],
        "copiedUserIdList": ["1557649583822098433", "1689184274680451074"],
        "taskDefKey": "Activity_0i7ea2w",
        "taskId": "8caadf87-4a67-11ef-aaa0-0050569cb713",
    }
    # postData={"eventId":eventId,"deptIdList":deptIdList,"userIdList":userIdList}
    # postData={"businessId":businessId,"copiedUserIdList":userIdList,"deptIdList":deptIdList,"processDefKey":"information"}
    return c.ppost("/asi/act/ru/copyto/copyto", postData)

    # c.ppost("/asi/act/ru/copyto/findSelf",{"pageNum":1,"pageSize":10,"readed":"0"})




def backTask(taskId="e89f643a-5f5a-11ef-b92b-525400123456"):
    print("回退任务")
    return c.ppost("/task/" + taskId + "/backTask", {})


def test():
    print("test")
    c.pget("/task/findCommentsById?id=1825767146983112705", {})


def queryExportableColumn():
    c.pget("/asi/inform/xls/queryExportableColumn")


def downExcel(fileName="sjgl.xlsx"):
    output = "/home/liudk/Downloads/" + fileName
    c.downLoadPost(
        "/asi/inform/xls/expExcel",
        output,
        {"exportPptionList2": ["title", "deptIdLabel", "typeLabel", "flightDate"]},
    )
    print("导出的文件：" + output)


# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())

