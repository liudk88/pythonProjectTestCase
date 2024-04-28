class FunClass:
    def __init__(self, name, des):  # 构造函数
        self.name = name  # 方法名
        self.des = des  # 方法描述

    def toString(self):  # 实例方法
        return self.name+": "+self.des