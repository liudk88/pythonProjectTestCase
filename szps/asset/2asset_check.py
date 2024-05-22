#  ===> 资产盘点 <===
import sys
sys.path.append("../..")
import common as c
from FunClass import FunClass

# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="5"
c.g_printTable='1'
g_taskId="5864176675332096"

funList=[]
funList.append(FunClass("taskList","【盘点任务列表】")) #0
funList.append(FunClass("taskAdd","【新增盘点任务】")) #1
funList.append(FunClass("taskDel","【删除盘点任务】")) #2
funList.append(FunClass("checkManageList","【盘点任务列表:盘点管理|盘点清单、已盘点、未判断、盘盈资产、盘亏资产、更新资产】")) #3
funList.append(FunClass("taskAssetList","【盘点任务列表:盘点管理|资产列表数据】")) #4

funList.append(FunClass("checkman","【资产盘点（盘点人员）: 任务列表】")) #5
funList.append(FunClass("impRfidReport","【导入rfid报告】")) #6
funList.append(FunClass("rfidCheckOnline","【在线对接盘点结果】")) #7
funList.append(FunClass("expCheckResult","【资产盘点（盘点人员）:导出盘点结果】")) #8
funList.append(FunClass("impCheckResult","【资产盘点（盘点人员）:导入盘点结果】")) #9

def taskList():
    c.pget("/ass/check/task?page=1&limit=10")

def taskAdd():
    postData={"checkPeopleList":["231107clcpxq6mnig66277"],"taskName":"测试盘点结果分析","checkDate":["2024-05-07T16:00:00.000Z","2024-05-22T16:00:00.000Z"],"checkType":"0","checkRangeList":["20180122-1JERCR0GJPR"],"status":"1","planCheckStartTime":"2024-05-07T16:00:00.000Z","planCheckEndTime":"2024-05-22T16:00:00.000Z"}
    c.ppost("/ass/check/add",postData)

def taskDel():
    c.pget("/ass/check/remove?taskIds=6079081770459136")

def checkManageList():
    checkStatus="4"
    c.pget("/ass/check/task/manage/"+g_taskId+"?checkStatus="+checkStatus+"&page=1&limit=10")

def checkman():
    c.pget("/ass/check/task/checkman?page=1&limit=10")

def taskAssetList():
    checkStatus="2"
    assetNameLike=""
    c.pget("/ass/check/taskAssetList?taskId="+g_taskId+"&checkStatus="+checkStatus+"&assetNameLike="+assetNameLike+"&page=1&limit=10")

def assetOverview():
    query={"query.taskNameLike":"K00032"}
    query={}
    c.pget("/ass/check/task",query)

def rfidCheckOnline():
    # 201802010500000003库里是机房2的资产，用来测试变更情况
    params = {"UHF_data": [{"id":0, "epc":"201802010500000011","count":14, "rssi":-53}
                          ,{"id":1, "epc":"DC20230503031882", "count":7, "rssi":-72}
                          ,{"id":2, "epc":"201802010500000009", "count":7, "rssi":-72}
                          ,{"id":3, "epc":"201802010500000006", "count":7, "rssi":-72}
                          ,{"id":4, "epc":"xxxxxx0001", "count":7, "rssi":-72}
                          ,{"id":5, "epc":"xxxxxx0002", "count":7, "rssi":-72}
                          ,{"id":6, "epc":"201802010500000003", "count":7, "rssi":-72}
                          ]
              };
    c.ppost("/ass/rfid/outterCheck",params)

def impRfidReport():
    # files = {'excelFile': open("rfidReport.xls", 'rb')}
    files = {'excelFile': open("/home/liudk/Downloads/szps/机房(Ⅰ)Tag_2024-04-18 16-33-12_043401.xls", 'rb')}
    c.post_file_req('/ass/rfid/'+g_taskId+'/imp',files,{})

def checkedList():
    c.pget("/ass/check/taskAssetList?taskId=5749489507442688&checkStatus=1&page=1&limit=10")

def expCheckResult():
    c.downLoad("/ass/check/excel/expCheckResult?taskId="+g_taskId,"/home/liudk/Downloads/rfid盘点结果.xlsx")

def impCheckResult():
    files = {'excelFile': open("updateCheckResult.xlsx", 'rb')}
    c.post_file_req('/ass/check/excel/'+g_taskId+'/impCheckResult',files,{})

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())