import sys
sys.path.append("../..")
import common as c

# 关联资产信息
def querySystemRefAssetList():
    c.pget("/ynwxb/asset/view/querySystemRefAssetList?flag=1&current=1&size=10000&refSystem=1141421512184561667")


querySystemRefAssetList()
# c.pget("/ynwxb/asset/headupdate/test")