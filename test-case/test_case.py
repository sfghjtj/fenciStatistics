import unittest


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


class Case_02(unittest.TestCase):

    '''
    所有的测试用例只会执行一次初始化和清除环境
    如果想在每次调用测试用例方式时初始化则def setUp(self):即可
    '''
    @classmethod
    def setUpClass(cls):
        print('before environment')

    @classmethod
    def tearDownClass(cls):
        print('after environment')

    @unittest.skip('just skip ,ok?')  # 测试用例可以跳过不执行,注意测试方法必须以test开头。
    def test_add(self):
        self.assertEqual(4, add(1, 2))

    @unittest.skipIf(False, 'skip?')
    def test_minus(self):
        self.assertEqual(1, minus(3, 2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
