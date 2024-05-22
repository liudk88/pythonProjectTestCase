import sys
sys.path.append("..")
import sysoperaGoOnline as flow
sys.path.append("../../..")
import common as c
from FunClass import FunClass

print('==> 系统上线申请流程 集成测试 <===')
gt_lastExeFunIndex="1"
funList=[]
funList.append(FunClass("test","【测试流程申请】"))
funList.append(FunClass("testAqjcEndFlow","【测试安全检查环节终止流程】"))

def test():
    print("111")

def testAqjcEndFlow():
    t_flowId="2024051700011"

    print("【申请流程】")
    flow.apply({"pkv":t_flowId,"CONTENT":"这是一条测试安全检查终止的“系统上线申请审批”单"})

    print("【业务部门项目负责人审批】")
    flow.dealWf("xiangdk",t_flowId,{"DEAL_OPT":"拟同意","nextStep": "nodeAqjc"})

    print("【安全扫描审批】-- 终止流程")
    flow.dealWf("elinkaqsm",t_flowId,{"DEAL_OPT":"完成扫描，发现中高危漏洞","nextStep": "endFlow"})

    req=c.pget("/wf/task?business_id="+t_flowId)
    nodes=req.json()['data']['nodes']
    assert nodes=='流程终止',('流程没有正常终止，安全检查终止流程功能验证不通过！')


# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())