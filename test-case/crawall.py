
import sys
import unittest
import pandas as pd
sys.path.append('..')
from crawler import U2crawsociality
from fenci import Partfreword
from pandasUtils import PandasExcel
from constant import craw_constant

# 传入资讯文章的infoId
# 实例：54b8d7dbdd7546099ed8e61fc773a720
# 关键词：
INFOID = '2544f33cf4be477fafb680ba33aa6acc'


class Case_01(unittest.TestCase):
    '''
    测试前准备环境的搭建
    '''

    def setUp(self):
        '''
        读取excel
        '''
        particColumns = [u'CF1级', u'CF2级', u'CF3级',
                         u'CF4级', u'CF5级', u'CF6级', u'分词名称']
        synonymColumns = [u'分词名称', u'同义词1', u'同义词2', u'同义词3', u'同义词4', u'同义词5']
        dictpath = PandasExcel.particwrite(particColumns)
        customdic = dictpath['customdic']
        filterdic = dictpath['filterdic']
        synodic = PandasExcel.synonymwrite(synonymColumns)['synodic']
        self.customdic = customdic
        self.filterdic = filterdic
        self.synodic = synodic

    def testCraw(self):
        # 资讯模块接口
        resource = U2crawsociality(
            craw_constant.SOCIALITY_URL, informationId=INFOID).infocrawler()
        pfw = Partfreword(resource, self.customdic,
                          self.filterdic, self.synodic)
        df = pfw.feqstatics()
        dfl = list()
        for i in df.values:
            dfl.append(list(i))
        print(dict(dfl), type(dfl))
        print(df, '\n', type(df), end=',')

    '''
    测试后准备环境的还原
    '''

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
