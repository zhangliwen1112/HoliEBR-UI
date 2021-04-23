# -*- coding: utf-8 -*- 
# @Time : 2020/11/18 11:22 
# @Author : 张丽雯 
# @File : AttributivelistData.py
# @中文描述 :  属性列表
import random
import string

attributive_code = ''.join(random.sample(string.digits + string.ascii_letters, 4))
attributive_type = '状态'
# attributive_type = '列表'
attributive_name = 'xinzeng_attributive1'
code_value = '2'
code_name = '12'
select_rule = '超过有效期'
edit_name = 'xiugai_attributive1'

# 复制属性数据
copy_code = 'fuzhi_' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
copy_name = "copy_name0" + ''.join(random.sample(string.digits + string.ascii_letters, 4))
