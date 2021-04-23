#coding=utf-8

"""
Created on 2020/11/18
@author: lianxiujuan
@desc: 标签-预产出容器
"""

import pytest
import sys
from DataApp.LabelmgData import *
from src.public.common.Login import *
from src.pageobjectAPP.pageLabel import *
from src.public.common.Select_Item import *
from src.public.common.Search_Item import *
import random,string

labeldata = ''.join(random.sample(string.ascii_letters + string.digits, 4))


class Test_precontainerlabel:
    def setup_class(self):
        app_login(username, password)
        login_label()
        ele = new_find_elements(container)
        new_click_ele(ele[2])
        time.sleep(2)
        label_add(labeldata, labeldata, labeldata, labeldata)
        time.sleep(2)

    def teardown_class(self):
        app_logout()

    # 新增 标签-预产出容器
    def test_add_precontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_add(precontainercode, precontainername, precontainerdesc, precontainerzpl)
        time.sleep(2)
        assert new_page_source(precontainercode)

    # 搜索 标签-预产出容器
    def test_search_precontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        search_item("编码", precontainercode)
        time.sleep(2)
        ele = new_find_elements(searchresult)
        text = new_get_text_ele(ele[0])
        time.sleep(2)
        assert precontainercode in text
        search_item("编码", ' ')
        time.sleep(2)

    # 编辑 标签-预产出容器
    def test_edit_precontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(precontainercode)
        label_edit(editname, editdesc, editzpl)
        time.sleep(2)
        assert new_page_source(editname)

    # 设置标准模板
    def test_setdefault_precontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        label_setdefault()
        time.sleep(2)
        select_item(labeldata)
        label_setdefault()
        time.sleep(2)

    # 删除 标签-预产出容器
    def test_delete_precontainerlabel(self):
        log.info("开始执行用例%s" % sys._getframe().f_code.co_name)
        select_item(precontainercode)
        label_delete()
        time.sleep(2)
        assert new_page_source(precontainercode) == False


if __name__ == '__main__':
    pytest.main(['-s','test_preprecontainerlabelcase.py'])
