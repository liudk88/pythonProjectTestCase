import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import common as c


#【新增】
def add(postData={"userPositionId":"123456"}):
    print("【新增】")

    return c.ppost("/sys/user/position/manage/batchAdd",postData)


# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())