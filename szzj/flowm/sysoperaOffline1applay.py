#!python
# encoding: utf-8
import common

testData=common.getData()

print('==> test 系统下线申请审批流程 <===')

fileToken=testData['update_flowSeq']+"FLOWM"

# 应用更新申请
common.post_app_offline_applay(testData['offline_flowSeq'],fileToken)