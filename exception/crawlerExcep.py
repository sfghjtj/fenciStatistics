# encoding=utf-8

from urllib.error import URLError


class CrawlerException(RuntimeError):
    '''
    爬虫模块异常
    '''

    def __init__(self, exception):
        '''
        初始化传入一个urllib2.URLError或urllib2.HTTPError异常对象
        '''
        try:
            assert isinstance(exception, URLError)
            if hasattr(exception, 'reason'):
                super(CrawlerException, self).__init__(exception.reason)
            elif hasattr(exception, 'code'):
                super(CrawlerException, self).__init__(exception.code)
            else:
                super(CrawlerException, self).__init__(exception)
        except AssertionError:
            super(CrawlerException, self).__init__(exception)
