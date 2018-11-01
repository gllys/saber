# __author__ = 'wilsonLwx'
# __date__ = '2018/10/22'

from rest_framework import serializers

from atom.models import EnvList


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvList
        fields = '__all__'
