import common as c

# 记住最后一次执行的方法的下标
g_lastExeFunIndex="11"

def printFunList(l):
    for index,f in enumerate(l):
        print(f"{index}. {f.toString()}")
        funlist = input("请输入需要执行的方法序号，多个以英文逗号隔开:")
        if len(funlist)>0:
            c.put("../../runtest.py","g_lastExeFunIndex",funlist) #记住下标，下次直接回车使用
        else:
            funlist=g_lastExeFunIndex #没有输入就重复执行上次的
        indexArr=funlist.split(",")
        print(indexArr)
