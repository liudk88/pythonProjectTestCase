#!python
# encoding: utf-8
import common
import os
import shutil

testData=common.getData()

print('==> test sysoperaDbUpdate <===')

def initSqlFiles(preFileName,finFileName):
    prePath = os.getcwd() + "/dbUpdateSqls/"+preFileName
    finPath = os.getcwd() + "/tmp/"+finFileName
    shutil.copy(prePath,finPath)

sysname=common.getNewSysName()
sysData=common.getSystemByName(sysname)
dbname=common.getNewDbName()
dbData=common.getDbByName(dbname)

# 上传数据库更新sql
# #先复制创建表的sql为当前申请单的sql
creaetSqlFile=testData['dbUpdate_flowSeq']+"_01.sql"
insertSqlFile=testData['dbUpdate_flowSeq']+"_02.sql"
dropSqlFile=testData['dbUpdate_flowSeq']+"_03.sql"

initSqlFiles("t测试运维管理平台-达梦数据库c建表.sql",creaetSqlFile)
initSqlFiles("t测试运维管理平台-达梦数据库i插数据.sql",insertSqlFile)
initSqlFiles("t测试运维管理平台-达梦数据库d删表.sql",dropSqlFile)


# 上传更新sql
fileToken=testData['dbUpdate_flowSeq']+"FLOWM"
common.post_file_request("/attachment/upload",fileToken,"./tmp/"+creaetSqlFile)
common.post_file_request("/attachment/upload",fileToken,"./tmp/"+insertSqlFile)
common.post_file_request("/attachment/upload",fileToken,"./tmp/"+dropSqlFile)

# 提交申请
common.post_db_update_applay(testData['dbUpdate_flowSeq'],sysname,sysData['pkv'],dbData['pkv'],fileToken)







