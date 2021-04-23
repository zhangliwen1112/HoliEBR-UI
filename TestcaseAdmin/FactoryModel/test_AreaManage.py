# -*- coding: utf-8 -*- 
# @Time : 2021/1/18 16:19 
# @Author : 张丽雯 
# @File : test_AreaManageCase.py 
# @中文描述 :  区域管理

import sys
import pytest
from src.pageobjectAdmin.pageAreaManage import *
from DataAdmin.AreaManageData import *
from src.pageobjectAdmin.pageCompanyManage import login_Factory
from src.public.Logger import Log
from src.public.common.Search_Item import *
from src.public.common.relation_remove import *


class Test_Area_Mange:
    # 登陆环境
    def setup_class(self):
        admin_login(admin_username, admin_password)
        login_Area_Manage()


    # def teardown_class(self):
    #     admin_logout()

    # 新增区域
    @pytest.mark.parametrize(('code','name'),add_data)
    def test_area_add(self,code,name):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Area_Manage_add(code,name)
        assert new_page_source(name1)

    # 筛选
    def test_device_search(self):
        log = Log()
        log .info('开始执行用例%s' % sys._getframe().f_code.co_name)
        search_item('编码',code1)
        sleep(2)
        assert new_page_source(name1)

    # 编辑区域
    def test_area_edit(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Area_Manage_edit(edit_name)
        assert new_page_source(edit_name)

    # 关联位置
    def test_area_relation(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_relation()

    #去关联
    def test_area_remove(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_remove()

    # 删除区域
    def test_area_delete(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Area_Manage_delete()

    # 清除筛选条件
    def test_section_search_clear(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',' ')