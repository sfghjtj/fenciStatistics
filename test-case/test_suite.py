import unittest
from test_case import Case_02


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [Case_02('test_minus'), Case_02('test_add')]
    # 这种方式无法对测试用例进行排序，同时，suite中也可以套suite
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Case_02))
    # suite.addTest(Case_02('test_minus')) 添加单个test测试用例
    suite.addTests(tests)
    # TextTestRunner输出到控制台,HTMLTestRunner(需单独下载)可以格式化输出到HTML
    runner = unittest.TextTestRunner(verbosity=2)  # 默认为1一般报告、0简单报告、2详细报告
    runner.run(suite)

    # 测试报告写入文件
    # with open('../testCase.txt', 'a', encoding='utf-8') as f:
    #    runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #   runner.run(suite)
