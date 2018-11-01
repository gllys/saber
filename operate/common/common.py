from django.forms.models import model_to_dict
from atom.models import *
import json


# 数据库筛选
def sqlFilter(sqlInfo: object) -> object:
    """
    :param sqlInfo:
    :type info: List[]
    :return:
    """
    info = []
    for i in sqlInfo:
        info.append(model_to_dict(i))
    if len(info) == 1:
        return info[0]
    else:
        return info


# 资源录入
def apiDataConduct(path):
    global apiDataConduct_result
    apiDataConduct_result = []
    file = open(path, encoding='utf-8')
    allList = json.load(file)
    for i in allList:
        # 版本号
        version = i['name']
        # 一个版本下全部api
        apiList = i['list']
        for j in apiList:
            if j['method'] == 'GET':
                if not j['req_query']:
                    apiDataConduct_result.append(
                        dict(path=j['path'], method=j['method'], title=j['title'], up_time=j['up_time'],
                             version=version, parameter='null', desc=''))
                else:
                    parameterGet = []
                    for x in j['req_query']:
                        parameterGet.append({x['name'] + '(' + x['desc'] + ')': x['required']})
                    apiDataConduct_result.append(
                        dict(path=j['path'], method=j['method'], title=j['title'], up_time=j['up_time'],
                             version=version, parameter=parameterGet, desc=''))
            elif j['method'] == 'POST':
                if not j['req_body_form']:
                    apiDataConduct_result.append(dict(path=j['path'], method=j['method'], title=j['title'],
                                                      up_time=j['up_time'], version=version, parameter='null', desc=''))
                else:
                    parameterPost = []
                    for z in j['req_body_form']:
                        parameterPost.append({z['name'] + '(' + z['desc'] + ')': z['required']})
                    apiDataConduct_result.append(
                        dict(path=j['path'], method=j['method'], title=j['title'], up_time=j['up_time'],
                             version=version, parameter=parameterPost, desc=''))
    return apiDataConduct_result


# 新增ui测试用例
def addUITestCase(parameterList):
        if len(list(UiTestCasesList.objects.filter(path=str(parameterList['path']), method=str(parameterList['method']),
                                                   title=str(parameterList['title']), up_time=str(parameterList['up_time']), version=str(parameterList['version']),
                                                 req_query=str(parameterList['req_query']), req_body_form=str(parameterList['req_body_form']),
                                                 desc=str(parameterList['desc'])))) is 0:
            into = InterfaceList(path=str(parameterList['path']), method=str(parameterList['method']), title=str(parameterList['title']),
                                 up_time=str(parameterList['up_time']), version=str(parameterList['version']), req_query=str(parameterList['req_query']),
                                 req_body_form=str(parameterList['req_body_form']), desc='')
            into.save()


# 接口字符串参数转变成字典
def stringToDict(parameters):
    """
    :type parameters: object
    :param parameters:
    :type info: List[]
    :return: Dict{}
    """
    result = {}
    if '?' in parameters:
        params = str(parameters).split('?')[1]
    else:
        params = str(parameters)
    for i in str(params).split('&'):
        result[i.split('=')[0]] = i.split('=')[1]
    return result
