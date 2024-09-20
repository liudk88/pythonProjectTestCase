import sys
sys.path.append("..")
import event as event
sys.path.append("../../..")
import common as c

print('==> 事件管理 集成测试 <===')

print("测试： 新增草稿和查看")

postData={"type":"001","title":"测试信息报告222211","flightDate":"2024-07-08","address":"地点","acReg":"飞机号","flightNo":"航班号","msgType":"1",
          "departure":"起飞点","arrival":"落地点","aircraftNo":"航空器","carNo":"车辆","groundEquipment":"地面设施","aircraftDamage":"1",
          "carDamage":"1","groundDamage":"1","otherReason":"其他原因","edescription":"事件经过","category":"1","appendFiles":"None",
          "occurDate":"2024-07-09","otherReasonDamage":"1","otherReason":"其他原因"}

# res=event.saveDraft(postData)

c.g_printTable=0
c.g_printJson=0
id=6509368853082112
res=event.get(id)
