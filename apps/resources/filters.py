# __author__ = 'wilsonLwx'
# __date__ = '2018/10/22'
import django_filters

from atom.models import EnvList


class EnvListFilter(django_filters.FilterSet):
    # 模糊查询
    env = django_filters.CharFilter(field_name='env', lookup_expr='contains')

    class Meta:
        model = EnvList
        fields = ['env']
