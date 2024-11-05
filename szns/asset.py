import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import common as c


# 资产保存
def save(postData={}):
    # 机房
    # postData={
    #     "ASSET_TYPE": "MR",
    #     "FILL_ORG": "c99f97c33d68ab5ef73d097665bcf412",
    #     "ASSET_TYPEH": "MR",
    #     "SERVER_CENTER_NAME": "ldk测试的机房0012",
    #     "business_usage": "机房业务用途test",
    #     "MACHINE_ROOM_SCALE": 20,
    #     "LOCATION": "机房位置放大成",
    #     "MACHINE_ROOM_CODE": "机房编码001",
    #     "CABINET_NUM_JSON": "{\"ITA\":\"01-08\",\"ITB\":\"01-09\"}",
    #     "MODULE_MSG": [{
    #         "rowIndex": 0,
    #         "moduleNum": "模组编号001",
    #         "assetName": "模组1"
    #     }, {
    #         "rowIndex": 1,
    #         "moduleNum": "模组编号002",
    #         "assetName": "模组2"
    #     }],
    #     "ORGID": "100906152858917e9d27f1b827dae333",
    #     "CONTACT_NAME": "ed2ac75be6fc11ec99d3000c29ac60b7",
    #     "CONTACT_PHONE": "13988888888",
    #     "on_site_admin": "机房现场管理员1",
    #     "on_site_admin_phone": "13988889999",
    #     "SERVER_CENTER_STATUS": "0",
    #     "SERVER_CENTER_MEASURE": "1,2",
    #     "manage_style": "1"
    # }

    # 服务器
    postData = {
        "IS_XIN_CHUANG": "2",
        "ASSET_TYPE": "ES",
        "ASSET_TYPEC": "ES",
        "ASSET_TYPEH": "ES",
        "FILL_ORG": "c99f97c33d68ab5ef73d097665bcf412",
        "IS_XIN_CHUANG_lab": "否",
        "NAME": "ldktest001",
        "PROJECT_NAME": "test",
        "SERVER_BRAND": "0",
        "FOREIGN_SERVER_BRAND": "",
        "DOMESTIC_SERVER_BRAND": "22",
        "EQUIPMENT_MODEL": "222",
        "SERIAL_NUMBER": "222",
        "EXE_TYPE": "0",
        "AI_EXE_TYPE": "",
        "CPU_TYPE": "0",
        "GW_CPU_TYPE": "",
        "GC_CPU_TYPE": "1",
        "QT_GWCPU": "",
        "QT_GCCPU": "",
        "CPU_MODEL": 3,
        "MEMORY_SIZE": 4,
        # "mounting_date": "2024-10-15T16:00:00.000Z",
        "RATED_POWER": 6,
        "device_usage": "4",
        "PURPOSE_OF_USE": "test",
        "STATUS": "1",
        "NETWORK": "1",
        "IP_ADDR": "192.1.1.1",
        "MANAGE_IP": "192.1.1.2",
        "ES_MAC": [{"CID": "ES_MAC", "rowIndex": 0, "VAL": "22"}],
        "ASSET_BELONG": "0",
        "SAFETY_DEPT": "南山区",
        "SAFETY_MAN": "资产组-测试",
        "SAFETY_MAN_PHONE": "13988888881",
        "ORGID": "1355-22WTW3Q9RZ5",
        "PERSON_LIABLE": "90952",
        "PERSON_TELEPHONE": "13510806989",
        "DELIVERY_UNIT": "深圳市信息安全管理中心",
        "DELIVERY_UNIT_FZR": "姚逸滨",
        "DELIVERY_UNIT_FZRDH": "13418628208",
        "COMPUTER_ORGID": "206",
        "MACHINE_ROOM": "1295793770343694336",
        "CABINET": "ITA01",
        "U_BIT": "01-12",
        "NUMBER_OF_U_OCCUPIED": 12,
        "ASSIGN_AREA": "1",
        "is_rented": "1",
        "rent_usage": "test",
        "REMARKS": "test",
    }

    # postData['pkv']=1295793770343694336
    print("保存资产")
    return c.ppost("/asset/form/AssetForm-MR", postData)


# 查看
def info(pkv="987007573750185985"):
    print("查看")
    formId = "AssetForm-SD"
    return c.pget("/asset/form/" + formId + "/view?flag=1&pkv=" + pkv)


# 导出excel数据
def expExcelDatas(
    fileName="assetExp.xlsx", xlsId="FXls20225243KCXS0MR", viewId="AssetView-MR"
):
    output = "/home/liudk/Downloads/" + fileName
    # 机房
    xlsId = "FXls20225243KCXS0MR"
    # xlsId FXls20225243KCXS0ES:实体服务器
    # xlsId FXls20225243KCXS0SD:存储设备

    params = {"ids": "987007573750185985"}
    c.downLoad(
        "/asset/view/excel/" + xlsId + "/exp?flag=1&viewId=" + viewId + "&isTemplate=0",
        output,
        params,
    )
    print("导出的文件：" + output)


# 导入excel数据
def impExcelDatas(fileName="assetExp.xlsx"):
    fileName = "实体服务器.xlsx"
    files = {"excelFile": open("/home/liudk/Downloads/" + fileName, "rb")}
    c.post_file_req(
        "/asset/view/excel/FXls20225243KCXS0ES/imp", files, {"ignoreCheck", "1"}
    )


# 方便直接运行本身文件，单独测试方法
if __name__ == "__main__":
    c.callSelfFun(globals())
