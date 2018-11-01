# __author__ = 'wilsonLwx'
# __date__ = '2018/10/15'

from rest_framework import mixins, views

from atom.models import TestCasesList, TestCasesResult
from apps.cases.filters import CaseListFilter
from utils.comm_classes import CommClasses, CreateComClass
from utils.pagination import Pagination
from .serializers import CaseInfoViewSerializer, TestResultSerializer


# Create your views here.

class CaseInfoViewSet(mixins.ListModelMixin, CreateComClass):
    """
    用例管理
    list：
        用例列表
    create：
        新增用例
    """
    queryset = TestCasesList.objects.get_queryset().order_by('-id')
    serializer_class = CaseInfoViewSerializer

    # 过滤 搜索 查询
    filter_backends, filter_class, search_fields, ordering_fields = \
        Pagination.filter(CaseListFilter, ('title',), ('up_time',))

    # 分页
    pagination_class = Pagination


class CaseUpdateView(views.APIView, CommClasses):
    """
    自定义更新用例
    get:
        用例详情
    post:
        更新用例
    """

    def __init__(self):
        super(CaseUpdateView, self).__init__()
        self.model = TestCasesList
        self.model_serializer = CaseInfoViewSerializer


class TestResultDetailView(views.APIView):
    """
    测试结果
    get:
        测试结果详情
    """
    # 重写get方法
    def get(self, request, pk, format=None):
        response = CommClasses(TestCasesResult, TestResultSerializer).get(request, pk)
        return response
