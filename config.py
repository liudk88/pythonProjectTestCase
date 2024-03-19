domain="http://localhost:9031/nisg"
# domain="http://192.168.99.59:8400/nisg"
access_token="cb31ea34-1511-46b2-9d41-fcabe3fab9b5"

# 提供修改当前配置参数的方法
def put(paramName,value):
    with open('config.py', 'r') as file:
        lines = file.readlines()
    # 修改行内容
    for i, line in enumerate(lines):
        if paramName in lines[i]:
            lines[i] = ""+paramName+"=\""+value+"\"\n"
    # 打开文件进行写入
    with open('config.py', 'w') as file:
        file.writelines(lines)