from flask.ext.restful import fields
import pandas as pd
'''
自定义所有资源的输出字段的类型
'''


class CrawData(fields.Raw):
    '''
    自定义爬虫分词接口输出的data字段的输出类型
    '''

    def format(self, data):
        if isinstance(data, pd.core.frame.DataFrame):
            seqData = list()
            for value in data.values:
                seqData.append(list(value))
            return dict(seqData)
        else:
            return data
