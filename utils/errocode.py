# __author__ = 'wilsonLwx'
# __date__ = '2018/10/18'


class StatusCode(object):
    """
    错误类型
    """

    def __init__(self, data=None):
        self.type_err = {'code': 406, 'message': 'TYPE ERROR'}
        self.not_found = {'code': 200, 'results': []}
        self.correct = {'code': 200, 'results': [data]}
        self.link_success = {'code': 200, 'status': 'SUCCESS'}
