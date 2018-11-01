from airtest.core.api import *
from operate.common.common import *
from atom.models import *
from time import sleep
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

pocoAndorid = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#pocoiOS = iosPoco()

r = open('../testCases/testcases.air/testcases.py', 'a+')


# 打开app
def launchApp(name, platform):
    appName = AppName.objects.filter(name=name, platform=platform)
    if sqlFilter(appName):
        start_app(sqlFilter(appName)['appName'])
    else:
        result = '{error: appName wrong}'
        return result


# 点击
def tap(name, platform, resolution=(1080, 1920)):
    if '.png' not in str(name):
        if platform == 'iOS':
            pocoiOS(text=name).click()
        else:
            pocoAndorid(text=name).click()
    else:
        touch(Template(name, resolution=resolution))


# 滑动
def swipe(platform, address1, address2=None, resolution=(1080, 1920)):
    if '.png' not in str(address1):
        if platform == 'iOS':
            pocoiOS(text=address1).drag_to(pocoiOS(text=address2))
        else:
            pocoAndorid(text=address1).drag_to(pocoAndorid(text=address2))
    else:
        swipe(Template(address1, resolution=resolution), vector=[0.2933, 0.1815])


# 判断存在
def isExists(name, platform, resolution=(1080, 1920)):
    if '.png' not in str(name):
        if platform == 'iOS':
            pocoiOS(text=name).exists()
        else:
            pocoAndorid(text=name).exists()
    else:
        assert_exists(Template(name, record_pos=(-0.324, 0.128), resolution=resolution), name)


# 判断等于
def isEqual(name, value, platform):
    if platform == 'iOS':
        pocoiOS(text=name).exists()
    else:
        pocoAndorid(text=value).exists()




# addUiTestCase("11",'we',"打开'海风智学中心',等待'10'", "点击'微课'", '', 'wanyl', '', 'Android')