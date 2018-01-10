
import sys
import os
from flask import Flask
from flask.ext import restful
from resources.crawstaticRes import CrawResource, CrawtxtResource
sys.path.append('..' + os.sep + '..')
from config import flaskRestful

'''
所有的资源进行导入并配置相应的路由，这里是所有的api的启动入口
'''
app = Flask(__name__)
api = restful.Api(app)

# 添加资源和路由
api.add_resource(CrawResource, '/crawStatics', endpoint='crawStatics_ep')
api.add_resource(CrawtxtResource, '/crawTxtStatics',
                 endpoint='crawTxtStatics_ep')

# 启动api
if __name__ == '__main__':
    app.run(host=flaskRestful.SERVER, port=flaskRestful.PORT)
