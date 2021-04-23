# -*- coding: utf-8 -*- 
# @Time : 2021/1/29 16:53 
# @Author : 张丽雯 
# @File : pageStolocationmove.py
# @中文描述 :  库位移动
from ElementApp.StolocationmovePage import *
from src.public.common.Login import *

#进入库位移动界面
def login_stolocationmove():
    new_click(inventory)
    new_click(stolocationmove)
    print('进入库位移动页面!')

# 移动库位
def stolocation_move(target,Cid):
    new_click(target_location)
    ele = new_find_elements(type_text)
    new_send_keys_ele(ele[10], target)
    sleep(1)
    new_click(select1)
    new_click(select_submit)
    new_send_keys_ele(ele[1],Cid)
    new_click(title)
    new_click(move)
    sleep(2)
    if new_page_source("物料位置不兼容"):
        new_click(location_submit)
    if new_page_source('目标库位的库区与物料上设定的默认/备用库区不兼容,是否继续执行该操作？'):
        new_click(yes_button)
    sleep(2)

def stolocation_detail(target,Cid):
    new_click(target_location)
    ele = new_find_elements(type_text)
    new_send_keys_ele(ele[10], target)
    sleep(2)
    new_click(select1)
    new_click(select_submit)
    new_send_keys_ele(ele[1],Cid)
    new_click(title)
    new_click(detail)
    sleep(2)
    new_click(location_submit)





