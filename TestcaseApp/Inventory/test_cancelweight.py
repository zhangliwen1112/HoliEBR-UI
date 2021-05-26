# -*- coding: utf-8 -*- 
# @Time : 2021/2/1 16:22 
# @Author : 张丽雯 
# @File : test_cancelweight.py 
# @中文描述 :  取消称量--取消称量
import pytest
import sys
from src.pageobjectAPP.pageCancelWeight import *
from src.public.common.Close_current_tab import *
from DataApp.CancelWeightData import *

class Test_cancel_weighting:

    def test_login(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_cancel_weight()
        new_page_source('取消称量')

    def test_cancel_execute(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        cancel_weight_execute(label3)
        Close_current_tab()