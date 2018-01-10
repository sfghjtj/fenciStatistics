import sys
import os
sys.path.append('..' + os.sep + '..')
from log import Logger
from crawler import U2crawsociality
from fenci import Partfreword
from pandasUtils import PandasExcel
from constant import craw_constant


def initResCiku():
    '''
    根据词典库初始化词典
    '''

    particColumns = [u'CF1级', u'CF2级', u'CF3级',
                     u'CF4级', u'CF5级', u'CF6级', u'分词名称']
    synonymColumns = [u'分词名称', u'同义词1', u'同义词2', u'同义词3', u'同义词4', u'同义词5']
    dictpath = PandasExcel.particwrite(particColumns)
    synodic = PandasExcel.synonymwrite(synonymColumns)['synodic']
    return {"customdic": dictpath['customdic'], "filterdic": dictpath
            ['filterdic'], "synodic": synodic}
