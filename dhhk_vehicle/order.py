#  ===> 技术授权 <===
import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
sys.path.append("../../..")
import common as c

# 获取当前时间
now = datetime.datetime.now()
# 格式化时间为指定字符串格式，这里按照年、月、日、时、分拼接并格式化
time_str = now.strftime('%Y%m%d-%H%M')

g_orderId = "TQ20250212000001"

def test():
    c.pget("/vehicle/order/commuter/list?pageNum=1&pageSize=10")
    #c.pget("/system/role/list")

def commuterList():
    c.ppost("/vehicle/order/commuter/list",{"pageNum":1,"pageSize":2,"orderStatus":"4"})

def commuterAdd(
    postData={
      "orderType": "0",
      "pickUpLocation": "深圳市南山区xxx街道"+time_str,
      "destination": "深圳市福田区xxx街道"+time_str,
      "startPoint": "sz",
      "passengerCount": 2,
      "remark": "这是一条通勤用车申请单"+time_str,
    },
):
    # postData = {"pickUpLocation":"深圳","startPoint":"机场东","destination":"东海航空","passengerCount":"2","remark":"测试sss"}
    return c.ppost("/vehicle/order/commuter/add", postData)

def commuterListSelf():
    c.ppost("/vehicle/order/commuter/listSelfPublished?pageNum=2",{"pageNum":3,"pageSize":3,"paged":True})

def commuterlistSelfGrab():
    c.ppost("/vehicle/order/commuter/listSelfGrab?pageNum=2",{"pageNum":2,"pageSize":3})


def grabOrder(orderId=g_orderId):
    c.pget("/vehicle/order/commuter/"+orderId+"/grab")

def cancelVehicle():
    c.pget("/vehicle/order/TQ20250121000001/cancelVehicle")

def confirmArrival(orderId=g_orderId):
    c.pget("/vehicle/order/commuter/"+orderId+"/confirmArrival")

def confirmEnd(orderId=g_orderId):
    c.pget("/vehicle/order/"+orderId+"/confirmEnd")

def orderUpdate():
    postData = {
        "id": 7295642825011200,
        "techGradeName": "技术授权配置ldk",
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
        "suitPeople": "zhangsan",
        "suitModelList": ["jx1", "jx2"],
        "orderByList": [
            {"id":"7261191222472704","gradeNum":2},
            {"id":"7261203710685184","gradeNum":4},
            {"id":"7261205679779840","gradeNum":6},
        ],
    }
    c.ppost("/order/tech/update", postData)



def orderDel():
    c.pget("/order/tech/remove/6949867782680576?historyDataDealWay=1")


def orderInfo(orderId=g_orderId):
    # return c.pget("/order/tech/" + str(orderId))
    print(orderId + "333")
    return c.pget("/vehicle/order/" + str(orderId))


def commuterExp():
    output = "/home/liudk/Downloads/通勤用车.xlsx"
    c.downLoadPost("/vehicle/order/commuter/export", output)
    print("导出的文件：" + output)


def downFile(fileName="testAttr_20240627132127A001.txt"):
    output = "/home/liudk/Downloads/dhhkUploadFile"
    c.downLoad("/profile/upload/2024/06/27/testUpload_20240627133741A002.txt", output)
    print("导出的文件：" + output)


# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())
