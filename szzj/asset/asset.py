#  ===> 资产管理 <===
import sys
sys.path.append("../..")
import common as c

# 提交应用更新申请
def saveSystemAccredit():
    # data = {"systemId":"systemid001" ,"orgIds":"orgid001,orgid002"}
    c.pget("/assetView/systemAccredit?systemId=systemid001&orgIds=orgid0012,orgid002")


# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())