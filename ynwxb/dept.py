import sys
import datetime

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import common as c

# 获取当前时间
now = datetime.datetime.now()

# 格式化时间为指定字符串格式，这里按照年、月、日、时、分拼接并格式化
time_str = now.strftime('%Y%m%d-%H%M')

print(time_str)

# 提交报告
def submit(
    postData={
        "pkv": "0D5744C53968489ABA7FA4759AB29EFF",
        "ORGANIZATION_NAME": "ldktest机构全称",
        "ORG_SHORT_NAME": "ldk机构简称"+time_str,
        "ORGANIZATION_CODE": "ldk统一社会信用代码",
        "REGION_LOCATION": "ldk区域位置",
        "ADDRESS": "ldk机构具体地址",
        "CITY_CODE": "ldk行政区划编码",
        "CONTCAT_NAME": "ldk应急联系人名称",
        "CONTCAT_PHONE": "13900222222",
        "CONTCAT_MAIL": "17792111@qq.com",
    },
):
    print("提交单位更新审核")
    return c.ppost("/dep/log/submit", postData)

def superList():
    c.pget("/dep/log/superior/list")

def subordinateList():
    c.pget("/dep/log/subordinate/list")

def info():
    c.pget("/dep/log/1862070165830688769")

def deptInfo():
    c.pget("/dep/log/deptInfo")
    
def audit():
    c.ppost("/dep/log/audit",{"id":"1862320361680416770","isPass":"true"})

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())
