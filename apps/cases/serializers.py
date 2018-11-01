# __author__ = 'wilsonLwx'
# __date__ = '2018/10/15'

from rest_framework import serializers

from atom.models import TestCasesList, TestCasesResult


class CaseInfoViewSerializer(serializers.ModelSerializer):
    """
    用例序列化类
    """
    # 使更新时间只显示 不作为手动项
    up_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TestCasesList
        fields = '__all__'


class TestResultSerializer(serializers.ModelSerializer):
    """
    测试结果序列化类
    """

    class Meta:
        model = TestCasesResult
        fields = '__all__'
