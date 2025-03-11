#  ===> 教员管理 <===
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
sys.path.append("../..")
import common as c


def add():
    data = {
        "instructorType": "1",
        "empNo": "A03421",
        "name": "李立杰",
        "teachingTypeList": ["Pilot","Flight_Attendant"],
        "authorizationTime": "2024-10-20",
        "electronicSignatureId": "1",
        "status": "0",
        "remarks": "测试是否有效",
    }
    c.ppost("/config/instructor/add", data)


def list():
    # c.pget("/config/instructor/list?pageNum=2&pageSize=2&authorizationTimeStart=2024-11-28&authorizationTimeEnd=2024-12-10&orderByColumn=id&isAsc=asc")
    c.pget("/config/instructor/list?pageNum=1&pageSize=1&orderByColumn=instructorType&isAsc=desc&paged=false")
    # c.pget("/config/instructor/list?pageNum=2&pageSize=2&isAsc=asc&paged=false")


def info(id="1869198226665541633"):
    c.pget("/config/instructor/" + id)


def update():
    data = {
        "instructorType": "1",
        "empNo": "A02937",
        "name": "3",
        "teachingTypeList": ["Pilot","Flight_Attendant","Safety_Officer"],
        "authorizationTime": "2024-10-25",
        "electronicSignatureId": "1",
        "remarks": "remarks1",
    }
    data["id"] = "1869198226665541633"
    data["status"] = "3"
    c.ppost("/config/instructor/update", data)


def remove(id="1851143048829906945"):
    c.pget("/config/instructor/remove/" + id)


def export():
    output = "/home/liudk/Downloads/教员信息.xlsx"
    c.downLoadPost("/config/instructor/export", output)
    print("导出的文件：" + output)


def options():
    c.pget("/config/instructor/options")


if __name__ == "__main__":
    c.callSelfFun(globals())
