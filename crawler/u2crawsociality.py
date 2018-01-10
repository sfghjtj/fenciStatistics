
from urllib.request import urlopen, Request
from urllib.error import URLError
import json
import sys
from jsonpath_rw import jsonpath, parse
sys.path.append('..')
from exception import CrawlerException
from log import Logger


class U2crawsociality(object):
    '''
    资讯接口爬虫获取json数据中的tex标签文本内容
    '''

    Log = Logger.getLogger(__name__)

    def __init__(self, url, **informationId):
        self.informationId = informationId
        self.url = url

    def infocrawler(self):
        try:
            assert self.informationId, '参数格式异常！'
            data = json.dumps(self.informationId).encode('utf-8')
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
            headers = {'User-Agent': user_agent}
            request = Request(self.url, data, headers)
            request.add_header('Content-Type', 'application/json')
            with urlopen(request) as ress:
                resinfo = ress.read()
            if not resinfo:
                return None
            if(self.__jsonpathm(resinfo, r'$.success') == 'False'):
                print(self.__jsonpathm(resinfo, r'$.success'))
                raise CrawlerException(self.__jsonpathm(resinfo, r'$.message'))
            else:
                return self.__jsonpathm(resinfo, r'$.data..tex')
        except URLError as e:
            self.Log.error(e)
            raise CrawlerException(e)
        except BaseException as e:
            self.Log.error(e)
            raise CrawlerException(e)

    def __jsonpathm(self, strvalue, json_path):
        obj = json.loads(strvalue, encoding='utf-8')
        jsp = parse(json_path)
        res = jsp.find(obj)
        resvalue = [d.value for d in res][0]
        return resvalue if isinstance(resvalue, str) \
            else str(resvalue)
