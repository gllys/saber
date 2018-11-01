# __author__ = 'wilsonLwx'
# __date__ = '2018/10/17'
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import filters
from collections import OrderedDict

from .errocode import StatusCode


class Pagination(PageNumberPagination):
    """
    自定义分页
    """
    # 设置默认每页10条
    page_size = 10
    # 设置查询范围的参数
    page_size_query_param = 'page_size'
    # 分页的参数名
    page_query_param = 'page'
    # 设置每页最大一百条
    # max_page_size = 100

    def get_paginated_response(self, data):
        # 重写获取分页数据的方法，新增code
        if not data:
            return Response(StatusCode().not_found)
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('code', 200),
            ('results', data)
        ]))

    @staticmethod
    def filter(filter_class: object, search_fields: object = None, ordering_fields: object = None) -> object:
        # 过滤
        filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
        filter_class = filter_class
        # 过滤的字段
        search_fields = search_fields
        # 排序字段
        ordering_fields = ordering_fields
        return filter_backends, filter_class, search_fields, ordering_fields
