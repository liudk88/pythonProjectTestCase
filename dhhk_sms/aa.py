# 用于存储解析出来的配置信息
config_dict = {}

with open('sms.properties', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()  # 去除首尾空白字符
        if line and not line.startswith('#'):  # 跳过空行和注释行（假设以 # 开头是注释）
            parts = line.split('=', 1)  # 以等号分割，最多分割一次，防止值中也有等号的情况
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                config_dict[key] = value

# 打印解析后的配置信息
for key, value in config_dict.items():
    print(f"{key} = {value}")




