# -*- encoding: utf-8 -*-
'''
-------------------------------------------------------
@File    :   api.py
@Time    :   2020/07/05 17:50:21
@Author  :   RGDZ
@Version :   1.0.0
@Contact :   3303476267@qq.com
@License :   
@Desc    :   
-------------------------------------------------------
'''


from sanic import Blueprint
from sanic.response import json, text
from sanic.request import Request


from .status_code import StatusCode, RespData

api = Blueprint('api')

# API
@api.route('/')
async def index(request:Request):
    """ index """
    resp_data = RespData(StatusCode.SUCCESS)
    resp_data.data({'info':'This is test...'})
    return json(resp_data.dump())

    

