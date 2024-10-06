import sys
sys.path.append("..")
import tech as tech
sys.path.append("../../..")
import common as c


print('==> 技术授权 集成测试 <===')
print('【新增技术授权配置】')
print('- 测试必填校验')
req=tech.techConfigAdd({});
assert req.json()['code']==500, '测试返回编码失败'
assert req.json()['data'][0]=='技术等级名称不能为空！', '测试非空提示失败'
assert req.json()['data'][1]=='技术等级类型不能为空！', '测试非空提示失败'
assert req.json()['data'][2]=='适用人员不能为空！', '测试非空提示失败'
assert req.json()['data'][3]=='适用机型不能为空！', '测试非空提示失败'

print('- 测试正常新增')
index=1
addData={"techGradeName":f"技术授权配置-add-{index}","techGradeType":"1"
    ,"suitPeopleList":["1","2"],"suitModelList":["B738"]
    ,"gradeNum":"1","remark":"证件备注"
    ,"remarkForTrain":"训练备注","remarkForFlair":"资质备注","remarkForFlightExp":"飞行经验备注"
    ,"reqTrainList":[{"groupId":1,"trainToDo":111,"trainDays":1},{"groupId":1,"trainToDo":222,"trainDays":2},{"groupId":2,"trainToDo":333,"trainDays":3}]
    ,"reqQualList":[{"qualToNeed":111},{"qualToNeed":222},{"qualToNeed":333}]
    ,"reqFlightExpList":[{"groupId":1,"techGrade":"dj1","flightExp":"jy1","expNum":1}
        ,{"groupId":1,"techGrade":"dj2","flightExp":"jy2","expNum":2}
        ,{"groupId":2,"techGrade":"dj3","flightExp":"jy3","expNum":3}]
         }
req=tech.techConfigAdd(addData)
techConfigId=req.json()['data']
techConfigId_1=techConfigId;
# 验证新增信息
data=tech.techConfigInfo(techConfigId).json()['data']
assert data['techGradeName']==addData['techGradeName'], '验证失败！'
assert data['gradeNum']==1, '验证失败！'
# todo: 其他字段验证...

index=index+1
print('- 测试新增，不设置等级序号，系统默认值为0')
req=tech.techConfigAdd({"techGradeName":f"技术授权配置-add-{index}","techGradeType":"1"
                           ,"suitPeopleList":["2","1"],"suitModelList":["B738"]})
techConfigId=req.json()['data']
# 验证显示序列
data=tech.techConfigInfo(techConfigId).json()['data']
assert data['gradeNum']==0, '不输入显示序列，默认值应该是0！'


print('- 测试插入到等级序列1之前')
index=index+1
techConfigId=tech.techConfigAdd({"techGradeName":f"技术授权配置-add-{index}","techGradeType":"1","gradeNum":"1"
                           ,"suitPeopleList":["1","2"],"suitModelList":["B738"]}).json()['data']
data=tech.techConfigInfo(techConfigId).json()['data']
assert data['gradeNum']==1, '显示序列按设置的插入，应该是1！'

# 重新查询，其序号应该要加1
data=tech.techConfigInfo(techConfigId_1).json()['data']
assert data['gradeNum']==2, '原来序号为1的数据应该更新为2！'

print('- 测试 技术等级名称、适用人员、技术等级类型、适用机型重复')
index=index+1
req=tech.techConfigAdd({"techGradeName":f"技术授权配置-add-1","techGradeType":"1"
                                    ,"suitPeopleList":["2","1"],"suitModelList":["B738"]})
assert req.json()['code']==500, '测试返回编码失败'
assert req.json()['msg']=='操作失败，已有该技术等级，请重新校验！', '操作失败，已有该技术等级，请重新校验！'


print('- 测试 需要具备的资质、需要通过的训练、飞行经验重复')
index=index+1
addData={"techGradeName":f"技术授权配置-add-{index}","techGradeType":"1"
    ,"suitPeopleList":["1","2"],"suitModelList":["B738"]
    ,"gradeNum":"1","remark":"证件备注"
    ,"reqTrainList":[{"groupId":1,"trainToDo":111,"trainDays":1},{"groupId":1,"trainToDo":111,"trainDays":2},{"groupId":2,"trainToDo":333,"trainDays":3}]
    ,"reqQualList":[{"qualToNeed":111},{"qualToNeed":111},{"qualToNeed":333}]
    ,"reqFlightExpList":[{"groupId":1,"techGrade":"dj1","flightExp":"jy1","expNum":1}
        ,{"groupId":1,"techGrade":"dj2","flightExp":"jy1","expNum":2}
        ,{"groupId":2,"techGrade":"dj3","flightExp":"jy3","expNum":3}]
         }
req=tech.techConfigAdd(addData)

addData={"techConfigId":techConfigId_1,"userId":"zhangsan","empNo":"testgh5001","effectiveTime":"2024-06-27","remark":"技术授权管理备注"
    ,"remarkForTrain":"训练备注","remarkForFlair":"资质备注","remarkForFlightExp":"飞行经验备注"
    ,"fileInfos":"[{'file':'testUpload.txt','uri':'/profile/upload/2024/06/27/testUpload_20240627135530A003.txt'},{'file':'testUpload2.txt','uri':'/profile/upload/2024/06/27/testUpload2_20240627135530A003.txt'}]"
    ,"suitModelList":["B738"]}
req=tech.techManageAdd(addData)


print('【新增技术授权管理】')
