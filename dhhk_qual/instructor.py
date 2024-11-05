#  ===> 教员管理 <===
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
sys.path.append("../..")
import common as c


def add():
    data = {
        "instructorType": "1",
        "empNo": "A04211",
        "name": "3",
        "teachingType": "Pilot",
        "authorizationTime": "2024-10-20",
        "electronicSignatureId": "1",
        "remarks": "测试需要删除的数据",
    }
    c.ppost("/config/instructor/add", data)


def list():
    c.pget("/config/instructor/list?pageNum=1&pageSize=10")


def info(id="1851513140533067778"):
    c.pget("/config/instructor/" + id)


def update():
    data = {
        "instructorType": "1",
        "empNo": "A04180",
        "name": "3",
        "teachingType": "4",
        "authorizationTime": "2024-10-25",
        "electronicSignatureId": "1",
        "remarks": "remarks1",
    }
    data["id"] = "1851435298696851457"
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
