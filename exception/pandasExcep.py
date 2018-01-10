# encoding=utf-8


class PandasException(RuntimeError):
    '''
    pandas处理过程封装的异常
    '''

    def __init__(self, message):
        super(PandasException, self).__init__(message)
        self.message = message

    def __str__(self):
        return repr(self.message)
