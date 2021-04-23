# -*- coding: utf-8 -*- 
# @Time : 2021/4/23 9:56 
# @Author : 张丽雯 
# @File : test_stolocationmove_abnormal.py 
# @中文描述 :  库位移动异常场景用例
import pytest
import sys
from src.pageobjectAPP.pageStolocationmove import *
from src.public.common.Close_current_tab import *
from src.public.common.Select_Item import *

class Test_stolocation_move:
    def setup_class(self):
        app_login(username, password)
        login_stolocationmove()
        stolocation_move('1234', 'LOT0000003 0008')
        sleep(2)

    def teardown_class(self):
        Close_current_tab()
        app_logout()

    # 移动库位-容器ID异常
    @pytest.mark.parametrize('target,ID',[('1234',' '),('3333','LOT0000003')])
    def test_stolocation_move_abnormal_001(self,target,ID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        new_click(target_location)
        ele = new_find_elements(type_text)
        new_send_keys_ele(ele[10], target)
        sleep(1)
        new_click(select1)
        new_click(select_submit)
        new_send_keys_ele(ele[1], ID)
        new_click(title)
        sleep(2)
        assert is_text_present('不存在该条码的托盘或容器')

    # 移动库位-移动前后库位相同
    @pytest.mark.parametrize('target,ID',[('1234','LOT0000003 0008')])
    def test_stolocation_move_abnormal_002(self,target,ID):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        for i in range(15):
            new_backspace('//form/div/div[2]/div/div/div[1]/div/input')
        stolocation_move(target,ID)
        assert is_text_present('目标位置和初始位置不能相同')

