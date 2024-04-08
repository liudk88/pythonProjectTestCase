domain="http://localhost:9031/nisg"
# domain="http://192.168.99.59:8400/nisg"
access_token="faf88d0c-79db-4d39-9c10-c8c35c2c1b49"

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