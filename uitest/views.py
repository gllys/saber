from operate.common.common import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from django.views.decorators.csrf import csrf_exempt
import json


@api_view(['POST'])
@csrf_exempt
# 新增ui cases
def updateUiTestCases(request):
    result = {
        'PASS': {"code": 200, "data": {"message": "更新成功"}},
        'OTHER': {"message": "please use POST"},
    }
    if request.method == 'POST':
        information = json.loads(request.body.decode())
        print(not sqlFilter(UiTestCasesList.objects.filter(id=information['id'])))
        if sqlFilter(UiTestCasesList.objects.filter(id=information['id'])):
            if 'caseName' in information.keys():
                caseName = information['caseName']
                UiTestCasesList.objects.filter(id=information['id']).update(caseName=caseName)
            if 'describe' in information.keys():
                describe = information['describe']
                UiTestCasesList.objects.filter(id=information['id']).update(describe=describe)
            if 'beginSteps' in information.keys():
                beginSteps = information['beginSteps']
                UiTestCasesList.objects.filter(id=information['id']).update(beginSteps=beginSteps)
            if 'steps' in information.keys():
                steps = information['steps']
                UiTestCasesList.objects.filter(id=information['id']).update(steps=steps)
            if 'endSteps' in information.keys():
                endSteps = information['endSteps']
                UiTestCasesList.objects.filter(id=information['id']).update(endSteps=endSteps)
            if 'owner' in information.keys():
                owner = information['owner']
                UiTestCasesList.objects.filter(id=information['id']).update(owner=owner)
            if 'showToAll' in information.keys():
                showToAll = information['showToAll']
                UiTestCasesList.objects.filter(id=information['id']).update(showToAll=showToAll)
            if 'project' in information.keys():
                project = information['project']
                UiTestCasesList.objects.filter(id=information['id']).update(project=project)
            if 'platform' in information.keys():
                platform = information['platform']
                UiTestCasesList.objects.filter(id=information['id']).update(platform=platform)
            return Response(result['PASS'], status=HTTP_200_OK)
        else:
            addUiTestCase(caseName=information['caseName'], describe=information['describe'],
                          beginSteps=information['beginSteps'], steps=information['steps'],
                          endSteps=information['endSteps'], owner=information['owner'],
                          showToAll=information['showToAll'], project=information['project'],
                          platform=information['platform'])
            return Response(result['PASS'], status=HTTP_200_OK)
    else:
        return Response(result['OTHER'], status=HTTP_412_PRECONDITION_FAILED)


@api_view(['GET'])
@csrf_exempt
# 返回ui cases
def getUiTestCase(request):
    result = {
        'PASS': {"code": 200},
        'OTHER': {"message": "please use POST"},
    }
    if request.method == 'GET':
        information = stringToDict(request.get_full_path())
        id = information['id']
        result['PASS']['data'] = showUiTestCase(id=id)
        print(result)
        return Response(result['PASS'], status=HTTP_200_OK)
    else:
        return Response(result['OTHER'], status=HTTP_412_PRECONDITION_FAILED)


# 根据id 获取ui cases 信息
def showUiTestCase(id=None):
    if id == 'all':
        caseInfo = UiTestCasesList.objects.filter()
        return sqlFilter(caseInfo)
    else:
        caseInfo = UiTestCasesList.objects.filter(id=id)
        return sqlFilter(caseInfo)


# 数据库增加ui case
def addUiTestCase(caseName, describe, beginSteps, steps, endSteps, owner, project, platform, showToAll=True):
    into = UiTestCasesList(caseName=str(caseName), describe=str(describe), beginSteps=str(beginSteps), steps=str(steps),
                           endSteps=str(endSteps), owner=owner, showToAll=showToAll, project=project, platform=platform)
    into.save()


# 增加ui case set
def updateUiTestCasesSet(request):
    result = {
        'PASS': {"code": 200, "data": {"message": "更新成功"}},
        'OTHER': {"message": "please use POST"},
    }
    if request.method == 'POST':
        information = json.loads(request.body.decode())
        print(not sqlFilter(UiTestCasesSet.objects.filter(id=information['id'])))
        if sqlFilter(UiTestCasesSet.objects.filter(id=information['id'])):
            if sqlFilter(UiTestCasesSet.objects.filter(id=information['id'])):
                if 'testCases' in information.keys():
                    testCases = information['testCases']
                    UiTestCasesSet.objects.filter(id=information['id']).update(testCases=testCases)
                if 'owner' in information.keys():
                    owner = information['owner']
                    UiTestCasesSet.objects.filter(id=information['id']).update(owner=owner)
                if 'name' in information.keys():
                    name = information['name']
                    UiTestCasesSet.objects.filter(id=information['id']).update(name=name)
                if 'showToAll' in information.keys():
                    showToAll = information['showToAll']
                    UiTestCasesSet.objects.filter(id=information['id']).update(showToAll=showToAll)
                if 'describe' in information.keys():
                    describe = information['describe']
                    UiTestCasesSet.objects.filter(id=information['id']).update(describe=describe)
                return Response(result['PASS'], status=HTTP_200_OK)
        else:
            addUiTestCaseSet(testCases=information['testCases'], describe=information['describe'],
                             owner=information['owner'], name=information['name'],
                             showToAll=information['showToAll'])


# 数据库增加ui cases set
def addUiTestCaseSet(testCases, describe, owner, showToAll=True):
    into = UiTestCasesList(testCases=str(testCases), describe=str(describe), owner=str(owner),
                           showToAll=showToAll)
    into.save()


def getUiTestCaseSet(request):
    result = {
        'PASS': {"code": 200},
        'OTHER': {"message": "please use POST"},
    }
    if request.method == 'GET':
        information = stringToDict(request.get_full_path())
        id = information['id']
        result['PASS']['data'] = showUiTestCasesSet(id=id)
        print(result['PASS'])
        return Response(result['PASS'], status=HTTP_200_OK)
    else:
        return Response(result['OTHER'], status=HTTP_412_PRECONDITION_FAILED)


# 根据id 获取ui cases set 信息
def showUiTestCasesSet(id=None):
    if id == 'all':
        caseInfo = UiTestCasesSet.objects.filter()
        return sqlFilter(caseInfo)
    else:
        caseInfo = UiTestCasesSet.objects.filter(id=id)
        return sqlFilter(caseInfo)
