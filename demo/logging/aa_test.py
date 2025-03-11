import logging
import logging.config
import pytest

# logging.config.fileConfig('./log_config.conf')
logger = logging.getLogger(__name__)
# 最终打印的是logger和console的最低级别的合并(两个都设置,前者控制最终输出级别，后者控制当前日志类能输出的级别)
logger.setLevel(level=logging.DEBUG)

#设置级别
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')# 格式控制
# 初始化控制台对象
console = logging.StreamHandler( )# 定义console代表控制台，选择streamHandler
console.setFormatter(formatter)
console.setLevel(level=logging.DEBUG)
# 把控制台对象添加到日志Handler中
logger.addHandler(console)

# 初始化文件对象
handler = logging.FileHandler("/home/liudk/demo.log")# 定义handler代表文件，选择FileHandler
handler.setFormatter(formatter)
logger.addHandler(handler)

def test_log():
    aa="ldk"
    print("测试打印输出")
    logger.debug('测试单元测试内打印日志0')
    logger.info(f'测试单元测试内打印日志0{aa}')
    logger.warning('测试单元测试内打印日志0')
    logger.error('测试单元测试内打印日志0')

