# encoding: utf-8
import config as g
import json
import requests
import time
import os
import random
import sys
import re
from datetime import datetime
import yaml
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
from logger import get_logger

logger = get_logger('common')

# 获取当前时间
now = datetime.now()
# 格式化为 yyyyMMddHHmm 格式
ftime = now.strftime("%Y%m%d%H%M_%S")


def getVals(valArr, numberOfTimes):
    result = []
    for i in range(numberOfTimes):
        index = random.randint(0, len(valArr) - 1)
        val = valArr[index]
        if val not in result:
            result.append(val)
    result.sort()
    return result


def getRandomVals(valArr):
    numberOfTimes = random.randint(0, len(valArr))
    return getVals(valArr, numberOfTimes)


def getRandomValsStr(valArr):
    numberOfTimes = random.randint(0, len(valArr))
    result = getVals(valArr, numberOfTimes)
    return ",".join(str(i) for i in result)


# charset参数可以限制文件编码格式
def post_file_request(url, fileToken, file_path):
    url = getUrl(url)
    data = {"fileToken": fileToken}
    if os.path.exists(file_path):
        if url not in [None, ""]:
            if url.startswith("http") or url.startswith("https"):
                files = {"file": open(file_path, "rb")}
                res = requests.post(url, headers=g_headers, files=files, data=data)
                return {"code": 0, "res": res}


def post_asset(assetType, postData):
    url = getUrl("/form/AssetForm-" + assetType)
    req = requests.post(url=url, json=postData, headers=g_headers)
    print(req.text)
    data = req.json()
    if data["code"] == 0:
        print("test success!")
    else:
        print("test fail!")


# ============= 20240314 add =============
g_printTable = "0"
g_printJson = "1"
g_headers = {"Authorization": g.access_token}

mdTdLen = 50


def get_len(string: str):
    """
    获取字符串的长度, 中文是两个字符, 英文是一个字符
    :param string:
    :return:
    """
    length = 0
    for ch in string:
        if "\u4e00" <= ch <= "\u9fa5":  # 是中文字符
            length += 2
        else:
            length += 1
    return length


# 把字符串全部转换为"-"
def repalceToFg(str):
    pattern = "."
    return re.sub(pattern, "-", str)


# 把数组按模板右补充空格
def ljust(arr, templateLens):
    i = 0
    rarr = []
    for key in arr:
        key = key.ljust(templateLens[i], " ")
        rarr.append(key)
        i = i + 1

    return rarr


# 用竖线分隔符打印数组
def printArrWithFg(arr):
    synx = " | "
    arrlen = len(arr)
    parr = arr[0:mdTdLen]
    str_arr = synx.join(parr)
    str_arr = "| " + str_arr + " |"
    if arrlen > mdTdLen:
        str_arr = str_arr + "······ |"
    print(str_arr)


def printTable(jobj, printTitle, level):
    colLen = {}
    title = []
    fgs = []
    valStrs = []
    i = 0
    objs = {}
    for key, value in jobj.items():
        title.append(key)
        n = get_len(key)
        if type(value) != dict and type(value) != list:
            s = str(value)
            valStrs.append(s)
            if n < get_len(s):
                n = get_len(s)
        else:
            if type(value) == dict:
                valStrs.append("{}")
            else:
                valStrs.append("[]")

            objs[key] = value
        colLen[i] = n
        i = i + 1

    title = ljust(title, colLen)
    valStrs = ljust(valStrs, colLen)

    for key in title:
        fgs.append(repalceToFg(key))

    if printTitle == "1":
        printArrWithFg(title)
        printArrWithFg(fgs)
    printArrWithFg(valStrs)

    for key, value in objs.items():
        print()
        print("# " + key + " L" + str(level))
        if type(value) == dict:
            if len(value) != 0:
                printTable(value, "1", level + 1)
        elif type(value) == list:
            pt = "1"
            for v in value:
                printTable(v, pt, level + 1)
                pt = "0"


# -- begin 重新封装get请求
def get(url, params={}, headers={}):
    print("▶ 请求地址： " + url)
    if len(headers) == 0:
        headers = g_headers
    return requests.get(
        url=g.domain + url, params=params, headers=headers, verify=False
    )


# def get(url):
#     print("请求地址： "+url)
#     return requests.get(url=g.domain+url,headers=headers,verify = False)


def post(url, params, headers={}):
    print("▶ 请求地址： " + url + "，请求参数：" + str(params))
    if type(headers) == dict and len(headers) == 0:
        headers = g_headers
    return requests.post(url=g.domain + url, json=params, headers=headers, verify=False)


# 以formData的方式提交参数
def formPost(url, params):
    print("请求地址： " + url)
    return requests.post(
        url=g.domain + url, data=params, headers=g_headers, verify=False
    )


def putUrl(url, params, headers={}):
    print("请求地址： " + url)
    if type(headers) == dict and len(headers) == 0:
        headers = g_headers
    return requests.put(url=g.domain + url, json=params, headers=headers, verify=False)


# --
# def pget(url):
#     res=get(url)
#     print("返回信息：")
#     jprint(res.json())
#     printTable(res.json(),"1",0)
#     return res


def pget(url, params={}):
    res = get(url, params)
    if g_printJson == "1":
        print("◀ 返回信息：")
        jprint(res.json())
    if g_printTable == "1":
        printTable(res.json(), "1", 0)
    return res


def ppost(url, params, headers={}):
    res = post(url, params, headers)
    print("◀ 返回信息：")
    jprint(res.json())
    if g_printTable == "1":
        printTable(res.json(), "1", 0)
    return res


def pput(url, params, headers={}):
    res = putUrl(url, params, headers)
    print("返回信息：")
    jprint(res.json())
    return res


def pformPost(url, params):
    res = formPost(url, params)
    print("返回信息：")
    jprint(res.json())
    return res


# -- end
# 获取命令行参数（去掉命令文件名本身）
def args():
    return sys.argv[1:]


# 格式化打印json对象
def jprint(jsonData):
    formatted_json = json.dumps(jsonData, indent=2, ensure_ascii=False)
    print(formatted_json)


# charset参数可以限制文件编码格式
def post_file_req(url, fileDatas, data):
    res = requests.post(g.domain + url, headers=g_headers, files=fileDatas, data=data)
    print("返回信息：")
    jprint(res.json())
    return res


# 下载文件方法
def downLoad(url, saveDir, params={}):
    r = get(url, params)
    with open(saveDir, "wb") as code:
        code.write(r.content)


def downLoadPost(url, saveDir, params={}):
    r = post(url, params)
    with open(saveDir, "wb") as code:
        code.write(r.content)


# 提供修改文件参数的方法
def put(pyFile, paramName, value):
    with open(pyFile, "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if paramName in lines[i]:
            # 修改行内容
            lines[i] = "" + paramName + '="' + str(value) + '"\n'
    # 打开文件进行写入
    with open(pyFile, "w") as file:
        file.writelines(lines)

## ===========================文件方法快速调用 begin
# 一. 如果执行命令有指定参数f，那么按f指定的函数执行
# 终端运行格式: python ./xxx.py -f 函数1,函数2...
# idea编辑命令，在Parammeters里填写 -f 函数1,函数2...
# 二. 一个py文件定两个个全局变量gt_lastExeFunIndex和funList，前者表示需要执行的函数下标（多个以英文逗号隔开），后者是供调用的函数列表
# 如果gt_lastExeFunIndex有值，那么就以gt_lastExeFunIndex为执行列表中对应的函数目标
# 如果没有，那么提示输入，按输入执行，并更新gt_lastExeFunIndex的值
def callSelfFun(caller):
    args = sys.argv[1:]
    callFunList = ""
    if len(args) == 2:
        callFunList = args[1].split(",")
    elif "funs" in caller and caller["funs"] != "":
        callFunList = caller["funs"].split(",")

    if callFunList != "":
        for index, f in enumerate(callFunList):
            print("执行方法=> " + f)
            func = caller[f]
            func()
    else:
        exeFunIndex = caller["gt_lastExeFunIndex"]  # 获取调用者的调用函数下标
        funList = caller["funList"]  # 获取调用者的函数列表
        if len(exeFunIndex) == 0:
            for index, f in enumerate(funList):
                print(str(index) + ". " + f.toString())
            exeFunIndex = input("请输入需要执行的方法序号，多个以英文逗号隔开:")
            if len(exeFunIndex) > 0:
                put(
                    caller["__file__"], "gt_lastExeFunIndex", exeFunIndex
                )  # 修改源文件调用函数下标，下次直接回车使用

        indexArr = exeFunIndex.split(",")
        for index, f in enumerate(funList):
            if str(index) in indexArr:
                print("执行方法=> " + f.name + ": " + f.des)
                func = caller[f.name]
                func()


## ===========================文件方法快速调用 end

def _get_group_names():
    """通过扫描配置文件获取所有组名"""
    groups = set()
    try:
        # 加载debug.yaml获取所有配置文件路径
        with open('debug.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            for file_config in config:
                if file_config.get('enabled', False):  # 只处理启用的配置(不设置表示不启用)
                    file_path = file_config['path']
                    # 从文件名中提取组名
                    file_name = os.path.splitext(os.path.basename(file_path))[0]
                    group_name = file_name.replace('_debug', '')
                    groups.add(group_name)
    except Exception as e:
        logger.error(f"获取组名失败: {str(e)}")
    return groups

class RequestContext:
    def __init__(self, current_group=None):
        self.current_group = current_group
        self.global_vars_file = 'global_vars.json'
        self.variables = self._load_global_vars()
        
    def _load_global_vars(self):
        """加载全局变量"""
        try:
            if os.path.exists(self.global_vars_file):
                with open(self.global_vars_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:  # 如果文件不为空
                        try:
                            return json.loads(content)
                        except json.JSONDecodeError:
                            logger.error("全局变量文件格式错误，将重置为默认结构")
                
            # 如果文件不存在、为空或格式错误，创建默认结构
            default_vars = {}
            for group in _get_group_names():
                default_vars[group] = {}
                
            # 如果没有找到任何组，至少创建一个空结构
            if not default_vars:
                default_vars = {"default_group": {}}
                
            self._save_global_vars(default_vars)
            return default_vars
        except Exception as e:
            logger.error(f"加载全局变量文件失败: {str(e)}")
            return {}
            
    def _save_global_vars(self, vars_data=None):
        """保存全局变量"""
        try:
            with open(self.global_vars_file, 'w', encoding='utf-8') as f:
                json.dump(vars_data or self.variables, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"保存全局变量文件失败: {str(e)}")
    
    def save_response_data(self, response_data, save_rules):
        """保存响应数据到变量"""
        if not self.current_group:
            return
            
        group_vars = self.variables.get(self.current_group, {})
        for var_name, path in save_rules.items():
            if path.startswith('$.'):
                jsonpath_expr = parse(path)
                matches = jsonpath_expr.find(response_data)
                if matches:
                    group_vars[var_name] = matches[0].value
                    logger.info(f"保存变量 {self.current_group}.{var_name}: {matches[0].value}")
        
        self.variables[self.current_group] = group_vars
        self._save_global_vars()
    
    def replace_variables(self, text):
        """替换字符串中的变量引用"""
        if not isinstance(text, str):
            return text
            
        def replace_var(match):
            var_path = match.group(1)
            # 检查是否指定了组名
            if '.' in var_path:
                group, var_name = var_path.split('.')
                return str(self.variables.get(group, {}).get(var_name, ''))
            # 没有指定组名，使用当前组
            elif self.current_group:
                return str(self.variables.get(self.current_group, {}).get(var_path, ''))
            return ''
            
        return re.sub(r'\${([\w.]+)}', replace_var, text)

    def replace_params(self, params):
        """递归替换参数中的变量"""
        if isinstance(params, dict):
            return {k: self.replace_params(v) for k, v in params.items()}
        elif isinstance(params, list):
            return [self.replace_params(v) for v in params]
        else:
            return self.replace_variables(params)

def load_yaml_file(file_path):
    """加载YAML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"错误：找不到文件 {file_path}")
        raise
    except yaml.YAMLError as e:
        logger.error(f"错误：YAML文件格式不正确: {str(e)}")
        raise
