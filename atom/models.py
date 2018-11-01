from datetime import datetime
from django.db import models


# 用户信息
class Users(models.Model):
    # 账号
    account = models.CharField(max_length=50)
    # 密码
    password = models.CharField(max_length=50)
    # id
    id = models.AutoField(primary_key=True)
    # email
    emails = models.EmailField(max_length=50, blank=True, null=True)
    # 名字
    name = models.CharField(max_length=50, blank=True, null=True)
    # 级别
    level = models.CharField(max_length=50, blank=True, null=True)
    # token
    token = models.CharField(max_length=300, blank=True, null=True)
    # 头像
    avatar = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'Users'
        ordering = ['id']


# token
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'Token'
        ordering = ['id']


# 测试环境集合
class EnvList(models.Model):
    """
    环境
    """
    # 环境编号
    id = models.AutoField(primary_key=True)
    # 环境path
    env = models.CharField(max_length=50, blank=True, null=True)
    # 环境名称
    name = models.CharField(max_length=50, blank=True, null=True)
    # db config
    db_config = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'EnvList'
        ordering = ['id']


# 测试资源
class TestResource(models.Model):
    # 账户
    account = models.CharField(max_length=50)
    # 密码
    password = models.CharField(max_length=50)
    # uuid
    uuid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'TestResource'
        ordering = ['account']


# UI测试用例
class UiTestCasesList(models.Model):
    # id
    id = models.AutoField(primary_key=True)
    # 测试名字
    caseName = models.CharField(max_length=300, blank=True, null=True)
    # 用例描述
    describe = models.CharField(max_length=300, blank=True, null=True)
    # 步骤
    steps = models.CharField(max_length=500, blank=True, null=True)
    # 初始步骤
    beginSteps = models.CharField(max_length=500, blank=True, null=True)
    # 结束步骤
    endSteps = models.CharField(max_length=500, blank=True, null=True)
    # 拥有者
    owner = models.CharField(max_length=50, blank=True, null=True)
    # 是否为公用
    showToAll = models.BooleanField(default=True)
    # 项目
    project = models.CharField(max_length=50, blank=True, null=True)
    # 平台
    platform = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'UiTestCasesList'
        ordering = ['id']


# Ui测试用例集合
class UiTestCasesSet(models.Model):
    # id
    id = models.AutoField(primary_key=True)
    # TestCases ids
    testCases = models.CharField(max_length=300, blank=True, null=True)
    # 拥有者
    owner = models.CharField(max_length=50, blank=True, null=True)
    # 是否为公用
    showToAll = models.BooleanField(default=True)
    # 描述
    describe = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'UiTestCasesSet'
        ordering = ['id']


# Ui测试结果
class UiTestResults(models.Model):
    # 测试编号
    id = models.AutoField(primary_key=True)
    # 结果
    result = models.BooleanField(default=True)
    # 错误信息
    errorInfo = models.CharField(max_length=300, default='none', blank=True, null=True)
    # 测试开始时间
    startTime = models.DateTimeField(blank=True, null=True)
    # Cases集合持续时间
    timeOfDuration = models.TimeField(blank=True, null=True)
    # 执行人员
    runner = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'UiTestResults'
        ordering = ['id']


# 接口测试用例
class InterfaceList(models.Model):
    """
    接口
    """
    # 接口编号
    id = models.AutoField(primary_key=True)
    # url
    path = models.CharField(max_length=200, blank=True, null=True)
    # method
    method = models.CharField(max_length=10, blank=True, null=True)
    # 标题
    title = models.CharField(max_length=200, blank=True, null=True)
    # 更新时间
    up_time = models.CharField(max_length=50, blank=True, null=True, default=datetime.now)
    # 版本
    version = models.CharField(max_length=20, blank=True, null=True)
    # 描述
    desc = models.CharField(max_length=300, blank=True, null=True)
    # 参数
    req_query = models.TextField(blank=True, null=True)
    # 参数
    req_body_form = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'InterfaceList'
        ordering = ['id']


# 接口测试case
class TestCasesList(models.Model):
    """
    测试用例
    """
    # 接口编号
    id = models.AutoField(primary_key=True)
    # url
    path = models.CharField(max_length=100, blank=True, null=True)
    # method
    method = models.CharField(max_length=10, blank=True, null=True)
    # 标题
    title = models.CharField(max_length=10, blank=True, null=True)
    # 作者
    owner = models.CharField(max_length=20, blank=True, null=True)
    # 更新时间
    up_time = models.DateTimeField(blank=True, null=True, default=datetime.now)
    # 版本
    version = models.CharField(max_length=10, blank=True, null=True)
    # 描述
    desc = models.CharField(max_length=200, blank=True, null=True)
    # 参数
    parameter = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'TestCasesList'
        ordering = ['id']


# 接口用例测试集合
class TestCasesSetList(models.Model):
    """
    场景
    """
    # id
    id = models.AutoField(primary_key=True)
    # TestCases ids
    testCases = models.CharField(max_length=300, blank=True, null=True)
    # 拥有者
    owner = models.CharField(max_length=50, blank=True, null=True)
    # 是否为公用
    showToAll = models.BooleanField(default=True)
    # 描述
    describe = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'TestCasesSetList'
        ordering = ['id']


# 接口用例测试结果
class TestCasesResult(models.Model):
    """
    接口测试结果
    """
    # 测试编号
    id = models.AutoField(primary_key=True)
    # 结果
    result = models.BooleanField(default=True)
    # 错误信息
    errorInfo = models.CharField(max_length=300, default='none', blank=True, null=True)
    # 测试开始时间
    startTime = models.DateTimeField(blank=True, null=True)
    # Cases集合持续时间
    timeOfDuration = models.TimeField(blank=True, null=True)
    # 执行人员
    runner = models.CharField(max_length=50, blank=True, null=True)
    # 测试返回结果（接口返回）
    InterfaceResult = models.CharField(max_length=100, blank=True, null=True)
    # 测试返回结果（status code返回）
    InterfaceStatusCodeResult = models.CharField(max_length=10, blank=True, null=True)
    # 测试返回结果（数据库返回）
    SqlResult = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'TestCasesResult'
        ordering = ['id']


# Ui测试app名字
class AppName(models.Model):
    """
    接口测试结果
    """
    # 编号
    id = models.AutoField(primary_key=True)
    # 平台 iOS android
    platform = models.CharField(max_length=30, default='android', blank=True, null=True)
    # name
    name = models.CharField(max_length=100, blank=True, null=True)
    # App name
    appName = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'AppName'
        ordering = ['id']
