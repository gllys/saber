from operate.common.common import *
from uitest.uiOperate.uiOperate import *
from operate.common.common import *
from atom.models import *
from time import *


def stringToCase(id):
    case = UiTestCasesList.objects.filter(id=id)
    platform = [sqlFilter(case)['platform']][0]
    if [sqlFilter(case)['beginSteps']] is not None:
        steps = str([sqlFilter(case)['beginSteps']][0]).split(',')
        runUiCases(steps, platform)
    if [sqlFilter(case)['steps']] is not None:
        steps = str([sqlFilter(case)['steps']][0]).split(',')
        runUiCases(steps, platform)
    if [sqlFilter(case)['endSteps']] is not None:
        steps = str([sqlFilter(case)['endSteps']][0]).split(',')
        runUiCases(steps, platform)


def runUiCases(steps, platform):
    for i in steps:
        if '打开' in i:
            name = str(i).split("'")
            launchApp(name[1], platform)
        if '点击' in i:
            name = str(i).split("'")
            tap(name[1], platform, resolution=(1080, 1920))
        if '滑动' in i:
            address1 = '1'
            swipe(platform, address1, address2=None, resolution=(1080, 1920))
        if '存在' in i:
            name = '1'
            isExists(name, platform, resolution=(1080, 1920))
        if '等待' in i:
            name = str(i).split("'")
            sleep(int(name[1]))


