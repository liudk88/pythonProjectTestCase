#!python
# encoding: utf-8
import common

testData=common.getData()

print('==> test 应用更新申请流程 <===')

sysname=common.getNewSysName()
sysData=common.getSystemByName(sysname)

# !!!如果不是从测试资源申请开始，那么注释掉下行（不需要创建应用服务器）
common.createApplaySystem("xiangdk",sysData['pkv'])

# 上传系统更新包
projectName="nisg"
fileToken=testData['update_flowSeq']+"FLOWM"
common.post_file_request("/attachment/upload",fileToken,projectName+".zip")

# 应用更新申请
common.post_app_update_applay(testData['update_flowSeq'],sysname,sysData['pkv'],projectName,fileToken)