# -*- encoding: utf-8 -*-
'''
-------------------------------------------------------
@File    :   config.py
@Time    :   2020/07/05 17:51:21
@Author  :   RGDZ
@Version :   1.0.0
@Contact :   3303476267@qq.com
@License :   
@Desc    :   App-Config
-------------------------------------------------------
'''

import os

class Config:
    """ Basic """
    DEBUG = True
    
    """ Security """
    SECRET_KEY = b'5\xc2\x11\xb6Q\xb7\xf3X\x00\xa5#<6\x1c\x8c\xae' # os.urandom(16)
    PARTICIPAN_KEY_LENGTH = 4
    USER_TOKEN_EXPIRES = 3600*24 # token life 1day

    """ DataBase """
    # mongodb
    MONGO_DB = 'E-Search'
    MONGO_SERVER_HOST = 'localhost'
    MONGO_SERVER_PORT = 27017
    MONGO_SERVER_PASSWORD = ''

    MONGODB_SETTINGS = {
        'db': MONGO_DB,
        'host': MONGO_SERVER_HOST,
        # 'password': MONGO_SERVER_PASSWORD,
        'port': MONGO_SERVER_PORT
    }