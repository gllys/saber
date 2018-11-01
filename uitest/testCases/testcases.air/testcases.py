# -*- encoding=utf8 -*-
__author__ = "wanyilei"

from airtest.core.api import *
from poco.drivers.ios import iosPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

pocoAndorid = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
pocoiOS = iosPoco()

auto_setup(__file__)

