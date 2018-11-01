# __author__ = 'wilsonLwx'
# __date__ = '2018/10/15'

from rest_framework import mixins, viewsets, views
# Create your views here.

from atom.models import InterfaceList
from utils.comm_classes import CommClasses
from utils.pagination import Pagination
from .serializers import InterfaceSerializer
from interfaces.filters import InterfaceListFilter


class InterfaceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    实现接口列表分页，过滤，搜索，排序
    list:
        实现接口列表分页，过滤，搜索，排序
    """
    queryset = InterfaceList.objects.get_queryset().order_by('-id')
    serializer_class = InterfaceSerializer

    # 过滤 搜索 查询
    filter_backends, filter_class, search_fields, ordering_fields = \
        Pagination.filter(InterfaceListFilter, ('title', 'path'), ('up_time',))

    # 分页
    pagination_class = Pagination


class InterfaceDetailView(views.APIView):
    """
    接口详情
    get:
        接口详情
    """

    # 重写get方法
    def get(self, request, pk, format=None):
        response = CommClasses(InterfaceList, InterfaceSerializer).get(request, pk)
        return response
