#coding=utf-8
#
# """
# Created on 2020/9/14
# @author: zhangliwen
# @desc: 工作中心-工作中心页面对象定义
# """

# 进入页面 xpath
Work_Centre = "//*[contains(text(),'工作中心')]"
Worker_Centre = "//a//span[contains(text(),'工作中心')]"


#页面上面按钮
add = '//*[contains(text(),"新增")]'
delete = '//*[contains(text(),"删除")]'
edit = '//*[contains(text(),"编辑")]'
fresh = '//*[contains(text(),"刷新")]'
show = "//span[contains(.,'显示列')]"
select = "//span[contains(.,'筛选')]"
ralated = '//*[contains(text(),"关联")]'

#新增页面元素
code = "//input[@placeholder='请输入编码']"
name = "//input[@placeholder='请输入名称']"
factory = "//form/div[2]/div/div/div/div/div/div/i"
factory1 = "//ul[2]/li[1]"
factory2 = "//ul[2]/li[2]"
factory3 = "//ul[2]/li[3]"
factory4 = "//ul[2]/li[4]"
area = "//div[2]/div/div/div/div/div/i"
area1 = "//div[8]/ul[2]/li"
location = "//div[3]/div/div/div/div/div/i"
location1 = "//div[9]/ul[2]/li"
store_section = "//div[4]/div/div/div/div/div/div/i"
store_section1 = "//div[11]/ul[2]/li"

submit = "//div[@class='ivu-modal-footer']//span[text()='确定']"

#删除确定取消按钮
delete_submit = "//button[@type='button']/span[text()='确定']"
delete_cancel = "//button[@type='button']/span[text()='取消']"

#选中第一条
First = "//div[@role=\"row\" and @row-index=\"0\"]"

#移动
movefirst = "//div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div"  #选中右侧第一个
removefirst = "//div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div" #选中左侧第一个
moveleft = "//b[contains(.,'<')]"
moveright = "//b[contains(.,'>')]"
