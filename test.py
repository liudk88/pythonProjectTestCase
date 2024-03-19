import sys
sys.path.append("../..")
import re
import common as c

# c.pget("/domain/app/orgManage")

# str="333"
#
# fmtstr='{:8}'.format(str)
# print(fmtstr)



mdTdLen=15

def get_len(string: str):
    """
    获取字符串的长度, 中文是两个字符, 英文是一个字符
    :param string:
    :return:
    """
    length = 0
    for ch in string:
        if '\u4e00' <= ch <= '\u9fa5':  # 是中文字符
            length += 2
        else:
            length += 1
    return length

# 把字符串全部转换为“-”
def repalceToFg(str):
    pattern = "."
    return re.sub(pattern,"-",str)

# 把数组按模板右补充空格
def ljust(arr,templateLens):
    i=0
    rarr=[];
    for key in arr:
        key=key.ljust(templateLens[i],"#")
        rarr.append(key)
        i=i+1

    return rarr
#用竖线分隔符打印数组
def printArrWithFg(arr):
    synx=" | "
    parr=arr[0:mdTdLen]
    str_arr=synx.join(parr)
    str_arr="| "+str_arr+" |"
    print(str_arr)

#获取数组的对象长度
def getArrColLen(objArr):
    colLen={}
    for v in objArr:
        for key, value in v.items():
            if type(value) != dict and type(value) != list:
                s=str(value)
                if colLen.get(key) is None: #还没有包含，应该是第一次计算（第一个对象）
                    colLen[key]=max(get_len(s),get_len(key))
                else:
                    colLen[key]=max(get_len(s),colLen[key])
            else:
                colLen[key]=0

    return colLen

# 获取对象的字段长度
def getObjColLen(obj):
    colLen={}
    for key, value in obj.items():
        if type(value) != dict and type(value) != list:
            s=str(value)
            colLen[key]=max(get_len(key),get_len(s))
    return colLen

def printTableV2(jobj,printTitle,level):
    objLen=getObjColLen(jobj)
    lenArr=[]
    keys=[]
    vals=[]
    fgs=[]

    colLen={}
    title=[]
    valStrs=[]
    i=0
    objs={}

    for key, value in jobj.items():
        len=objLen[key]
        # if len !=0:

        keys.append(key)
        fgs.append(repalceToFg(key))
        vals.append(value)

def printTable0(jobj,printTitle,level):
    colLen={}
    title=[]
    fgs=[]
    valStrs=[]
    i=0
    objs={}
    for key, value in jobj.items():
        title.append(key)
        n=get_len(key)
        if type(value) != dict and type(value) != list:
            s=str(value)
            valStrs.append(s)
            if n < get_len(s):
                n = get_len(s)
        else:
            if type(value) == dict:
                valStrs.append("{}")
            else:
                valStrs.append("[]")

            objs[key]=value
        colLen[i]=n
        i=i+1

    title=ljust(title,colLen)
    valStrs=ljust(valStrs,colLen)

    for key in title:
        fgs.append(repalceToFg(key))

    if printTitle == '1':
        printArrWithFg(title)
        printArrWithFg(fgs)
    printArrWithFg(valStrs)

    for key, value in objs.items():
        print()
        print("# "+key +" L"+str(level))
        if type(value) == dict:
            if len(value)!=0:
                printTable0(value,"1",level+1)
        elif type(value) == list:
            pt="1"
            for v in value:
                printTable0(v,pt,level+1)

def printTable(jobj):
    printTable0(jobj,"1",0)



data={
    "id" : "001",
    "name" : "zhangsan",
    "sex": "男",
    "house": [
        {"name":"主管单位上报的数据a","addr":"addr1"},
        {"name":"h2","addr":"addr2"}
    ]
}

printTable(data)

print(getArrColLen(data['house']))
print(getObjColLen(data))