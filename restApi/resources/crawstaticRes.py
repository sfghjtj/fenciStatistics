import sys
import os
from flask.ext.restful import Resource, fields, marshal_with, reqparse
sys.path.append('..')
sys.path.append('..' + os.sep + '..')
from common import initResCiku, CrawData, CrawVO
from log import Logger
from crawler import U2crawsociality
from fenci import Partfreword
from pandasUtils import PandasExcel
from constant import craw_constant

LOG = Logger.getLogger(__name__)  # 获取日志记录器
DICT_PATH = initResCiku()  # 初始化词库
LOG.info('初始化的词典库相关地址为:{}'.format(DICT_PATH))

# 对post参数进行解析
craw_parser = reqparse.RequestParser()
# FIXME当格式不对时无法返回规定的格式化json数据。
craw_parser.add_argument('infoId', dest='infoId', type=str,
                         location='json', required=False, help='invalid param!')
craw_parser.add_argument('text', dest='text', type=str,
                         location='json', required=False, help='invalid param!')
# 对post输出response格式化
craw_fields = {'success': fields.Boolean,
               'message': fields.String, 'data': CrawData}


class CrawResource(Resource):
    '''
    爬虫接口分词统计接口的资源类型:处理infoId FIXME未定义自定义异常
    '''
    @marshal_with(craw_fields)
    def post(self):
        crawParams = craw_parser.parse_args()
        try:
            resSociety = U2crawsociality(
                craw_constant.SOCIALITY_URL, informationId=crawParams['infoId']).infocrawler()
            partfrew = Partfreword(resSociety, DICT_PATH['customdic'], DICT_PATH[
                'filterdic'], DICT_PATH['synodic'])
            # 传递True进行同义词处理
            dataResult = partfrew.feqstatics(True)
            LOG.info('分词统计结果为:{}'.format(dataResult))
        except AssertionError as e:
            LOG.error(e)
            return CrawVO(code='500', success=False, message=e, data=None)
        except BaseException as e:
            LOG.error(e)
            return CrawVO(code='500', success=False, message=str(e), data=None)
        else:
            return CrawVO(code='200', success=True, message=None, data=dataResult)


class CrawtxtResource(Resource):
    '''
    爬虫接口分词统计接口的资源类型:处理txt FIXME未定义自定义异常
    '''
    @marshal_with(craw_fields)
    def post(self):
        crawParams = craw_parser.parse_args()
        try:
            assert crawParams['text'], 'text请求不能为空！'
            partfrew = Partfreword(crawParams['text'], DICT_PATH['customdic'], DICT_PATH[
                                   'filterdic'], DICT_PATH['synodic'])
            # 传递False不进行同义词处理
            dataResult = partfrew.feqstatics(False)
            LOG.info('分词统计结果为:{}'.format(dataResult))
        except AssertionError as e:
            LOG.error(e)
            return CrawVO(code='500', success=False, message=e, data=None)
        except BaseException as e:
            LOG.error(e)
            return CrawVO(code='500', success=False, message=str(e), data=None)
        else:
            return CrawVO(code='200', success=True, message=None, data=dataResult)
