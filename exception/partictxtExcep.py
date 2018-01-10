# encoding=utf-8


class ParticException(RuntimeError):
    '''
    分词异常继承运行时异常
    '''

    def __init__(self, info):
        super(ParticException, self).__init__(info)
        self.info = info

    def __str__(self):
        return repr(self.info)
