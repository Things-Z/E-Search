# -*- encoding: utf-8 -*-
'''
-------------------------------------------------------
@File    :   api.py
@Time    :   2020/07/05 17:50:21
@Author  :   RGDZ
@Version :   1.0.0
@Contact :   3303476267@qq.com
@License :   
@Desc    :   E-Search API
-------------------------------------------------------
'''


from sanic import Blueprint
from sanic.response import json, text
from sanic.request import Request


from .status_code import StatusCode, RespData
from .routes import Routes

api = Blueprint('api')

# API
@api.route(Routes.INDEX)
async def index(request:Request):
    """ index """
    resp_data = RespData(StatusCode.SUCCESS)
    resp_data.code = StatusCode.ERROR
    resp_data.data = {
        'info':'This is test...',
        'json':request.json,
        'args':request.args,
        'content-type':request.content_type}
    return json(resp_data.dump)

    

@api.route(Routes.API_SEARCH_BY_HASH)
async def searchByHash(request:Request):
    """ Search By File's Hash 
    method: GET/POST
    POST: {
        'hash':hash,
        'type':'md5/sha1/sha256/sha512'
    }
    GET: ?type=type&hash=hash
    """
    if request.method == "GET":
        hash_value = request.args.get('hash')[0]
        hash_type = request.args.get('type')[0]
    elif request.method == "POST" and request.content_type == "application/json":
        hash_value = request.json.get('hash')
        hash_type = request.json.get('type')
    # Search
    resp_data = RespData()
    if not hash_value or not hash_type:
        resp_data.code = StatusCode.NO_EXISTSED
        return json(resp_data.dump)
    resp_data.code = StatusCode.SUCCESS
    resp_data.data = {}
    return json(resp_data.dump)


@api.route(Routes.API_SEARCH_BY_URL)
async def searchByURL(request:Request):
    """ Search By URL 
    method: GET/POST
    POST: {
        'url':url,
    }
    GET: ?url=url
    """
    if request.method == "GET":
        url_value = request.args.get('url')[0]
    elif request.method == "POST" and request.content_type == "application/json":
        url_value = request.json.get('url')
    # Search
    resp_data = RespData()
    if not hash_value or not hash_type:
        resp_data.code = StatusCode.NO_EXISTSED
        return json(resp_data.dump)
    resp_data.code = StatusCode.SUCCESS
    resp_data.data = {}
    return json(resp_data.dump)

@api.route(Routes.API_SEARCH_BY_EMAIL)
async def searchByEmail(request:Request):
    """ Search By Email 
    method: GET/POST
    POST: {
        'email':email,
    }
    GET: ?email
    """
    if request.method == "GET":
        url_value = request.args.get('email')[0]
    elif request.method == "POST" and request.content_type == "application/json":
        url_value = request.json.get('email')
    # Search
    resp_data = RespData()
    if not hash_value or not hash_type:
        resp_data.code = StatusCode.NO_EXISTSED
        return json(resp_data.dump)
    resp_data.code = StatusCode.SUCCESS
    resp_data.data = {}
    return json(resp_data.dump)


