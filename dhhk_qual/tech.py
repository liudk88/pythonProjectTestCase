#  ===> 技术授权 <===
import sys
sys.path.append("../..")
import common as c
from FunClass import FunClass

# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="4"
funList=[]
funList.append(FunClass("techConfigAdd","【新增：技术授权配置】")) #0
funList.append(FunClass("techConfigUpdate","【更新：技术授权配置】")) #1
funList.append(FunClass("techConfigList","【列表：技术授权配置】")) #2
funList.append(FunClass("techConfigDel","【删除：技术授权配置】")) #3
funList.append(FunClass("techConfigInfo","【查看：技术授权配置】")) #4
funList.append(FunClass("techConfigExport","【导出：技术授权配置】")) #5

funList.append(FunClass("techManageAdd","【新增：技术授权管理】")) #6
funList.append(FunClass("uploadFile","【上传 附件】")) #7
funList.append(FunClass("downFile","【下载 附件】")) #8
funList.append(FunClass("techManageAdd","【新增：技术授权管理】")) #9
funList.append(FunClass("techManageInfo","【查看：技术授权管理】")) #10
funList.append(FunClass("techManageUpdate","【更新：技术授权管理】")) #11
funList.append(FunClass("techManageList","【列表：技术授权管理】")) #12
funList.append(FunClass("techManageDel","【删除：技术授权管理】")) #13

g_techConfigId=6893227822166016

def techConfigAdd(postData={"techGradeName":"技术授权配置1","techGradeType":"技术等级类型01","gradeNum":"1","remark":"证件备注"
    ,"remarkForTrain":"训练备注","remarkForFlair":"资质备注","remarkForFlightExp":"飞行经验备注"
    ,"reqTrainList":[{"groupId":1,"trainToDo":111,"trainDays":1},{"groupId":1,"trainToDo":222,"trainDays":2},{"groupId":2,"trainToDo":333,"trainDays":3}]
    ,"reqQualList":[{"qualToNeed":111},{"qualToNeed":222},{"qualToNeed":333}]
    ,"reqFlightExpList":[{"groupId":1,"techGradeList":["100","200","300"],"flightExp":"jy1","expNum":1}
        ,{"groupId":1,"techGrade":"dj2","flightExp":"jy2","expNum":2},{"groupId":2,"techGrade":"dj3","flightExp":"jy3","expNum":3}]
    ,"suitPeopleList":["0","1"]
    ,"suitModelList":["B738"]}):
    return c.ppost("/config/tech/add",postData)


def techConfigUpdate():
    postData={"id":6893227822166016,"techGradeName":"技术授权配置2","techGradeType":"技术等级类型21","gradeNum":"2","remark":"证件备注2"
        ,"remarkForTrain":"训练备注2","remarkForFlair":"资质备注2","remarkForFlightExp":"飞行经验备注2"
        ,"reqTrainList":[{"groupId":1,"trainToDo":22111,"trainDays":1},{"groupId":1,"trainToDo":22222,"trainDays":2},{"groupId":2,"trainToDo":22333,"trainDays":3}]
        ,"reqQualList":[{"qualToNeed":111},{"qualToNeed":222},{"qualToNeed":333}]
        ,"reqFlightExpList":[{"groupId":1,"techGrade":"2dj1","flightExp":"2jy1","expNum":66}
            ,{"groupId":1,"techGrade":"dj2","flightExp":"jy2","expNum":2},{"groupId":2,"techGrade":"dj3","flightExp":"jy3","expNum":3}]
        ,"suitPeopleList":["4","5"]
        ,"suitModelList":["jx1","jx2"]}
    c.ppost("/config/tech/update",postData)

def techConfigList():
    c.pget("/config/tech/list?pageNum=1&pageSize=10&orderProperty=suitPeople&asc=true&paged=true")

def techConfigDel():
    c.pget("/config/tech/remove/6469968876089344?historyDataDealWay=1")

def techConfigInfo(techConfigId=g_techConfigId):
    return c.pget("/config/tech/"+str(techConfigId))

def techConfigExport():
    output="/home/liudk/Downloads/技术授权配置.xlsx"
    c.downLoadPost("/config/tech/export",output)
    print('导出的文件：'+output)

def techManageAdd(postData={"techConfigId":g_techConfigId,"userId":"zhangsan","empNo":"testgh5001","effectiveTime":"2024-06-27","remark":"技术授权管理备注"
    ,"remarkForTrain":"训练备注","remarkForFlair":"资质备注","remarkForFlightExp":"飞行经验备注"
    ,"fileInfos":"[{'file':'testUpload.txt','uri':'/profile/upload/2024/06/27/testUpload_20240627135530A003.txt'},{'file':'testUpload2.txt','uri':'/profile/upload/2024/06/27/testUpload2_20240627135530A003.txt'}]"
    ,"suitModelList":["B738"]}):

    c.ppost("/manage/tech/add",postData)

def uploadFile(reportName="testUpload.txt"):
    files = {'file': open(reportName, 'rb')}
    c.post_file_req('/common/upload',files,{})

def downFile(fileName="testAttr_20240627132127A001.txt"):
    output="/home/liudk/Downloads/dhhkUploadFile"
    c.downLoad("/profile/upload/2024/06/27/testUpload_20240627133741A002.txt",output)
    print('导出的文件：'+output)

def techManageUpdate():
    postData={"id":6377934436118528,"techConfigId":g_techConfigId,"userId":"1","empNo":"22testgh5001","effectiveTime":"2024-07-27","remark":"22技术授权管理备注"
        ,"remarkForTrain":"22训练备注","remarkForFlair":"22资质备注","remarkForFlightExp":"22飞行经验备注"
        ,"fileInfos":"[{'file':'22testUpload.txt','uri':'/profile/upload/2024/06/27/testUpload_20240627135530A003.txt'},{'file':'22testUpload2.txt','uri':'/profile/upload/2024/06/27/testUpload2_20240627135530A003.txt'}]"
        ,"suitModelList":["B738"]}
    c.ppost("/manage/tech/update",postData)

def techManageInfo():
    c.pget("/manage/tech/6379525583745024")

def techManageDel():
    c.pget("/manage/tech/remove/6379459594039296")

def techManageDisable():
    c.pget("/manage/tech/disable/6379459594039296")

def techManageList():
    c.pget("/manage/tech/list?pageNum=1&pageSize=10&orderProperty=empNo&asc=true")

def techManageExport():
    output="/home/liudk/Downloads/技术授权管理.xlsx"
    c.downLoadPost("/manage/tech/export",output)
    print('导出的文件：'+output)

def downTemplate():
    output="/home/liudk/Downloads/技术授权管理导入模板.xlsx"
    c.downLoad("/manage/tech/downTemplate",output)
    print('导出的文件：'+output)

def techManageImp():
    files = {'file': open("/home/liudk/Downloads/技术授权管理导入模板.xlsx", 'rb')}
    c.post_file_req('/manage/tech/importData?ignoreNotMatchModel=true',files,{})

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())