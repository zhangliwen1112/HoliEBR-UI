# -*- coding: utf-8 -*- 
# @Time : 2021/4/7 13:39 
# @Author : 张丽雯 
# @File : WeightwoPage.py 
# @中文描述 :  称量工单页面元素

weightwo = "//*[contains(text(),'称量工单')]"
weight_mode = "//div[@class='v-select__selections']"
net_mode = "//div[@class='v-list-item__title'][text()='净重']"
manual_mode = "//div[@class='v-list-item__title'][text()='人工输入']"
counting_mode = "//div[@class='v-list-item__title'][text()='计数']"
containerID = "//div[@class='layout pt-2']//input[@type='text']"
# 容器列表界面
container_list = "//button/span[text()='容器列表']"
select_container = "//div[@class='container']//div[@role='row' and @aria-rowindex='2']" #选择第一行的容器
submit = "//span[text()='确定']"
verify = "//button/span[text()='验证']"
input_container = "//form/div[2]/div/div/div/div[1]/div/input"
# 净重
net = '//form/div[3]/div[2]/div/div[1]/div/div/div[1]/div/input'
# 皮重
tare = "//form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/input"
tare1 = "//div[@class='v-input v-input--is-label-active v-input--is-dirty theme--light v-text-field v-text-field--is-booted']//input[@type='text']"
# 异常信息弹框
alert = "//div[@class='v-card v-sheet v-sheet--tile theme--light']"
yes_button = "//div[@class='DialogActions']//span[contains(.,'确定')]"
no_button = "//div[@class='DialogActions']//span[contains(.,'取消')]"
over_button = "//div[@class='DialogActions']//span[contains(.,'是')]"
nover_button = "//div[@class='DialogActions']//span[contains(.,'否')]"
# 清洁规则、危险信息弹框
message_alert = "//div[@class='v-dialog v-dialog--active v-dialog--persistent v-dialog--scrollable']"

# 工单物料列表--n表示第几个物料，0,1,2... 表示第一个、第二个、第三个....
def material(n):
    return "//div[@class='layout column fill-height ma-0']//div[@row-index='"+n+"']//div[@aria-colindex='1']"

# 净重称量结果选择
weighFin = "//span[contains(.,'结束称量')]"
SamContainer = "//span[contains(.,'相同容器')]"
CanWeigh = "//span[contains(.,' 取消称量')]"

# 人工输入记录称量弹框
manual_submit = "//div[@class='v-card__actions']//span[contains(.,'确定')]"

# 剩余量
remain_number = "//form/div[3]/div[1]/div/div[1]/div/div/div[1]/div/input"
# 净重
net_number = "//form/div[3]/div[2]/div/div[1]/div/div/div[1]/div/input"
# 皮重
tare_number = "//form/div[3]/div[2]/div/div[2]/div/div/div[1]/div/input"
# 秤
weightvalue = "//div[@class='cp_precentage']/span"
# 批次信息
lot_detail = "//button/span[text()='批次信息']"
lot = "//tr[1]/td[2]"
container = "//tr[1]/td[4]"
closed = "//div[@class='v-card__actions']//span[contains(.,'关闭')]"

# 取消称量
cancel_weight = "//button/span[text()='取消称量']"

# 界面右侧物料信息
material_msg = "//div/p[@class='text-truncate']"


