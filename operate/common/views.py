from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from atom.mongodb import *
import json


# Create your views here.
# 更新api接口
@api_view(['GET'])
def updateMongodbToMysql(request):
    result = {
        'GET': {"message": "update success"},
        'OTHER': {"message": "please use GET"},
    }
    if request.method == 'GET':
        dictToMysql(parameterList=mongodbToDict())
        return Response(json.dumps(result['GET']), content_type="application/json", status=HTTP_200_OK)
    else:
        return Response(json.dumps(result['OTHER']), content_type="application/json",
                        status=HTTP_412_PRECONDITION_FAILED)

