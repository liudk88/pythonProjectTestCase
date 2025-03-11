#  ===>  <===
import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import common as c

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

def test():
    # url="/zrz/yn/analyse/groupIndexModel?rawMode=true&level=0&modelId=10500718952501248&groupId=530100"
    # 指定州市
    # url=url+"&groupId=530100"
    # url="/zrz/yn/analyse/indicatorList?indicatorId=10500206039453696&level=0&modelId=10500718952501248&groupId=530100"
    # url="/zrz/yn/analyse/indicatorList?level=0&modelId=10500718952501248"
    # url="/sys/orgScope/treeInfo?configId=3531689318961152"
    
    # 获取指标内容 (通过指标id和单位id唯一对应)
    # /zrz/yn/analyse/indicatorList?indicatorId=10500206039453696&level=1&groupId=53000P&modelId=10500718952501248
    # 获取单位指标填写内容
    url="/zrz/indicator/analyse/indicatorList?indicatorId=10500206039453696&level=1&groupId=53000P&modelId=10500718952501248"

    c.pget(url)

# 查询区域得分统计列表
# /work/scope/selectAdminInfo : 查询单位列表
def queryScoreList():
    url="/zrz/yn/analyse/queryCityIndexScoreList"
    data={
        "rawMode": "true",
        "modelId": "10500718952501248",
        "indicatorId":"10500206039453696",
        "groupId": "53000P",
        # "industryList": ['03','04'],
        "orgId" : "44E799B6F8934B97914EA667A479BA22"
    }
    c.ppost(url,data)

# 查询区域下的单位得分统计列表
def queryScoreOrgList():
    url="/zrz/yn/analyse/queryOrgScoreList"
    # url=url+"&orgId=D6F43888D4EF4C3F87B8FF9F01A99D86"
    # url=url+"&focus=2"
    # url=url+"&rectifyFlag=0"
    data={
        "modelId": "10500718952501248",
        # "industryList": ['03','04'],
        "cityCodeList" : ["53000P"],
        "indicatorId" : "10500206039453696",
        # "orgId" : "530000010000"
        "scoreRange" : "0"
    }
    c.ppost(url,data)

def getOrgQuestion():
    url="/zrz/yn/analyse/getOrgQuestion?orgId=44E799B6F8934B97914EA667A479BA22&indicatorId=10654370785710080&modelId=10500718952501248"
    c.pget(url)

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())
