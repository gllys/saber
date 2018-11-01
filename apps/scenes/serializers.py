# __author__ = 'wilsonLwx'
# __date__ = '2018/10/18'

from rest_framework import serializers

from atom.models import TestCasesSetList


class ScenesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCasesSetList
        fields = '__all__'
