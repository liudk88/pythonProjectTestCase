import sys
sys.path.append("../..")
import common as c

def assetOverview():
    query={"query.taskNameLike":"K00032"}
    query={}
    c.pget("/ass/check/task",query)

def rfidCheckOnline():
    params = {"UHF_data":[{"id":0, "epc":"TG-200906309030001","count":14, "rssi":-53}, {"id":1, "epc":"abc1000000000219312e3051xx", "count":7, "rssi":-72}]};
    c.ppost("/ass/rfid/outterCheck",params)

def rfidCheckOffline():
    files = {'excelFile': open("rfidReport.xls", 'rb')}
    c.post_file_req('/ass/rfid/5749489507442688/imp',files,{})


# assetOverview()

#rfid在线盘点
# rfidCheckOnline()


#rfid离线盘点
rfidCheckOffline()