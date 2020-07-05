# -*- encoding: utf-8 -*-
'''
-------------------------------------------------------
@File    :   create_app.py
@Time    :   2020/07/05 17:57:53
@Author  :   RGDZ
@Version :   1.0.0
@Contact :   3303476267@qq.com
@License :   
@Desc    :   
-------------------------------------------------------
'''

from sanic import Sanic


from .config import Config


def register_blueprint(app:Sanic)->None:
    """ register blueprint """
    from .api import api
    app.blueprint(api)
    print(api.routes)

def create_app()->Sanic:
    """ create app """
    app = Sanic(__name__)
    app.config.from_object(Config)
    register_blueprint(app)
    return app
