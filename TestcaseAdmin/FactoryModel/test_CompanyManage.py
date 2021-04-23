# coding=utf-8

"""
Created on 2020/9/8
@author: zhangliwen
@desc:admin 企业管理界面
"""
import sys
import pytest
from src.pageobjectAdmin.pageCompanyManage import *
from DataAdmin.CompanyManageData import *
from src.public.Logger import Log
from src.public.common.Search_Item import *
from src.public.common.relation_remove import *


class Test_Company_Manage:
    # 登陆环境,进入工厂模型-企业管理页面
    def setup_class(self):
        # admin_login(admin_username, admin_password)
        login_Company_Manage()
        sleep(2)

    # def teardown_class(self):
    #     admin_logout()


    # 新增企业
    @pytest.mark.parametrize(('code','name'),data)
    def test_company_add(self,code,name):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Company_Manage_add(code,name)
        assert new_page_source(code)

    # 筛选企业
    def test_company_search(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',code01)
        assert new_page_source(code01)

    # 编辑企业
    def test_company_edit(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Company_Manage_edit(editname)
        assert new_page_source(editname)


    # 关联位置
    def test_company_relation(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_relation()

    #去关联
    def test_company_remove(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Manage_remove()


    # 删除区域
    def test_company_delete(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        Company_Manage_delete()

    # 清除筛选条件
    def test_section_search_clear(self):
        log = Log()
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item('编码',' ')

