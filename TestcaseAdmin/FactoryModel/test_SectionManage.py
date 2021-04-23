# coding=utf-8

"""
Created on 2020/9/14
@author: zhangliwen
@desc:HoliEBR-Admin
"""
import sys
import pytest
from src.pageobjectAdmin.pageSectionManage import *
from DataAdmin.SectionManageData import *
from src.public.Logger import Log
from src.public.common.Search_Item import *
from src.public.common.relation_remove import *


class Test_Section_Manage():
    # 登陆环境
    # def setup_class(self):
    #     admin_login(admin_username, admin_password)
    #
    # def teardown_class(self):
    #     admin_logout()

    # 进入工厂模型-区段管理页面
    def test_section_manage(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        login_section_manage()
        sleep(1)

    # 新增区段
    def test_section_add(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        section_manage_add(section_code,add_name,add_type1)
        assert new_page_source(add_name)

    # 筛选区段
    def test_section_search(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',section_code)
        assert new_page_source(add_name)

    # 编辑区段
    def test_section_edit(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        section_manage_edit(edit_name,edit_type,storetype)
        assert new_page_source(edit_name)

    # 关联位置
    def test_section_relation(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_relation()

    #去关联
    def test_section_remove(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_remove()


    # 删除区域
    def test_section_delete(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        section_manage_delete()

    # 清除筛选条件
    def test_section_search_clear(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',' ')