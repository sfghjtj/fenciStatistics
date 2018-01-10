
import sys
import os
import jieba
sys.path.append('..')
from exception import ParticException
from log import Logger


class SynorepUtil(object):
    '''
    分词后进行同义词替换工具
    '''

    Log = Logger.getLogger(__name__)

    @staticmethod
    def synorepm(resource, customdic, synodic):
        seq_re = None
        try:
            assert isinstance(resource, str) and os.path.exists(customdic) \
                and os.path.exists(synodic)
            seq_pr = SynorepUtil().__partictxt(resource, customdic)
            seq_re = SynorepUtil().__repsynor(seq_pr, synodic)
        except BaseException as e:
            SynorepUtil.Log.error(e)
            raise ParticException(e)
        else:
            return seq_re

    def __partictxt(self, resource, customdic):
        # 添加自定义词典
        try:
            jieba.load_userdict(customdic)
            seg_list = jieba.cut(resource, cut_all=False)
        except BaseException as e:
            SynorepUtil.Log.error(e)
            raise ParticException(e)
        else:
            return "/".join(seg_list)

    def __repsynor(self, resource, synodic):
        # 同义词替换返回替换后的字符串
        combine_dict = {}
        for w in open(synodic, "r", encoding='utf-8'):
            w_1 = w.strip().split("\t")
            num = len(w_1)
            for i in range(0, num):
                combine_dict[w_1[i]] = w_1[0]

        seg_list_2 = ""
        for word in resource.split("/"):
            if word in combine_dict:
                word = combine_dict[word]
                seg_list_2 += word
            else:
                seg_list_2 += word
        return seg_list_2
