# __author__ = 'wilsonLwx'
# __date__ = '2018/10/12'

from rest_framework import serializers

from atom.models import InterfaceList


class InterfaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterfaceList
        fields = "__all__"
