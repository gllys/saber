"""atom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from apps.interfaces.views import InterfaceListViewSet
from apps.cases import views as case_views
from apps.cases.views import CaseInfoViewSet
from apps.interfaces import views as interface_views
from apps.scenes import views as scenes_views
from apps.resources import views as envs_views
from operate.login.views import *
from operate.common.views import *
from uitest.views import *

# 实例化router对象
from apps.scenes.views import ScenesViewSet
from apps.resources.views import EnvListViewSet

router = DefaultRouter()

# 注册interface接口路由
router.register('interfaces', InterfaceListViewSet)

# case接口路由
router.register('cases', CaseInfoViewSet)

# scenes接口路由
router.register('scenes', ScenesViewSet)

# env接口路由
router.register('envs', EnvListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # yilei's
    path('user/login/', login),
    path('user/info/', userInfo),
    path('updateMongodbToMysql/', updateMongodbToMysql),
    path('user/register/', register),
    path('update/UiTestCases/', updateUiTestCases),
    path('show/UiTestCases/', getUiTestCase),
    # weixing's
    path('docs/', include_docs_urls(title='测试系统')),
    # update cases and get cases 路由
    path('cases/<pk>/', case_views.CaseUpdateView.as_view()),
    path('interfaces/<pk>/', interface_views.InterfaceDetailView.as_view()),
    # update scenes and get scenes 路由
    path('scenes/<pk>/', scenes_views.ScenesUpdateView.as_view()),
    # update envs and get envs 路由
    path('envs/<pk>/', envs_views.EnvListView.as_view()),
    # 测试连接
    path('env-links/', envs_views.TestLinkView.as_view()),
    # 测试结果接口
    path('test-results/<pk>/', case_views.TestResultDetailView.as_view()),
]
