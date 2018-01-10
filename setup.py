from setuptools import setup, find_packages

'''
如果不用setup.py将模块发布或添加为系统模块，仅仅作为第三方模块的依赖安装的话，可以不用定义setup.py。
即:如果项目要作为工具包发布可以setup.py与requirements.txt结合使用，不显示egg类型文件夹；如果仅仅运行该项目则只需requirements.txt。
如果仅仅定义requirements.txt:则内容直接设置为：
jieba >= 0.39
nltk >= 3.2.5
numpy >= 1.13.3
pandas >= 0.21.0
xlrd >= 1.1.0
flask >= 0.12.2
jsonpath-rw >= 1.4.0
Flask-RESTful >= 0.3.6
'''
setup(
    name='analysis',
    version='1.0',
    packages=find_packages(),
    # scripts=['say_hello.py'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'config': ['*.config'],
        'data': ['*.xlsx'],
    },
    # metadata for upload to PyPI
    author='bldztuisong',
    author_email='zhaohouwei@bldz.com',
    description='bldz for crawler and other anlysis package',
    long_description=open("README.rst").read(),
    url='http://pangu.bldz.com:10081/business-service/analysis.git',
    # license='PSF',
    keywords='bldz analysis crawler pandas partword statics',
    # could also include long_description, download_url, classifiers, etc.
)
