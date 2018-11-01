import pymongo
from operate.common.common import *
import datetime


# 获取mongodb转为字典
def mongodbToDict():
    interfaceList = []
    # mongodb 数据库配置
    client = pymongo.MongoClient('mongodb://192.168.0.206:27017')
    db = client['yapi']
    interface = db['interface']
    for i in interface.find():
        if 'project_id' in i.keys():
            for r in db['project'].find({'_id': i['project_id']}, projection=['name']):
                version = r['name']
        else:
            version = ''
        if 'path' not in i.keys():
            i['path'] = ''
        if 'method' not in i.keys():
            i['method'] = ''
        if 'title' not in i.keys():
            i['title'] = ''
        if 'up_time' not in i.keys():
            i['up_time'] = ''
        if 'desc' not in i.keys():
            i['desc'] = ''
        if 'req_query' not in i.keys():
            i['req_query'] = ''
        if 'req_body_form' not in i.keys():
            i['req_body_form'] = ''
        interfaceList.append(dict(path=i['path'], method=i['method'], title=i['title'], up_time=i['up_time'],
                                  version=version, req_query=i['req_query'], req_body_form=i['req_body_form'],
                                  desc=''))
    return interfaceList


# 把字典数据存储到mysql
def dictToMysql(parameterList):
    for i in parameterList:
        if len(list(InterfaceList.objects.filter(path=str(i['path']), method=str(i['method']), title=str(i['title']),
                                                 up_time=str(i['up_time']), version=str(i['version']),
                                                 req_query=str(i['req_query']), req_body_form=str(i['req_body_form']),
                                                 desc=str(i['desc'])))) is 0:
            into = InterfaceList(path=str(i['path']), method=str(i['method']), title=str(i['title']),
                                 up_time=str(i['up_time']), version=str(i['version']), req_query=str(i['req_query']),
                                 req_body_form=str(i['req_body_form']), desc='')
            into.save()