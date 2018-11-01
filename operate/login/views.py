from django.db.models import QuerySet
from operate.common.common import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from django.views.decorators.csrf import csrf_exempt
import json
import hashlib
import os


@api_view(['POST'])
@csrf_exempt
# 登录
def login(request):
    result = {
        'ERROR': {"message": "用户不存在或者密码错误"},
        'PASS': {"code": 200, "data": {"message": "登陆成功"}},
        'OTHER': {"message": "please use POST"},
    }
    if request.method == 'POST':
        information = json.loads(request.body.decode())
        # get mysql
        usersInfo: QuerySet[Users] = Users.objects.filter(account=information['username'],
                                                          password=information['password'])
        if not usersInfo:
            return Response(result['ERROR'], status=HTTP_404_NOT_FOUND)
        else:
            result['PASS']['data']['token'] = sqlFilter(usersInfo)['token']
            return Response(result['PASS'],  status=HTTP_200_OK)
    else:
        return Response(result['OTHER'], status=HTTP_412_PRECONDITION_FAILED)


@api_view(['GET'])
@csrf_exempt
# userInfo
def userInfo(request):
    result = {
        'PASS': {"code": 200, "data": {"message": "success"}},
        'ERROR': {"message": "用户不存在或者密码错误"},
        'OTHER': {"message": "please use GET"},
    }
    if request.method == 'GET':
        information = stringToDict(request.get_full_path())
        # get mysql
        usersInfo: QuerySet[Users] = Users.objects.filter(token=information['token'])
        if not usersInfo:
            return Response(result['ERROR'], status=HTTP_404_NOT_FOUND)
        else:
            result['PASS']['data']['roles'] = [sqlFilter(usersInfo)['level']]
            result['PASS']['data']['name'] = sqlFilter(usersInfo)['name']
            result['PASS']['data']['avatar'] = sqlFilter(usersInfo)['avatar']
            return Response(result['PASS'], status=HTTP_200_OK)
        return Response(result['OTHER'], status=HTTP_412_PRECONDITION_FAILED)


# 数据入库
def accountIntoSql(account, password, emails='none', name='none', level=5):
    token = hashlib.sha1(os.urandom(24)).hexdigest()
    into = Users(account=str(account), password=str(password), emails=str(emails), name=str(name), level=str(level),
                 token=token)
    into.save()


# 注册
@api_view(['POST'])
def register(request):
    result = {
        'PASS': {"message": "成功注册"},
        'ERROR': {"message": "用户已经注册"},
        'OTHER': {"message": "please use POST"},
    }
    information = json.loads((request.body.decode()))
    if information['emails'] is None:
        information['emails'] = ''
    if information['name'] is None:
        information['name'] = ''
    if information['level'] is None:
        information['level'] = 'admin'
    if information['avatar'] is None:
        information['avatar'] = ''
    if request.method == 'POST':
        if Users.objects.filter(account=information['account'], password=information['password'],
                                emails=information['emails'], name=information['name'], level=information['level']):
            return Response(result['ERROR'], status=HTTP_412_PRECONDITION_FAILED)
        else:
            accountIntoSql(information['account'], information['password'], information['emails'], information['name'],
                           information['level'])
            return Response(result['PASS'], status=HTTP_200_OK)
    else:
        return Response(result['OTHER'], status=HTTP_412_PRECONDITION_FAILED)