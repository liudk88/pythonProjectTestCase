#!python
# encoding: utf-8
import common
import time

assetType="MR"
mrName="ldktestMr_"+time.strftime("%Y%m%d%H%M%S",time.localtime())
#机房安全措施
jfaqcs=common.getRandomValsStr([0,1,2,3,4,5,6,7,8,9,10])
orgid=common.getSingleVal(['1354-22WQ7IS2IOJ','1355-22WTW3Q9RZ5','1356-22WURMFZLIC','1357-22WV9LVWLWS','1358-22WVMRQUCUQ','1359-22WW6ISSLK3','1360-22WWL31EC9T','1361-22WX1IQSJFQ','1362-22WXIZ0RKSL','1363-22WXVPX2WKA'])
data={
    "SERVER_CENTER_NAME": mrName,
    "MACHINE_ROOM_SCALE": "22",
    "MACHINE_ROOM_CODE": "22",
    "ORGID": orgid,
    "LOCATION": "机房位置",
    "CONTACT_NAME": "张三",
    "CONTACT_PHONE": "13999999999",
    "SERVER_CENTER_STATUS": "1",
    "SERVER_CENTER_MEASURE": jfaqcs,
    "ASSET_TYPE": assetType,
    "ASSET_TYPEH": assetType
}
# print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print "==> 测试新增机房 <==="
# common.post_asset(assetType,data)

testData=common.getData()
print "==> 测试导出excel <==="
outputpath=testData['output_dir']+"/MR.xlsx"
# common.down_file("/view/excel/FXls20225243KCXS0MR/exp?flag=1&viewId=AssetView-MR&isTemplate=0&ids=1082742971989753856",{},outputpath)

common.down_file("/view/excel/FXls20225243KCXS0MR/exp?flag=1&viewId=AssetView-MR&isTemplate=0",{},outputpath)