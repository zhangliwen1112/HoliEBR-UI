# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:04 
# @Author : lianxiujuan 
# @File : pageRiskprevention.py
# @中文描述 : 危险防范信息-page


from ElementApp.Riskprevention import *
from src.public.FunctionSet import *


# 进入危险防范信息界面
from src.public.common.elements import error_message, error_message2


def login_Riskprevention():
    new_click(material)
    new_click(riskpre)

# 新增危险防范信息
def riskprevention_add(addcode, cdescdata, edescdata):
    new_click(add)
    ele = new_find_elements(allinput)
    new_send_keys_ele(ele[0], addcode)
    new_send_keys_ele(ele[1], cdescdata)
    new_send_keys_ele(ele[2], edescdata)
    new_click(yes_button)
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(no_button)
    elif is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(no_button)
    sleep(0.5)

# 编辑危险防范信息
def riskprevention_edit(editcdescdata, editedescdata):
    new_click(edit)
    ele = new_find_elements(allinput)
    new_type_double_ele(ele[1], editcdescdata)
    new_type_double_ele(ele[2], editedescdata)
    new_click(yes_button)
    if is_element_present(error_message):
        new_get_text(error_message)
        new_click(no_button)
    elif is_element_present(error_message2):
        new_get_text(error_message2)
        new_click(no_button)
    sleep(0.5)

# 删除危险防范信息
def riskprevention_delete():
    new_click(delete)
    new_click(delete_yes_button)
