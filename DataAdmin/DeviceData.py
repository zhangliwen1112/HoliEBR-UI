# -*- coding: utf-8 -*- 
# @Time : 2021/1/19 15:43 
# @Author : 张丽雯 
# @File : DeviceData.py 
# @中文描述 :  外部设备

device_code01 = 'dcode01'
device_name01 = '电子秤新增01'
device_type01 = '电子秤'
device_status01 = '在线'
device_address01 = 'ws://172.26.15.5:3000/api/ws/scale'
device_des01 = '电子秤新增'

device_code02 = 'dcode02'
device_name02 = '手环新增02'
device_type02 = '手环'
device_status02 = '注册'
device_address02 = 'ws://172.26.15.5:3000/api/ws/rfid'
device_des02 = '手环新增'

device_code03 = 'dcode03'
device_name03 = '打印机新增03'
device_type03 = '打印机'
device_status03 = '离线'
device_address03 = 'http://172.26.15.5:3000/api/print'
device_des03 = '打印机新增'

add_data = [
        (device_code01,device_name01,device_type01,device_status01,device_address01,device_des01),
        (device_code02,device_name02,device_type02,device_status02,device_address02,device_des02),
        (device_code03,device_name03,device_type03,device_status03,device_address03,device_des02)
            ]

edit_name01 = '电子秤修改'
edit_type01 = '电子秤'
edit_status01 = '注销'
edit_address01 = 'ws://172.26.15.5:3000/api/ws/scale'
edit_des01 = '电子秤状态修改'

delete_data = [device_code01,device_code02,device_code03]