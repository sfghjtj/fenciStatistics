import logging
import logging.config
from os import path, sep


LOG_CONFIG = path.dirname(path.dirname(__file__)) + \
    sep + 'config' + sep + 'logging.config'
logging.config.fileConfig(LOG_CONFIG)


class Logger(object):
    '''
    log日志生成器，调用：Logger.getLogger(__name__)即可！
    注意区分下__main__的情况,用root记录器。
    '''

    @classmethod
    def getLogger(cls, moduleName):
        return logging.getLogger(moduleName)
