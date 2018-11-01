# __author__ = 'wilsonLwx'
# __date__ = '2018/10/14'
import django_filters
from atom.models import InterfaceList


class InterfaceListFilter(django_filters.FilterSet):
    """
    接口过滤类
    """
    # 模糊查询
    title = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    path = django_filters.CharFilter(field_name='path', lookup_expr='contains')

    class Meta:
        model = InterfaceList
        fields = ['title', 'path', 'method', 'version']
