# __author__ = 'wilsonLwx'
# __date__ = '2018/10/15'


from rest_framework import mixins, views

# Create your views here.

from atom.models import TestCasesSetList
from apps.scenes.filters import SceneListFilter
from utils.comm_classes import CommClasses, CreateComClass
from utils.pagination import Pagination
from .serializers import ScenesViewSerializer


class ScenesViewSet(mixins.ListModelMixin, CreateComClass):
    """
    测试场景
    """
    queryset = TestCasesSetList.objects.get_queryset().order_by('-id')
    serializer_class = ScenesViewSerializer

    # 分页
    pagination_class = Pagination

    # 过滤 搜索 查询
    filter_backends, filter_class, search_fields, ordering_fields = \
        Pagination.filter(SceneListFilter, ('title',), ('up_time',))


class ScenesUpdateView(views.APIView, CommClasses):
    """
    自定义更新场景
    get:
        场景详情
    post:
        更新场景
    """

    def __init__(self):
        super(ScenesUpdateView, self).__init__()
        self.model = TestCasesSetList
        self.model_serializer = ScenesViewSerializer
