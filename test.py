import sys
sys.path.append("../..")
import common as c

#下载文件
# r=c.get("/ynwxb/asset/view/exportAllTypeAsset")
# with open("test.xlsx","wb") as code:
#     code.write(r.content)

#断言
# s_age = input("请输入您的年龄:")
# age = int(s_age)
# assert 20 < age < 80, "断言错误提示：年龄不在范围之内！"
# print("您输入的年龄在20和80之间")


# c.pget("/ldktest2/list")

postData={"UPDATE_TIME":None,"MACHINE_ROOM":"","USERA":"温锦展","QT_GWCPU":"","STATUS_lab":"在用","OPERATING_SYSTEM_VERSION":"3","IS_XIN_CHUANG_lab":"否","DOMESTIC_TERMINAL_BRAND":"","TERMINAL_MODEL":"DELL","STATUS":"1","TERMINAL_BRAND":"1","ORGID":"100906152858917e9d27f1b827dae333","BATCH_ENTRY":"0","NETWORK":"0","FOREIGN_CPU_TYPE":"0","FSore20225N0DTMFL002":1232365110391996400,"IP_SEGMENT":"","QT_GCZD":"","ASSET_TYPEC":"TM","CORPORATE_IP_ADDRESS":"","ASSET_TYPEH":"TM","MAC":"","FOREIGN_CPU_TYPE_lab":"Intel（英特尔）","BATCH_ENTRY_lab":"是","TERMINAL_NAME":"西丽街道办非国产终端","ORGID_lab":"南山区","QT_GWZD":"","TERMINAL_BRAND_lab":"国外","PERSON_TELEPHONE":"13168060501","ASSIGNING_CODES":"","DOMESTIC_CPU_TYPE":"","LOCATION":"","TERMINAL_TYPE":"0","QT_ZDLX":"","FSore20225N0DTMHP003":1232365110391996400,"USERA_PHONE":"","FOREIGN_TERMINAL_BRAND_lab":"DELL","FSore20225P07JCEY001":1232365110391996400,"OPERATING_SYSTEM_lab":"国外","FLAG":True,"FILL_ORG":"02ed2661754368ddd17862d328ef316f","CONTRACT_NO":"","NUMBER_OF_TERMINALS":"","PURCHASE_TIME":"","HOST_NAME":"WINDOWS-V0VGFEF","FOREIGN_TERMINAL_BRAND":"1","ASSET_TYPE":"TM","pkv":"1232365110391996419","OPERATING_SYSTEM":"1","REMARK":"新增","TERMINAL_TYPE_lab":"台式电脑","CPU_TYPE":"1","PERSON_LIABLE":"温锦展","NETWORK_lab":"政务网","FSore20225N0DTMDI001":1232365110391996400,"ASSET_CODE":"","RELATED_CONTRACT":"","HOST_SAFETY_PROTECTION_TOOLS":"","IS_XIN_CHUANG":"2","CPU_TYPE_lab":"国外","OPERATING_SYSTEM_VERSION_lab":"Windows","IP_ADDRESS":"","COMPUTER_ORGID":"","QT_GCCPU":""}
c.ppost("/asset/form/AssetForm-TM",postData)