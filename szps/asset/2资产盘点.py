#  ===> 资产盘点 <===
import sys
sys.path.append("../..")
import common as c
from FunClass import FunClass

# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="5"
g_taskId="6079141185200128"

l=[]
l.append(FunClass("taskList","【盘点任务列表】"))
l.append(FunClass("taskAdd","【新增盘点任务】"))
l.append(FunClass("taskDel","【删除盘点任务】"))
l.append(FunClass("checkManageList","【盘点任务列表:盘点管理|盘点清单、已盘点、未判断、盘盈资产、盘亏资产、更新资产】"))
l.append(FunClass("taskAssetList","【盘点任务列表:盘点管理|资产列表数据】"))
l.append(FunClass("rfidCheckOnline","【在线对接盘点结果】"))

def taskList():
    c.pget("/ass/check/task?page=1&limit=10")

def taskAdd():
    postData={"checkPeopleList":["231107clcpxq6mnig66277"],"taskName":"测试盘点结果分析","checkDate":["2024-05-07T16:00:00.000Z","2024-05-22T16:00:00.000Z"],"checkType":"0","checkRangeList":["20180122-1JERCR0GJPR"],"status":"1","planCheckStartTime":"2024-05-07T16:00:00.000Z","planCheckEndTime":"2024-05-22T16:00:00.000Z"}
    c.ppost("/ass/check/add",postData)

def taskDel():
    c.pget("/ass/check/remove?taskIds=6079081770459136")

def checkManageList():
    taskId="5749489507442688"
    checkStatus="1"
    c.pget("/ass/check/task/manage/5749489507442688?taskId="+taskId+"&checkStatus="+checkStatus+"&page=1&limit=10")

def taskAssetList():
    checkStatus=""
    assetNameLike=""
    c.pget("/ass/check/taskAssetList?taskId="+g_taskId+"&checkStatus="+checkStatus+"&assetNameLike="+assetNameLike+"&page=1&limit=10")

def assetOverview():
    query={"query.taskNameLike":"K00032"}
    query={}
    c.pget("/ass/check/task",query)

def rfidCheckOnline():
    params = {"UHF_data": [{"id":0, "epc":"201802010500000011","count":14, "rssi":-53}
                          ,{"id":1, "epc":"DC20230503031882", "count":7, "rssi":-72}
                          ,{"id":2, "epc":"xxxxxx0001", "count":7, "rssi":-72}
                          ,{"id":3, "epc":"xxxxxx0002", "count":7, "rssi":-72}
                          ,{"id":4, "epc":"ldktestRfid001", "count":7, "rssi":-72}
                          ]
              };
    c.ppost("/ass/rfid/outterCheck",params)

def rfidCheckOffline():
    files = {'excelFile': open("rfidReport.xls", 'rb')}
    c.post_file_req('/ass/rfid/5749489507442688/imp',files,{})

def checkedList():
    c.pget("/ass/check/taskAssetList?taskId=5749489507442688&checkStatus=1&page=1&limit=10")



# assetOverview()

#rfid在线盘点
# rfidCheckOnline()


#rfid离线盘点
# rfidCheckOffline()


# =================
#如果gt_lastExeFunIndex有值，那么就以gt_lastExeFunIndex为执行目标
#如果没有，那么提示输入，按输入执行，并更新gt_lastExeFunIndex的值
funlist=''
if len(gt_lastExeFunIndex)==0:
    for index,f in enumerate(l):
        print(str(index)+". "+f.toString())
    funlist = input("请输入需要执行的方法序号，多个以英文逗号隔开:")
    if len(funlist)>0:
        c.put("2资产盘点.py","gt_lastExeFunIndex",funlist) #记住下标，下次直接回车使用
else:
    funlist=gt_lastExeFunIndex

indexArr=funlist.split(",")
for index,f in enumerate(l):
    if str(index) in indexArr:
        print('执行方法=> '+f.name +": "+f.des)
        func = globals()[f.name]
        func()