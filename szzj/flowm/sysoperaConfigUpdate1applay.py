#!python
# encoding: utf-8
import common

testData=common.getData()

print('==> test 配置更新审批流程 <===')

sysname=common.getNewSysName()
sysData=common.getSystemByName(sysname)

fileToken=testData['configUpdate_flowSeq']+"FLOWM"

common.post_config_update_applay(testData['offline_flowSeq'],sysData['pkv'],fileToken)