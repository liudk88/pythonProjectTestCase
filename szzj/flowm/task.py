#  ===> 流程任务 <===
import sys
sys.path.append("../..")
import common as c
from FunClass import FunClass

#获取自定用户、指定流程id的任务
def getTodoTaskId(headers,flowId):
    req = c.get("/view/FView20221Q0V7XZK002/view?FLOW_SEQ="+flowId,headers=headers)
    assert len(req.json()['data']['datas']) > 0,'查询任务结果为空'
    return req.json()['data']['datas'][0]['WTASK_ID']

if __name__ == "__main__":
    c.callSelfFun(globals())