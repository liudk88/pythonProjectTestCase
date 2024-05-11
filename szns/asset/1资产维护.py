#  ===> 资产维护 <===
import sys
sys.path.append("../..")
import common as c
from FunClass import FunClass

# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="2"
l=[]
l.append(FunClass("updateAsset","【修改资产】"))
l.append(FunClass("delAsset","【下架】"))
l.append(FunClass("infoAsset","【资产详情】"))

g_assetId='1232365110391996419'

def updateAsset():
    postData={"UPDATE_TIME":None,"MACHINE_ROOM":"","USERA":"温锦展1","QT_GWCPU":"","STATUS_lab":"在用","OPERATING_SYSTEM_VERSION":"3","IS_XIN_CHUANG_lab":"否","DOMESTIC_TERMINAL_BRAND":"","TERMINAL_MODEL":"DELL","STATUS":"1","TERMINAL_BRAND":"1","ORGID":"100906152858917e9d27f1b827dae333","BATCH_ENTRY":"0","NETWORK":"0","FOREIGN_CPU_TYPE":"0","FSore20225N0DTMFL002":1232365110391996400,"IP_SEGMENT":"","QT_GCZD":"","ASSET_TYPEC":"TM","CORPORATE_IP_ADDRESS":"","ASSET_TYPEH":"TM","MAC":"","FOREIGN_CPU_TYPE_lab":"Intel（英特尔）","BATCH_ENTRY_lab":"是","TERMINAL_NAME":"西丽街道办非国产终端","ORGID_lab":"南山区","QT_GWZD":"","TERMINAL_BRAND_lab":"国外","PERSON_TELEPHONE":"13168060501","ASSIGNING_CODES":"","DOMESTIC_CPU_TYPE":"","LOCATION":"","TERMINAL_TYPE":"0","QT_ZDLX":"","FSore20225N0DTMHP003":1232365110391996400,"USERA_PHONE":"","FOREIGN_TERMINAL_BRAND_lab":"DELL","FSore20225P07JCEY001":1232365110391996400,"OPERATING_SYSTEM_lab":"国外","FLAG":True,"FILL_ORG":"02ed2661754368ddd17862d328ef316f","CONTRACT_NO":"","NUMBER_OF_TERMINALS":"","PURCHASE_TIME":"","HOST_NAME":"WINDOWS-V0VGFEF","FOREIGN_TERMINAL_BRAND":"1","ASSET_TYPE":"TM",
              "pkv":g_assetId,"OPERATING_SYSTEM":"1","REMARK":"新增","TERMINAL_TYPE_lab":"台式电脑","CPU_TYPE":"1","PERSON_LIABLE":"温锦展","NETWORK_lab":"政务网","FSore20225N0DTMDI001":1232365110391996400,"ASSET_CODE":"","RELATED_CONTRACT":"","HOST_SAFETY_PROTECTION_TOOLS":"","IS_XIN_CHUANG":"2","CPU_TYPE_lab":"国外","OPERATING_SYSTEM_VERSION_lab":"Windows","IP_ADDRESS":"","COMPUTER_ORGID":"","QT_GCCPU":""}
    # postData={}
    c.ppost("/asset/form/AssetForm-TM",postData)

def delAsset():
    c.pget("/szns/asset/discard/"+g_assetId+"?delFlag=flag&flag=1&viewId=AssetView-MR")

def infoAsset():
    c.pget("/asset/form/AssetForm-TM/view?pkv="+g_assetId+"&flag=1&ectVal=INFO_FORM")

# =================
#如果gt_lastExeFunIndex有值，那么就以gt_lastExeFunIndex为执行目标
#如果没有，那么提示输入，按输入执行，并更新gt_lastExeFunIndex的值
funlist=''
if len(gt_lastExeFunIndex)==0:
    for index,f in enumerate(l):
        print(str(index)+". "+f.toString())
    funlist = input("请输入需要执行的方法序号，多个以英文逗号隔开:")
    if len(funlist)>0:
        c.put("util.py","gt_lastExeFunIndex",funlist) #记住下标，下次直接回车使用
else:
    funlist=gt_lastExeFunIndex

indexArr=funlist.split(",")
for index,f in enumerate(l):
    if str(index) in indexArr:
        print('执行方法=> '+f.name +": "+f.des)
        func = globals()[f.name]
        func()