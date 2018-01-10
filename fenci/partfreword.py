
import jieba
import jieba.posseg as pseg
import jieba.analyse as anl
import codecs
import re
import os
import sys
from nltk.probability import FreqDist
from .synorep import SynorepUtil
import numpy as np
import pandas as pd
open = codecs.open
sys.path.append('..')
from exception import ParticException
from crawler import U2crawsociality
from log import Logger


class Partfreword(object):
    '''
    结巴分词nltk词频统计
    '''

    Log = Logger.getLogger(__name__)

    def __init__(self, resource, customdic, filterdic, synodic):
        self.resource = resource
        self.customdic = customdic
        self.filterdic = filterdic
        self.synodic = synodic
        try:
            assert isinstance(resource, str) and os.path.exists(customdic) \
                and os.path.exists(synodic) and os.path.exists(filterdic)
            jieba.load_userdict(customdic)
        except AssertionError as e:
            self.Log.error(e)
            raise ParticException(e)

    def __synopart(self, needSyno):
        '''
        同义词替换后进行分词,且只保留名称词性
        '''
        cfp = None
        word_list = []
        try:
            if needSyno:
                resourcestr = SynorepUtil.synorepm(
                    self.resource, self.customdic, self.synodic)
                wordlist = list(pseg.cut(resourcestr))
            else:
                wordlist = list(pseg.cut(self.resource))
            # 添加保留词词典
            with open(self.filterdic, 'r+', 'utf-8') as cfp:
                filter_word = []
                for line in cfp:
                    for word in line.split():
                        filter_word.append(word)
            # 提取名词,只保留自定义词库中的词。
            for wds in wordlist:
                if wds.flag == 'x' and wds.word != ' ' and wds.word \
                        != 'ns' or re.match(r'^n', wds.flag) is not None and \
                        re.match(r'^nr', wds.flag) is None:
                    if wds.word in filter_word:
                        word_list.append(wds.word)
            return word_list
        except BaseException as e:
            self.Log.error(e)
            raise ParticException(e)

    def feqstatics(self, needSyno):
        '''
        nltk统计词频，若无词库中的词，则返回关键字
        '''
        fdist = FreqDist(self.__synopart(needSyno))
        if not len(fdist):
            return self.__genekeyword()
        else:
            nslist = []
            frelist = []
            for i in fdist:
                nslist.append(i)
                frelist.append(fdist[i])
            df = Partfreword.geneDataFrame(['名称', '词频'], nslist, frelist)
            df = df.sort_values(by='词频', ascending=False)
            return pd.DataFrame(df.values, columns=df.columns)

    def __genekeyword(self):
        '''
        关键字提取
        '''
        df = None
        try:
            resourcestr = SynorepUtil.synorepm(
                self.resource, self.customdic, self.synodic)
            # 基于TF-IDF算法进行无监督的关键词抽取算法
            # seg = anl.extract_tags(resourcestr, topK=20, withWeight=True)
            # 基于TestRank算法
            seg = anl.textrank(resourcestr, topK=20, withWeight=True)
            taglist = []
            weightlist = []
            for tag, weight in seg:
                taglist.append(tag)
                weightlist.append(weight)
            df = Partfreword.geneDataFrame(['名称', '权重'], taglist, weightlist)
        except BaseException as e:
            self.Log.error(e)
            raise ParticException(e)
        else:
            return df

    @staticmethod
    def geneDataFrame(columslist, *taglist):
        '''
        生成pandas对象DataFrame
        '''
        res_list = list(zip(*taglist))
        return pd.DataFrame(res_list, columns=columslist)
