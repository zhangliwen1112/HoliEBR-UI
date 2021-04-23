# -*- coding: utf-8 -*-

# @Time : 2021/1/13
# @Author : lianxiujuan
# @File : pageusergp.py
# @中文描述 :  用户组

from ElementAdmin.UsergroupPage import *
from src.public.FunctionSet import *


# 进入用户组界面
def login_usergp():
    new_click(authmg)
    new_click(userauth)

# 新增用户组
def usergp_add(addcode, addname):
    new_click(add)
    ele = new_find_elements(input)
    new_send_keys_ele(ele[1], addcode)
    new_send_keys_ele(ele[2], addname)
    new_click(yes_button)

# 勾选/去勾选权限
def usergp_setauth():
    ele = new_find_elements(authlist)
    new_click_ele(ele[1])

# 编辑用户组
def usergp_edit(editname):
    new_click(edit)
    ele = new_find_elements(input)
    new_send_keys_ele(ele[1], editname)
    new_click(yes_button)

# 删除用户组
def usergp_delete():
    new_click(delete)
    new_click(delete_yes_button)
