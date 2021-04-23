# -*- coding: utf-8 -*- 
# @Time : 2021/1/21 9:40 
# @Author : 张丽雯 
# @File : pageDeviceManage.py 
# @中文描述 :  设备管理-设备管理界面

from ElementApp.DeviceManagePage import *
from src.public.common.Login import *


# 进入设备管理界面
def login_device_manage():
    new_click(device)
    new_click(device_manage)
    print('进入设备管理界面')


# 不可指派
def device_manage_unavailable(text):
    new_click(first_row)
    new_click(unavailable)
    new_type(comments, text)
    new_click(submit)


# 可指派
def device_manage_available(text):
    new_click(first_row)
    new_click(available)
    new_type(comments, text)
    new_click(submit)


# 手动
def device_manage_manual():
    new_click(first_row)
    new_click(manual)
    new_click(tips_submit)


# 自动
def device_manage_automatic():
    new_click(first_row)
    new_click(automatic)
    new_click(tips_submit)


# 离线
def device_manage_offline():
    new_click(first_row)
    new_click(offline)
    new_click(tips_submit)


# 上线
def device_manage_online():
    new_click(first_row)
    new_click(online)
    new_click(tips_submit)


# 标签
def device_manage_label(text):
    new_click(first_row)
    new_click(label)
    new_type(comments, text)
    new_click(submit)
