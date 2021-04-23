# -*- coding: utf-8 -*- 
# @Time : 2021/2/23 14:10 
# @Author : 张丽雯 
# @File : test_Organize_abnormal.py 
# @中文描述 :  组织机构异常场景用例
import sys
import pytest
from src.pageobjectAdmin.pageOrganize import *
from DataAdmin.OrganizeData import *
from src.public.common.Search_Item import *


class Test_Organize:
    # 登陆环境
    def setup_class(self):
        # admin_login(admin_username, admin_password)
        # sleep(1)
        login_organize_manage()

    def teardown_class(self):
        organize_user_delete()
        organize_delete_orgcom()
        # admin_logout()

    # 新增企业 -- 机构名称异常场景
    @pytest.mark.parametrize('add_name, code, add_type', add_orgname_abnormal_list)
    def test_add_orgcom_name_abnormal(self,add_name, code, add_type):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_add_orgcom(add_name, code, add_type)
        assert new_page_source('请按照格式要求填写数据')

    # 新增企业 -- 机构编码异常场景
    @pytest.mark.parametrize('add_name, code, add_type', add_orgcode_abnormal_list)
    def test_add_orgcom_code_abnormal(self,add_name, code, add_type):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_add_orgcom(add_name, code, add_type)
        assert new_page_source('请按照格式要求填写数据')

    # 新增企业
    def test_add_orgcom(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_add_orgcom(add_name, code, add_type)
        sleep(1)
        assert new_page_source(add_name)

    # 编辑企业 -- 机构名称异常场景
    @pytest.mark.parametrize('edit_name, edit_type', edit_orgname_abnormal_list)
    def test_edit_orgcom_name_abnormal(self, edit_name, edit_type):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_edit_orgcom(edit_name, edit_type)
        assert new_page_source('请按照格式要求填写数据')

    # 新增用户--姓名异常场景
    @pytest.mark.parametrize('users, user_code, tel, status, male',add_user_abnormal_list)
    def test_org_username_add(self,users, user_code, tel, status, male):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_add(users, user_code, tel, status, male)
        assert new_page_source('请按照格式要求填写数据')

    # 新增用户--编码异常场景
    @pytest.mark.parametrize('users, user_code, tel, status, male',add_code_abnormal_list)
    def test_org_code_add(self,users, user_code, tel, status, male):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_add(users, user_code, tel, status, male)
        assert new_page_source('请按照格式要求填写数据')

    # 新增用户--电话号码异常场景
    @pytest.mark.parametrize('users, user_code, tel, status, male', add_tel_abnormal_list)
    def test_org_tel_add(self, users, user_code, tel, status, male):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_add(users, user_code, tel, status, male)
        assert new_page_source('请按照格式要求填写数据')

    # 新增用户
    def test_org_user_add(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_add(users, user_code, tel, status, male)
        sleep(1)
        assert new_page_source(users)

    # 修改用户--姓名异常场景
    @pytest.mark.parametrize('users, tel, status',edit_user_abnormal_list)
    def test_org_username_edit(self,users, tel, status):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_edit(users, tel, status)
        assert new_page_source('请按照格式要求填写数据')

    # 修改用户--电话号码异常场景
    @pytest.mark.parametrize('users, tel, status',edit_tel_abnormal_list)
    def test_org_tel_edit(self,users, tel, status):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        organize_user_edit(users, tel, status)
        assert new_page_source('请按照格式要求填写数据')
