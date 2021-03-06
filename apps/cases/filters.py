# __author__ = 'wilsonLwx'
# __date__ = '2018/10/14'
import django_filters
from atom.models import TestCasesList


class CaseListFilter(django_filters.FilterSet):
    # 模糊查询
    owner = django_filters.CharFilter(field_name='owner', lookup_expr='contains')

    class Meta:
        model = TestCasesList
        fields = ['owner']
