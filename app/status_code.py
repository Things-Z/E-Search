# -*- encoding: utf-8 -*-
'''
-------------------------------------------------------
@File    :   status_code.py
@Time    :   2020/07/05 18:10:21
@Author  :   RGDZ
@Version :   1.0.0
@Contact :   3303476267@qq.com
@License :   
@Desc    :   
-------------------------------------------------------
'''

class StatusCode:
    """ Background status code """
    NULL = 0 # Nothing
    ERROR = 100 # Execution error
    SUCCESS = 200 # Sucess
    NOT_ADMIN = 300 # Not admin
    ADMIN_BUT_NOEXEC = 301 # Is admin, but no code is executed
    NOT_LOGIND = 400 # Not Login
    LOGIND_BUT_NOEXEC = 401 # Is Login，but no code is executed
    TOKEN_LOSE = 500 # Token dead
    VERIFY_DATA = 800 # verify data
    VERIFYD_BUT_NOEXEC = 801 # verify data success, but no code is executed
    BAD_DATA = 900 # bad data
    NO_EXISTSED = 1000 # The data doesn't exist
    EXISTSED = 1001 # The data already exists

    @classmethod
    def codeMsg(cls, code:int)->str:
        return cls.allCode()[code]

    @classmethod
    def allCode(cls)->dict:
        data = {}
        for name, value in vars(cls).items():
            if type(value) is int:
                data.update({value:name})
        return data


class RespData:
    """ create data
    data = {
        'code':Status.Code,
        'msg':Status.Code.msg
        'data':data
    }
    """
    __code:int = 0
    __data:dict = {}
    def __init__(self, code:int=StatusCode.NULL, data:dict=None):
        self.__code = code
        self.__data = data if data else {}

    def code(self, code:int=None)->int:
        if code:
            self.__code = code
        return self.__code

    def msg(self)->int:
        return StatusCode.codeMsg(self.__code)

    def data(self, data:dict=None):
        if data:
            self.__data.update(data)
        return self.__data

    def dump(self):
        return {'code':self.code(), 'msg':self.msg(), 'data':self.data()}


if __name__ == "__main__":
    print(StatusCode.codeMsg(StatusCode.SUCCESS))
