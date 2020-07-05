# -*- encoding: utf-8 -*-
'''
-------------------------------------------------------
@File    :   run.py
@Time    :   2020/07/05 17:47:22
@Author  :   RGDZ
@Version :   1.0.0
@Contact :   3303476267@qq.com
@License :   
@Desc    :   Start E-Search App
-------------------------------------------------------
'''

from app import app


if __name__ == "__main__":
    app.run(debug=True)