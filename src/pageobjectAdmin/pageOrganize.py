# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 16:30 
# @Author : 张丽雯 
# @File : pageOrganize.py 
# @中文描述 :  组织机构

from src.public.common.Login import *
from ElementAdmin.organizePage import *
from src.public.common.elements import error_tips


# 进入组织机构页面
def login_organize_manage():
    new_click(organize)
    print('进入组织机构页面！')


# 新增企业
def organize_add_orgcom(name, code, type):
    new_click(o_add)
    ele = driver.find_elements_by_xpath(input_option)
    new_send_keys_ele(ele[1],name)
    new_send_keys_ele(ele[2],code)
    if type == '公司':
        new_click(OrganType2)
    else:
        new_click(OrganType3)
    new_click(OrganUpper)
    new_click(Upper1)
    new_click(Upper2)
    new_click(add_submit)
    sleep(0.5)
    # 异常判断
    if is_element_present(error_tips):
        new_get_text(error_tips)
    if new_page_source('请按照格式要求填写数据'):
        driver.find_elements_by_xpath(add_cancel)[2].click()



# 编辑企业
def organize_edit_orgcom(name, type):
    new_click(group)
    new_click(company1)
    new_click(company1_1)
    new_click(o_edit)
    ele = driver.find_elements_by_xpath(input_option)
    new_send_keys_ele(ele[1], name)
    if type == '公司':
        new_click(OrganType2)
    else:
        new_click(OrganType3)
    new_click(OrganUpper)
    new_click(Upper1)
    new_click(Upper2)
    new_click(add_submit)
    sleep(0.5)
    if is_element_present(error_tips):
        new_get_text(error_tips)
    # 异常判断
    if new_page_source('请按照格式要求填写数据'):
        driver.find_elements_by_xpath(add_cancel)[2].click()
    new_click(group)


# 删除新增企业
def organize_delete_orgcom():
    new_click(group)
    new_click(company1)
    new_click(company1_1)
    new_click(o_delete)
    new_click(delete_submit)


# 刷新左侧组织机构树表结构
def organize_refresh_orgcom():
    new_click(o_refresh)


# 新增用户名
def organize_user_add(user, code, tel, status, male):
    new_click(add)
    ele = driver.find_elements_by_xpath(input_option)
    new_send_keys_ele(ele[4], user)
    new_send_keys_ele(ele[5], code)
    new_send_keys_ele(ele[6], tel)
    new_click(add_UserSta)
    if status == '离职':
        new_click(UserSta_off)
    else:
        new_click(UserSta_online)
    if male == '男':
        new_click(UserMale1)
    else:
        new_click(UserMale2)
    new_click(UserDate)
    sleep(1)
    new_click(UserDate_first)
    new_click(UserOrg1)
    driver.find_elements_by_xpath(User_submit)[3].click()
    sleep(0.5)
    # 异常判断
    if is_element_present(error_tips):
        new_get_text(error_tips)
    if new_page_source('请按照格式要求填写数据'):
        driver.find_elements_by_xpath(add_cancel)[4].click()


# 修改新增的用户
def organize_user_edit(name, tel, status):
    new_click(edit)
    sleep(0.5)
    ele = driver.find_elements_by_xpath(input_option)
    new_send_keys_ele(ele[4], name)
    new_send_keys_ele(ele[6], tel)
    new_click(edit_UserSta)
    if status == '离职':
        new_click(UserSta_off)
    else:
        new_click(UserSta_online)
    new_click(UserOrg2)
    driver.find_elements_by_xpath(User_submit)[3].click()
    sleep(0.5)
    # 异常判断
    if is_element_present(error_tips):
        new_get_text(error_tips)
    if new_page_source('请按照格式要求填写数据'):
        driver.find_elements_by_xpath(add_cancel)[4].click()


# 删除增加的用户
def organize_user_delete():
    new_click(delete)
    driver.find_elements_by_xpath(DetUser_submit)[1].click()


# 刷新列表
def organize_user_refresh():
    new_click(refresh)
