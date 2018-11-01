# __author__ = 'wilsonLwx'
# __date__ = '2018/10/15'
import yaml
import pymysql
from rest_framework import mixins, views

# Create your views here.
from rest_framework.response import Response

from atom.models import EnvList
from apps.resources.filters import EnvListFilter
from apps.resources.serializers import EnvSerializer
from utils.comm_classes import CommClasses, CreateComClass
from utils.pagination import Pagination


class EnvListViewSet(mixins.ListModelMixin, CreateComClass):
    """
    环境视图
    list:
        环境列表
    """
    queryset = EnvList.objects.get_queryset().order_by('-id')
    serializer_class = EnvSerializer

    # 过滤 搜索 查询
    filter_backends, filter_class, search_fields, ordering_fields = \
        Pagination.filter(EnvListFilter, ('env',))

    # 分页
    pagination_class = Pagination


class EnvListView(views.APIView, CommClasses):
    """
    环境详情和更新视图
    get:
        环境详情
    post:
        更新环境
    """

    def __init__(self):
        super(EnvListView, self).__init__()
        self.model = EnvList
        self.model_serializer = EnvSerializer


class TestLinkView(views.APIView):
    def get(self, request):
        return Response('ok')
