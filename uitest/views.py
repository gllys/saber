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
    print(request.get_full_path())
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


def showUiTestCase(id=None):
    if id == 'all':
        caseInfo = UiTestCasesList.objects.filter()
        return sqlFilter(caseInfo)
    else:
        caseInfo = UiTestCasesList.objects.filter(id=id)
        return sqlFilter(caseInfo)


def addUiTestCase(caseName, describe, beginSteps, steps, endSteps, owner, project, platform, showToAll=True):
    into = UiTestCasesList(caseName=str(caseName), describe=str(describe), beginSteps=str(beginSteps), steps=str(steps),
                           endSteps=str(endSteps), owner=owner, showToAll=showToAll, project=project, platform=platform)
    into.save()
