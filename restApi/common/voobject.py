
'''
定义资源resource的处理返回的对象VO
'''


class CrawVO(object):
    '''
    定义爬虫分词接口的response对象
    '''

    def __init__(self, code, success, message, data):
        self.code = code
        self.success = success
        self.message = message
        self.data = data

    def __str__(self):
        return repr({"code": self.code, "success": self.success,
                     "data": self.data, "message": self.message})
