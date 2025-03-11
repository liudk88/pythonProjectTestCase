import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] %(levelname)s [%(filename)s:%(lineno)d:%(funcName)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),  # 输出到控制台
        logging.FileHandler('/home/liudk/pytest.log')  # 输出到文件
    ]
)

def get_logger(name='main'):
    """
    获取指定名称的logger
    :param name: logger名称，默认为'main'
    :return: logger实例
    """
    return logging.getLogger(name)
