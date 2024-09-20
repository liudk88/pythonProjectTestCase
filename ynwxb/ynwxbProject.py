#  ===>  <===
import sys
sys.path.append("..")
import common as c
from FunClass import FunClass
import json

# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="2"

funList=[]
funList.append(FunClass("addQuestionTask","【提供给亚信新增任务接口】")) #0
funList.append(FunClass("selectQuestionTask","【提供给亚信查看任务接口】")) #1
funList.append(FunClass("queryQuestionTask","【提供给亚信查询任务列表接口】")) #1

def addQuestionTask():
    print("测试提供给亚信新增任务接口")
    fileDatas = {'file': open("testUpload.txt", 'rb')}
    data={
        "content": "任务内容",
        "name": "任务名称",
        "startDate": "2024-06-03 16:00:00",
        "endDate": "2024-06-04 16:00:00",
        "orgIdList": "98003311",
    }
    c.post_file_req("/outter/work/task/question/add",fileDatas,data)
    # c.ppost("/outter/work/task/question/add",data)

def selectQuestionTask():
    c.pget("/outter/work/task/question/select?workId=6350569471004672")

def queryQuestionTask():
    c.pget("/outter/work/task/question/list?startDateStr=2024-06-26&endDateStr=2024-06-27")

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())