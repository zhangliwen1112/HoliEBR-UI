# coding=utf-8

"""
Created on 2020/10/14
@author: lianxiujuan
@desc: 标准托盘页码元素
"""

# 登录页码元素
inventory = "//*[text()='库存管理']"
pallet = "//*[text()='托盘']"
stdpallet = "//*[text()='标准托盘']"

# 标准托盘上端按钮
add = "//*[text()='新增']"
edit = "//*[text()='编辑']"
delete = "//*[text()='删除']"

# 新增/编辑标准托盘界面元素
allselect = '//div[@class="v-card v-sheet theme--light"]//i[text()="arrow_drop_down"]'
type1 = "//div[@role='listbox']/div[1]"  # 每次选择第一个
allinput = '//div[@class="v-card v-sheet theme--light"]//input[@type="text"]'
yes_button = '//div[@class="v-card v-sheet theme--light"]//span[text()="确定"]'
cancle = '//div[@class="v-card v-sheet theme--light"]//span[text()="取消"]'
# 删除标准托盘
delete_yes_button = '//button[@color="red"]'

#选中第一条
first = "//div[@role='row' and @row-index='0']//div[@col-id='code']"
