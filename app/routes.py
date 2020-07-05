# -*- encoding: utf-8 -*-
'''
-------------------------------------------------------
@File    :   routes.py
@Time    :   2020/07/05 21:26:53
@Author  :   RGDZ
@Version :   1.0.0
@Contact :   3303476267@qq.com
@License :   
@Desc    :   Define routes
-------------------------------------------------------
'''


class Routes:
    #index
    INDEX = "/"

    #API
    API_PATH = INDEX+"api"
    API_SEARCH_BY_HASH = API_PATH + "/hash"
    API_SEARCH_BY_URL = API_PATH + "/url"
    API_SEARCH_BY_EMAIL = API_PATH + "/email"