# encoding=utf-8
import pandas as pd
import numpy as np
import os
import sys
sys.path.append('..')
from exception import PandasException
from log import Logger

'''
excel的配置的文件路劲
FIXME:该模块用缓存配置并读取
'''
EXCEL_PATH = os.path.dirname(os.path.dirname(
    __file__)) + os.sep + 'data' + os.sep + 'fenci3.xlsx'


class PandasExcel(object):
    """
    pandas处理excel工具
    """

    Log = Logger.getLogger(__name__)
    df = pd.read_excel(EXCEL_PATH)

    @classmethod
    def particwrite(cls, particColumns):
        '''
        根据传入的字段列表写入自定义词库,返回词库地址
        '''
        customdic = os.path.abspath(os.path.dirname(os.path.dirname(
            __file__))) + os.sep + 'data' + os.sep + 'ciku3.txt'
        fileciku = open(customdic, 'w+', 1, encoding='utf-8')
        filterdic = os.path.abspath(os.path.dirname(os.path.dirname(
            __file__))) + os.sep + 'data' + os.sep + 'filter3.txt'
        filterku = open(filterdic, 'w+', 1, encoding='utf-8')
        try:
            for column in particColumns:
                assert column in cls.df.columns, '传入参数不是excel所在的字段列表！'
            particDatas = cls.df.loc[:, particColumns]
            for particColumn in particDatas.columns:
                columnData = particDatas[particColumn].drop_duplicates()
                columnData = columnData[columnData.notnull()]
                for data in columnData:
                    str = data + ' ' + 'ns' + '\n'
                    fileciku.write(str)
                    filterku.write(data + '\n')
        except AssertionError as e:
            cls.Log.error(e)
            raise PandasException(e)
        except BaseException as e:
            cls.Log.error(e)
            raise PandasException(e)
        else:
            return dict(customdic=customdic, filterdic=filterdic)
        finally:
            fileciku.close()
            filterku.close()

    @classmethod
    def synonymwrite(cls, synonymColumns):
        '''
        根据传入的字段列表写入同义词词库,返回词库地址
        '''
        synodic = os.path.abspath(os.path.dirname(os.path.dirname(
            __file__))) + os.sep + 'data' + os.sep + 'tongyici3.txt'
        synoku = open(synodic, 'w+', 1, encoding='utf-8')
        try:
            for column in synonymColumns:
                assert column in cls.df.columns, '传入参数不是excel所在的字段列表！'
            synonymDatas = cls.df.loc[:, synonymColumns]
            synonymIndexs = synonymDatas.index
            for index in range(len(synonymIndexs)):
                synodata = synonymDatas.loc[index]
                synodata = synodata[synodata.notnull()]
                if len(synodata) != 1:
                    str = ''
                    for data in synodata:
                        str += '\t' + data
                    if str.startswith('\t'):
                        str = str[len('\t'):]
                        synoku.write(str + '\n')
        except AssertionError as e:
            cls.Log.error(e)
            raise PandasException(e)
        except BaseException as e:
            cls.Log.error(e)
            raise PandasException(e)
        else:
            return dict(synodic=synodic)
        finally:
            synoku.close()
