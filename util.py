import common as c
from FunClass import FunClass
import json

# 记住最后一次执行的方法的下标
gt_lastExeFunIndex="0"

l=[]
l.append(FunClass("createFunFormCurl","【把cur命令结果生成函数到文件】"))

def createFunFormCurl():
    with open("draft", 'r') as file:
        lines = file.readlines()
        url=''
        method='get'
        postData={}
        for i, line in enumerate(lines):
            if '--data-raw' in lines[i]:
                method='post'
                postDataStr=lines[i].replace("--data-raw '","").replace("}' \\","}").strip()
                postData=json.loads(postDataStr)
                postDataStr=postDataStr.replace("null","None").replace("true","True")
                # postDataStr=json.dumps(postData, indent=4, ensure_ascii=False)
            elif 'curl' in lines[i]:
                url=lines[i].replace("curl ","").replace("\' \\","").strip()
                inde=url.index("/nisg")+5
                t= len(url)
                url=url[inde:t]

        # mName = input("请输入生成的方法名称:")
        mName ="aaa"
        # print(mName)
        # print(url)
        # print(method)
        # print(postDataStr)
        print("def "+mName+"():")
        if 'get'== method:
            print("    c.pget(\""+url+"\")")
        elif 'post'== method:
            print("    postData="+postDataStr)
            print("    c.ppost(\""+url+"\",postData)")




# =================
#如果gt_lastExeFunIndex有值，那么就以gt_lastExeFunIndex为执行目标
#如果没有，那么提示输入，按输入执行，并更新gt_lastExeFunIndex的值
funlist=''
if len(gt_lastExeFunIndex)==0:
    for index,f in enumerate(l):
        print(str(index)+". "+f.toString())
    funlist = input("请输入需要执行的方法序号，多个以英文逗号隔开:")
    if len(funlist)>0:
        c.put("util.py","gt_lastExeFunIndex",funlist) #记住下标，下次直接回车使用
else:
    funlist=gt_lastExeFunIndex

indexArr=funlist.split(",")
for index,f in enumerate(l):
    if str(index) in indexArr:
        print('执行方法=> '+f.name)
        func = globals()[f.name]
        func()
