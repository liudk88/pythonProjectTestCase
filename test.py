import sys
sys.path.append("../..")
import common as c

#下载文件
# r=c.get("/ynwxb/asset/view/exportAllTypeAsset")
# with open("test.xlsx","wb") as code:
#     code.write(r.content)

#断言
# s_age = input("请输入您的年龄:")
# age = int(s_age)
# assert 20 < age < 80, "断言错误提示：年龄不在范围之内！"
# print("您输入的年龄在20和80之间")


# c.pget("/ldktest/list")
# c.ppost("/login/testDecode",{"str":"SckY4x8ZKcXREQLYphA63UfVxg8C+b51BXNqyOSuSBF/OGbrqxrJT56ZOrivquf8HqWooqhbLzESZNFN2bUQdQgLRroUYep1hfFj3eGj2GRxRYEAWLZ58zT3DEfeRo1jYi+UBSJsncRBoDpIHQA4fkgTAFqxWXvpcfuvCn/gOn4="})
c.pget("/asset/backup/myBackupList?startDateStr=2024-05-22&endDateStr=2024-05-31&page=1&limit=10")