# -*- coding: utf-8 -*- 
# @Time : 2021/1/21 9:41 
# @Author : 张丽雯 
# @File : DeviceManagePage.py 
# @中文描述 :  设备管理-设备管理页面元素

# 登录页码元素
device = "//*[contains(text(),'设备管理')]"
device_manage = "//div[@class='v-list-group__items']//*[contains(text(),'设备管理')]"

# 列表上端按钮
assigned = "//span[text()='指派']"
available = "//span[text()='可指派']"
unavailable = "//span[text()='不可指派']"
release = "//span[text()='释放']"
move = "//span[text()='移动']"
transfer = "//span[text()='转移']"
online = "//span[text()='上线']"
offline = "//span[text()='离线']"
edit = "//span[contains(.,'编辑')]"
automatic = "//span[text()='自动']"
manual = "//span[text()='手动']"
update = "//span[text()='更新']"
label = "//span[text()='标签']"
check = "//span[text()='查看']"
refresh = "//span[text()='刷新']"

# -----------------------------------------指派页面元素------------------------------------------
select_wo = "//input[@readonly='readonly']"
select_wo1 = "//tbody//tr[1]"  #选择第一个工单
select_wo_submit = "//div[@class='text-sm-right pt-2']//span[text()='确定']"

# -----------------------------------------备注、提交按钮元素（指派页面、转移等页面均一样）--------------------------------------
first_row = "//span[@ref='eCellValue'][text()='1']"   #选择第一行，序号为1
comments = "//textarea"
submit = "//span[text()='确定']"
tips_submit = "//div[@class='DialogActions']//span[contains(.,'确定')]"  #弹框确定按钮



