#  ===> 技术授权 <===
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
sys.path.append("../..")
import common as c
import os

g_techConfigId = 7091825656934400
g_techManageId = "7092328368386048"


def configAdd(
    postData={
        "techGradeName": "菜单v111",
        "techGradeType": "技术等级类型01",
        "gradeNum": "1",
        "remark": "证件备注",
        "remarkForTrain": "训练备注",
        "remarkForFlair": "资质备注",
        "remarkForFlightExp": "飞行经验备注",
        "reqTrainList": [
            {"groupId": "abc", "trainToDoList": ["100", "200", "300"], "trainDays": 1},
            {
                "groupId": "def",
                "trainToDoList": ["1100", "1200", "1300"],
                "trainDays": 2,
            },
            {
                "groupId": "ghi",
                "trainToDoList": ["2100", "2200", "2300"],
                "trainDays": 3,
            },
        ],
        "reqQualList": [{"qualToNeed": 111}, {"qualToNeed": 222}, {"qualToNeed": 333}],
        "reqFlightExpList": [
            {
                "groupId": "abc",
                "techGradeList": ["100", "200", "300"],
                "flightExp": "jy1",
                "expNum": 1,
            },
            {"groupId": "def", "techGrade": "dj2", "flightExp": "jy2", "expNum": 2},
            {"groupId": "ghi", "techGrade": "dj3", "flightExp": "jy3", "expNum": 3},
        ],
        "validityPeriodUnit": "0",
        "validityPeriod": "2",
        # ,"suitPeopleList":["0","1"]
        "suitPeople": "zhangsan",
        "suitModelList": ["B737"],
    },
):
    return c.ppost("/config/tech/add", postData)


def configUpdate():
    postData = {
        "id": 6893227822166016,
        "techGradeName": "技术授权配置2",
        "techGradeType": "技术等级类型21",
        "gradeNum": "2",
        "remark": "证件备注2",
        "remarkForTrain": "训练备注2",
        "remarkForFlair": "资质备注2",
        "remarkForFlightExp": "飞行经验备注2",
        "reqTrainList": [
            {"groupId": 1, "trainToDo": 22111, "trainDays": 1},
            {"groupId": 1, "trainToDo": 22222, "trainDays": 2},
            {"groupId": 2, "trainToDo": 22333, "trainDays": 3},
        ],
        "reqQualList": [{"qualToNeed": 111}, {"qualToNeed": 222}, {"qualToNeed": 333}],
        "reqFlightExpList": [
            {"groupId": 1, "techGrade": "2dj1", "flightExp": "2jy1", "expNum": 66},
            {"groupId": 1, "techGrade": "dj2", "flightExp": "jy2", "expNum": 2},
            {"groupId": 2, "techGrade": "dj3", "flightExp": "jy3", "expNum": 3},
        ],
        "suitPeopleList": ["4", "5"],
        "suitModelList": ["jx1", "jx2"],
    }
    c.ppost("/config/tech/update", postData)


def configList():
    # c.pget("/config/tech/list?pageNum=1&pageSize=10&suitMode=B738&orderProperty=suitPeople&asc=true&paged=true")
    c.pget("/config/tech/list?pageNum=1&pageSize=10&suitModeIn=B7371&suitModeIn=B7372")
    # c.pget("/manage/empInfo/list?pageSize=10&pageNum=2")


def configDel():
    c.pget("/config/tech/remove/6469968876089344?historyDataDealWay=1")


def configInfo(techConfigId=g_techConfigId):
    return c.pget("/config/tech/" + str(techConfigId))


def configExport():
    output = "/home/liudk/Downloads/技术授权配置.xlsx"
    c.downLoadPost("/config/tech/export", output)
    print("导出的文件：" + output)


def manageAdd(
    postData={
        "techConfigId": g_techConfigId,
        "empNo": "A02220",
        "effectiveTime": "2024-06-27",
        "remark": "技术授权管理备注",
        "remarkForTrain": "训练备注",
        "remarkForFlair": "资质备注",
        "remarkForFlightExp": "飞行经验备注",
        "fileInfos": [134, 135],
        "suitModelList": ["B737"],
    },
):
    postData = {
        "userId": "张雪",
        "effectiveTime": "2024-10-12",
        "empNo": "A02220",
        "remark": "xxldk",
        "suitModelList": ["B737"],
        "techConfigId": g_techConfigId,
        "fileIdList": ["146", "147", "150"],
    }

    res = c.ppost("/manage/tech/add", postData)
    # current_path = os.path.realpath(__file__)
    # 更新当前文件的技术授权管理id
    # g_techManageId="7092328368386048"


def uploadFile(reportName="testUpload.txt"):
    files = {"file": open(reportName, "rb")}
    c.post_file_req("/common/upload", files, {})


def downFile(fileName="testAttr_20240627132127A001.txt"):
    output = "/home/liudk/Downloads/dhhkUploadFile"
    c.downLoad("/profile/upload/2024/06/27/testUpload_20240627133741A002.txt", output)
    print("导出的文件：" + output)


def manageUpdate():
    postData = {
        "id": 6377934436118528,
        "techConfigId": g_techConfigId,
        "userId": "1",
        "empNo": "22testgh5001",
        "effectiveTime": "2024-07-27",
        "remark": "22技术授权管理备注",
        "remarkForTrain": "22训练备注",
        "remarkForFlair": "22资质备注",
        "remarkForFlightExp": "22飞行经验备注",
        "fileInfos": "[{'file':'22testUpload.txt','uri':'/profile/upload/2024/06/27/testUpload_20240627135530A003.txt'},{'file':'22testUpload2.txt','uri':'/profile/upload/2024/06/27/testUpload2_20240627135530A003.txt'}]",
        "suitModelList": ["738"],
    }
    c.ppost("/manage/tech/update", postData)


def techManageInfo():
    c.pget("/manage/tech/" + str(id))


def manageDel():
    c.pget("/manage/tech/remove/6379459594039296")


def manageDisable():
    c.pget("/manage/tech/disable/6379459594039296")


def manageList():
    c.pget("/manage/tech/list?pageNum=1&pageSize=100&orderProperty=empNo&asc=true")


def manageExport():
    output = "/home/liudk/Downloads/技术授权管理.xlsx"
    c.downLoadPost("/manage/tech/export", output)
    print("导出的文件：" + output)


def manageDownTemplate():
    output = "/home/liudk/Downloads/技术授权管理导入模板.xlsx"
    c.downLoadPost("/manage/tech/downTemplate", output)
    print("导出的文件：" + output)


def manageImp():
    files = {"file": open("/home/liudk/Downloads/技术授权管理导入模板.xlsx", "rb")}
    c.post_file_req("/manage/tech/importData?ignoreNotMatchModel=false", files, {})


# manageAdd();
# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())
