# __author__ = 'wilsonLwx'
# __date__ = '2018/10/19'

from rest_framework import status, mixins, viewsets
from rest_framework.response import Response

from utils.errocode import StatusCode


class CommClasses(object):
    """
    公共类
    """

    def __init__(self, model, model_serializer):
        self.model = model
        self.model_serializer = model_serializer

    def get_object(self, pk):
        # 获取对象的方法
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return False

    # get方法
    def get(self, request, pk, format=None):
        # 判断传入参数是否正确
        if not pk.isdigit():
            return Response(StatusCode().type_err)

        # 获取对象
        obj = self.get_object(pk)
        if obj:
            # 序列化对象
            serializer = self.model_serializer(obj, data=request.data)
            if serializer.is_valid():
                # 返回处理后的数据和状态码
                return Response(StatusCode(serializer.data).correct)
        else:
            return Response(StatusCode().not_found, status=status.HTTP_200_OK)

    # post方法，
    def post(self, request, pk, format=None):
        if not pk.isdigit():
            return Response(StatusCode().type_err)

        # 获取对象
        obj = self.get_object(pk)
        if obj:
            # 序列化对象
            serializer = self.model_serializer(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(StatusCode(serializer.data).correct)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(StatusCode().not_found, status=status.HTTP_200_OK)


class CreateComClass(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create公共类
    """
    def create(self, request, *args, **kwargs):
        # 重写create方法 塞入code
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(StatusCode(serializer.data).correct, headers=headers)
