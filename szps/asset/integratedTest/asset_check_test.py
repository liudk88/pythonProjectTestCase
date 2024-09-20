import sys
sys.path.append("..")
import asset_check as assetcheck
sys.path.append("../../..")
import common as c
from FunClass import FunClass

print('==> 资产盘点 集成测试 <===')
gt_lastExeFunIndex="1"
funList=[]
funList.append(FunClass("testCheckResult","【资产盘点结果测试】"))
funList.append(FunClass("testAssetWiteList","【资产白名单测试】"))

# DELETE FROM ASSET_CHECK_RECORD;
# DELETE FROM ASSET_CHECK_ASSET;
# DELETE FROM ASSET_CHECK_WHITELIST;
# 不加白名单嵌
#                                                     机房
# 1. DC20181010020001	201802010500000014   20180122-1JEQS36BCC8           （白名单）
# 2. DC20181010020002	201802010500000012   20180122-1JEQS36BCC8           （白名单）
# 3. DC20181010020003	201802010500000001   20180122-1JEQS36BCC8
# 4. DC20181010020004	201802010500000002   20180122-1JEQS36BCC8
# 5. DC20181010020007	201802010500000005   20180122-1JEQS36BCC8
# 6. DC20181101030007	/                    20180122-1JEQS36BCC8   盘亏
# 7. DC20181101030008	/                    20180122-1JEQS36BCC8   盘亏
# 8. DC20210812031225
# 9. DC20211222010523	2022091602100018     20190819-5WF1GH6KRP0          （白名单）

# AA100002010000011375 盘盈
# AAA20211124021000505 盘盈
# AAA20220916021000188 盘盈 （和2022091602100018相差了一个尾数）
# AA201802010500000014 已盘点
# AA201802010500000012 已盘点
# DC20210812031225     更新（机房不一样）
# AA201802010500000005 已盘点
# AA201802010500000002 已盘点 和 DC20181010020004对应相同资产
# DC20181010020004     已盘点
# DC20181010020003     已盘点 和 AA201802010500000001对应相同资产
# AA201802010500000001 已盘点

def testCheckResult():
    print('==> 资产盘点结果测试 <===')
    print("【 开始：验证未开始盘点时盘点资产清单数量 】")
    req=assetcheck.taskList({'taskNameLike':'机房(Ⅰ)'})
    assert req.json()['data']['records'][0]['checkTotal']==7, '盘点总数应该是7个'
    assert req.json()['data']['records'][0]['unCheckNum']==7, '未盘点总数应该是7个'
    assert req.json()['data']['records'][0]['checkedNum']==0, '已盘点总数应该是0个'
    assert req.json()['data']['records'][0]['addNum']==0, '盘盈总数应该是0个'
    assert req.json()['data']['records'][0]['delNum']==0, '盘亏总数应该是0个'
    assert req.json()['data']['records'][0]['updateNum']==0, '更新资产总数应该是0个'

    print("【 导入rfid报告，验证导入后结果 】")
    assetcheck.impRfidReport("../rfidReport.xls")
    req=assetcheck.taskList({'taskNameLike':'机房(Ⅰ)'})
    assert req.json()['data']['records'][0]['checkTotal']==7, '盘点总数应该是7个'
    assert req.json()['data']['records'][0]['unCheckNum']==0, '未盘点总数应该是0个'
    assert req.json()['data']['records'][0]['checkedNum']==5, '已盘点总数应该是5个'
    assert req.json()['data']['records'][0]['addNum']==3, '盘盈总数应该是2个'
    assert req.json()['data']['records'][0]['delNum']==2, '盘亏总数应该是2个'
    assert req.json()['data']['records'][0]['updateNum']==1, '更新资产总数应该是1个'

def testAssetWiteList():
    print('==> 测试资产白名单对整个业务的影响 <===')
    print("【 开始：白名单为空 】")
    req=assetcheck.whitelistList()
    assert len(req.json()['data']['records'])==0, '测试白名单查询个数不正确'

    print("【 新增两个非资产资产作为白名单 】")
    assetcheck.whitelistAdd("abc11,def11")
    req=assetcheck.whitelistList()
    assert len(req.json()['data']['records'])==0, '测试白名单新增非资产数据，不会成为白名单'

    print("【 新增三个资产作为白名单 】")
    assetcheck.whitelistAdd("20181010-4L6GZ7HM7EA,20181010-4L6GZ7HSM9E,20211222-Q4M73GLVSOG")
    req=assetcheck.whitelistList()
    assert len(req.json()['data']['records'])==3, '白名单资产应该是3个'
    #验证盘点资产清单、未盘点
    req=assetcheck.taskList({'taskNameLike':'机房(Ⅰ)'})
    assert req.json()['data']['records'][0]['checkTotal']==5, '盘点总数应该是5个(排除了两个机房范围内的，有一个最终是更新的，不是本机房范围内的)'
    assert req.json()['data']['records'][0]['unCheckNum']==5, '未盘点总数应该是5个'

    print("【 有3个资产白名单情况下，导入rfid盘点结果报告，验证盘点结果 】")
    assetcheck.impRfidReport("../rfidReport.xls")
    req=assetcheck.taskList({'taskNameLike':'机房(Ⅰ)'})
    assert req.json()['data']['records'][0]['checkTotal']==5, '盘点总数应该是5个(排除了两个机房范围内的，有一个最终是更新的，但不是本机房范围内的)'
    assert req.json()['data']['records'][0]['unCheckNum']==0, '未盘点总数应该是0个'
    assert req.json()['data']['records'][0]['checkedNum']==3, '已盘点总数由原来的5个去掉两个白名单的，应该是3个'
    assert req.json()['data']['records'][0]['addNum']==3, '盘盈资产总数是rfid里比资产库（白名单也是资产库的一部分，所以不影响）里多出来的，应该是3个'
    assert req.json()['data']['records'][0]['delNum']==2, '盘亏总数应该是2个（道理同盘盈）'
    assert req.json()['data']['records'][0]['updateNum']==1, '更新资产总数应该是1个，有一个被白名单排除了'

    print("todo: 需要验证白名单对管理中每个标签的资产树的统计结果...")
    print("todo: 需要验证盘点结束对盘点管理中每个标签的资产树的统计结果...")

    print("【 测试删除资产白名单 】")
    req=assetcheck.whitelistDelByAssetIds('20181010-4L6GZ7HM7EA,20181010-4L6GZ7HSM9E,20211222-Q4M73GLVSOG,abc11,def11')
    req=assetcheck.whitelistList()
    assert len(req.json()['data']['records'])==0, '白名单已经清空，总数应该是0'

# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())
