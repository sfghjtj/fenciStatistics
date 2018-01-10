
import unittest
import sys
import os
sys.path.append('..')
from log import Logger


class Log_Case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 使用时传入当前模块名称就行了！！！
        cls.logger = Logger.getLogger(__name__)
        print('start...')

    @classmethod
    def tearDownClass(cls):
        print('end...')

    def test_log(self):
        self.logger.debug('debug testCase!')
        self.logger.info('info testCase!')
        self.logger.warn('warn testCase!')
        self.logger.error('errro testCase!')
        self.logger.critical('critical testCase!')

if __name__ == "__main__":
    suite = unittest.TestSuite(tests=(Log_Case('test_log'),))
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)
