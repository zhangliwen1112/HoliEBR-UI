# -*- coding: utf-8 -*- 
# @Time : 2020/11/19 9:09 
# @Author : 张丽雯 
# @File : EqpcategoryData.py 
# @中文描述 :  设备类别接口
import random
import string

text = 'xinz'
eqpcode = 'code' +''.join(random.sample(string.digits + string.ascii_letters, 4))
eqpname = 'name' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
code = 'outcode' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
name = 'outname' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
type1 = '数字'

addcode = 'incode' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
addname = 'inname' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
outcode = 'outcode' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
outname = 'outname' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
editname = 'editname' + ''.join(random.sample(string.digits + string.ascii_letters, 4))
type2 = '文本'