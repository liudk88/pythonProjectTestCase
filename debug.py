#! /bin/python
import requests
from logger import get_logger
from common import RequestContext, load_yaml_file
import config as g
import json
import os

logger = get_logger('dhhk_vehicle_order')
g_headers = {"Authorization": g.access_token}

def send_request(item, context):
    """发送HTTP请求并记录日志"""
    # 检查send字段，只有send=1时才发送请求
    # if 'send' not in item or item['send'] != 1:
        # logger.info(f"跳过请求: {item.get('title', 'unknown')}\n")
        # return
        
    # 处理变量替换
    url = g.domain + context.replace_variables(item['url'])
    method = item['type'].upper()
    # 如果params不存在或为None，使用空对象
    params = context.replace_params(item.get('params', {}))
    
    # 记录请求信息
    logger.info(f"【 {item['title']} : {item.get('id', 'unknown')} 】")
    logger.info(f"请求地址: {url}")
    logger.info(f"请求类型: {method}")
    logger.info(f"请求参数: {params}")
    
    try:
        if method == 'DOWNLOAD_POST':
            # 处理POST下载
            response = requests.post(url, json=params, headers=g_headers, verify=False)
            if response.status_code == 200:
                file_path = context.replace_variables(item['file_save_dir'])
                with open(file_path, "wb") as code:
                     code.write(response.content)
                logger.info(f"文件已保存到: {file_path}\n")
            else:
                logger.error(f"下载失败，状态码: {response.status_code}\n")
            return
            
        elif method == 'DOWNLOAD_GET':
            # 处理GET下载
            response = requests.get(url, params=params, headers=g_headers, verify=False)
            if response.status_code == 200:
                file_path = context.replace_variables(item['file_save_dir'])
                with open(file_path, "wb") as code:
                     code.write(response.content)
                logger.info(f"文件已保存到: {file_path}\n")
            else:
                logger.error(f"下载失败，状态码: {response.status_code}\n")
            return
        elif method == 'UPLOAD':
            file_path = context.replace_variables(item['upload_file'])
            logger.info(f"上传的文件: {file_path}\n")
            # 上传文件
            fileDatas = {'excelFile': open(file_path, 'rb')}
            response = requests.post(url, headers=g_headers, files=fileDatas, data={}, verify=False)
            return
            
        # 处理普通请求
        if method == 'GET':
            response = requests.get(url, params=params, headers=g_headers, verify=False)
        elif method == 'POST':
            response = requests.post(url, json=params, headers=g_headers, verify=False)
        else:
            logger.error(f"不支持的请求类型: {method}\n")
            return
        
        # 记录响应信息
        logger.info(f"响应状态码: {response.status_code}")
        
        # 根据format_response参数决定是否格式化响应内容
        if item.get('format_response', False):
            try:
                response_json = response.json()
                formatted_response = json.dumps(response_json, indent=2, ensure_ascii=False)
                logger.info(f"响应内容: \n{formatted_response}\n")
            except:
                logger.info(f"响应内容: {response.text}\n")
        else:
            logger.info(f"响应内容: {response.text}\n")
            
        # 保存需要的响应数据
        if 'save' in item and response.status_code == 200:
            context.save_response_data(response.json(), item['save'])
            
    except Exception as e:
        logger.error(f"请求发生错误: {str(e)}\n")

def process_yaml_file(file_config, context):
    """处理单个YAML文件"""
    try:
        if not file_config.get('enabled', False):
            logger.info(f"跳过禁用的文件: {file_config['path']}")
            return
            
        # 从文件路径中提取变量组名
        file_name = os.path.splitext(os.path.basename(file_config['path']))[0]
        group_name = file_name.replace('_debug', '')
        context.current_group = group_name
        
        # 加载YAML文件
        data = load_yaml_file(file_config['path'])
        logger.info(f"开始处理文件: {file_config['name']} ({file_config['path']})")
        
        # 获取请求组列表
        request_groups = file_config.get('request_groups', [])
        
        # 处理每个请求组
        for group in request_groups:
            logger.info(f"开始执行测试组: {group['name']}\n")
            
            # 获取当前组的请求ID列表
            request_ids = group.get('requests', [])
            
            # 创建请求ID到请求数据的映射
            request_map = {item['id']: item for item in data}
            
            # 按照配置文件中的顺序执行请求
            for request_id in request_ids:
                if request_id in request_map:
                    send_request(request_map[request_id], context)
                else:
                    logger.warning(f"找不到请求ID: {request_id}")
                
            logger.info(f"测试组 {group['name']} 执行完成\n")
            
    except Exception as e:
        logger.error(f"处理文件 {file_config['path']} 时发生错误: {str(e)}\n")

def run_all_requests():
    try:
        # 加载主配置文件
        config = load_yaml_file('debug.yaml')
        logger.info("成功读取配置文件，准备进行接口调试...\n")
        
        # 创建请求上下文
        context = RequestContext()
        
        # 处理每个测试文件
        for file_config in config:  # 这里改为直接遍历config
            process_yaml_file(file_config, context)
            
    except Exception as e:
        logger.error(f"发生错误: {str(e)}\n")

def test_vehicle_order():
    """测试机坪用车相关接口"""
    run_all_requests()

if __name__ == '__main__':
    run_all_requests()
