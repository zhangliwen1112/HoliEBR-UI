# -*- coding: utf-8 -*- 
# @Time : 2021/4/7 9:27 
# @Author : 张丽雯 
# @File : pageWeightwo.py 
# @中文描述 :  称量工单-称量模式页面逻辑方法

from ElementApp.WeightwoPage import *
from ElementApp.WeightPage import weightmanage
from src.public.common.Login import *
from src.public.common.elements import *


# 进入称量工单页面
def login_weightwo():
    new_click(weightmanage)
    new_click(weightwo)
    print('进入称量工单页面')


# 净重称量模式
def weight_wo_net(n, tarevalue, selectmode='结束称量', isover='是'):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    new_click(weight_mode)
    new_click(net_mode)

    # 通过容器列表选择
    new_click(container_list)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)

    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    new_click(verify)
    sleep(1)
    if is_text_present('误差!衡器误差:'):
        sleep(2)
        new_click(yes_button)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    while is_element_present(message_alert):
        sleep(1)
        new_click(submit)
    new_type_double(tare, tarevalue)
    sleep(1)
    new_click(verify)
    sleep(3)
    new_click(verify)
    sleep(2)
    if new_page_source('称量量已超出容器剩余量，确定要继续吗？'):
        new_click(yes_button)
        sleep(1)
    if selectmode == '结束称量':
        new_click(weighFin)
    elif selectmode == '相同容器':
        new_click(SamContainer)
    else:
        new_click(CanWeigh)
    sleep(1)
    if new_page_source('是否结束容器？'):
        if isover == '是':
            new_click(over_button)
        else:
            new_click(nover_button)

# 人工输入称量模式
def weight_wo_manual(n, netvalue, tarevalue):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    new_click(weight_mode)
    new_click(manual_mode)
    # 通过容器列表选择
    new_click(container_list)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(3)
    new_click(verify)
    sleep(1)
    while is_element_present(message_alert):
        sleep(1)
        new_click(submit)
        sleep(1)
    sleep(2)
    for i in range(1, 15):
        new_backspace(net)
    new_type(net, netvalue)
    sleep(2)
    new_click(net)
    new_type_double(tare, tarevalue)
    sleep(1)
    new_click(verify)
    sleep(2)
    if is_text_present('记录称量'):
        sleep(1)
        new_click(manual_submit)
    sleep(2)


# 计数称量模式
def weight_wo_count(n, tarevalue, isover='是'):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    new_click(weight_mode)
    new_click(counting_mode)
    # 通过容器列表选择
    new_click(container_list)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(3)
    new_click(verify)
    sleep(1)
    if is_text_present('误差!衡器误差:'):
        sleep(1)
        new_click(yes_button)
    while is_element_present(message_alert):
        sleep(1)
        new_click(submit)
        sleep(1)
    new_type_double(tare, tarevalue)
    sleep(1)
    new_click(verify)
    sleep(2)
    new_click(verify)
    sleep(1)
    if is_text_present('记录称量'):
        sleep(1)
        new_click(manual_submit)
    sleep(1)
    if is_text_present('是否结束容器？'):
        if isover == '是':
            new_click(over_button)
        else:
            new_click(nover_button)

# 批次信息
def weight_wo_lot_detail(n):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    # 通过容器列表选择
    new_click(container_list)
    sleep(0.5)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    new_click(lot_detail)
    if new_get_text(container) == new_js_text(input_container):
        print('批次信息容器号是：', new_get_text(container))
    else:
        print('批次信息容器号不正确！')
    if new_get_text(lot) == new_js_text(input_container)[:-5]:
        print('批次信息批次号是：', new_get_text(lot))
    else:
        print('批次信息批次号不正确！')
    sleep(2)
    new_click(closed)


# 取消称量
def weight_wo_cancel(n,cancelweight1='否',cancelweight2='否'):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    # 通过容器列表选择
    new_click(container_list)
    sleep(0.5)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    if cancelweight1 == '取消称量':
        new_click(cancel_weight)
    else:
        new_click(verify)
        sleep(1)
        if is_text_present('误差!衡器误差:'):
            sleep(1)
            new_click(yes_button)
        while is_element_present(message_alert):
            sleep(1)
            new_click(submit)
            sleep(1)
        new_click(verify)
        if cancelweight2 == '取消称量':
            new_click(cancel_weight)

# 输入容器ID
def weight_wo_container_ID(ID):
    new_type_double(containerID,ID)
    new_click(material_msg)

# 净重称量-获取净重值
def weight_wo_net_netvalue(n, tarevalue):
    # 选择工单物料
    new_click(material(n))
    sleep(1)
    new_click(weight_mode)
    new_click(net_mode)

    # 通过容器列表选择
    new_click(container_list)
    new_click(select_container)
    sleep(0.5)
    new_click(submit)

    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    new_click(verify)
    sleep(1)
    if is_text_present('误差!衡器误差:'):
        sleep(2)
        new_click(yes_button)
    while is_element_present(alert):
        new_click(yes_button)
        sleep(2)
    while is_element_present(message_alert):
        sleep(1)
        new_click(submit)
    new_type_double(tare, tarevalue)
    sleep(1)
    new_click(verify)
    sleep(3)
    new_click(verify)
    sleep(2)
    net_value = new_js_text(net_number)
    print(net_value)
    tare_value = new_js_text(tare_number)
    print(tare_value)

