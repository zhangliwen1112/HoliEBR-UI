# -*- coding: utf-8 -*- 
# @Time : 2021/2/5 14:46 
# @Author : 张丽雯 
# @File : 111.py 
# @中文描述 :

# !/usr/bin/python3
# while 来计算 1 到 100 的总和：
# n = 100
# sum = 0
# a = 1
# while a <= n:
#     sum = sum + a
#     a =a +  1
# print('1到%d 之和为： %d' %(n,sum))
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')
#
# if None:
#     print('hello')

# i=1
# while i<=9:
#      #里面一层循环控制每一行中的列数
#      j=1
#      while j<=i:
#           mut =j*i
#           print("%d*%d=%d"%(j,i,mut), end="  ")
#           j+=1
#      print("")
#      i+=1

# for i in range(1,10):
#     for j in range(1,10):
#         if j<=i:
#             mut = j * i
#             print("%d*%d=%d" % (j, i, mut), end=" ")  # end = '' 表示不换行
#             j += 1
#     print("\r")
#     i += 1

# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)

# while True:
#     number = input('请输入一个整数(输入Q退出程序)：')
#     if number in ['q','Q']:
#         break                #如果输入的是q或Q,结束退出
#     elif not number.isdigit():
#         print('您的输入有误！只能输入整数(输入Q退出程序)！请重新输入')
#         continue         #如果输入的数字不是十进制,结束循环,重新开始
#     else :
#             number = int(number)
#             print('十进制 --> 十六进制 ：%d -> 0x%x' %(number,number))
#             print('十进制 --> 八进制 ：%d -> 0o%o' %(number,number))
#             print('十进制 --> 二进制 ：%d ->'%number,bin(number))



# def paixu(li) :
#     max = 0
#     for ad in range(len(li) - 1):
#         for x in range(len(li) - 1 - ad):
#             if li[x] > li[x + 1]:
#                 max = li[x]
#                 li[x] = li[x + 1]
#                 li[x + 1] = max
#             else:
#                 max = li[x + 1]
#     print(li)
# paixu([41,23344,9353,5554,44,7557,6434,500,2000])
# import os
# import sys
#
# # list = [1,2,3,4]
# # it = iter(list)
# # while True:
# #     try:
# #         print(next(it))
# #     except StopIteration:
# #         sys.exit()
#
# # 迭代器
# # class MyNumbers:
# #     def __iter__(self):
# #         self.a = 1
# #         return self
# #
# #     def __next__(self):
# #         if self.a<20:
# #             x = self.a
# #             self.a += 1
# #             return x
# #         else:
# #            raise StopIteration
# #
# #
# # myclass = MyNumbers()
# # myiter = iter(myclass)
# #
# # for x in myiter:
# #     print(x,end= ' ')
#
# #
# # num = [1,3,6]
# # new = tuple(map(lambda x:x,num))
# # print(new)
#
# # f = open('a.txt','rb+')
# # f.write(b'0123456789abcdef')
# # f.write('python 是一个非常好的语言。 \n是的，的确非常好！\n')
# # f.tell()
# # print(f.tell())
# # print(f.seek(-3,2))
# # for a in f:
# #     print(a)
# # f.close()
#
# # from urllib import request
# # response = request.urlopen("http://www.baidu.com/")
# # fi = open("project.txt",'w')
# # page = fi.write(str(response.read()))
# # fi.close()
#
# # c = os.getcwd()
# # print('当前工作目录为 %s'%c)
# # print('当前工作目录为',c)
# #
# # while True:
# #     try:
# #         x = int(input('请输入一个整数：'))
# #         break
# #     except ValueError:
# #         print('您输入的不是数字，请再次尝试输入！')
# import sys
# #
# # try:
# #     f = open('myfile.txt')
# #     s = f.readline()
# #     i = int(s.strip())
# # except OSError as err:
# #     print("OS error:{0}".format(err))
# # except ValueError:
# #     print('Could not convert data to an integer')
# # except:
# #     print('unexpected error:',sys.exc_info()[0])
# #     raise
#
# # for arg in sys.argv[1:]:
# #     try:
# #         f = open(arg,'r')
# #     except IOError:
# #         print('cannot open',arg)
# #     else:
# #         print(arg,'has',len(f.newlines()),'lines')
# #         f.close()
#
# # # 九九乘法表
# # for i in range(1,10):
# #     for j in range(1,i+1):
# #         mun = j*i
# #         print('%d*%d=%d'%(j,i,mun),end=' ')
# #     print('\n')
#
# # 九九乘法表
# # i = 1
# # while i<10:
# #     j = 1
# #     while j<=i:
# #         mun = j*i
# #         print('%d*%d=%d' % (j, i, mun), end=' ')
# #         j = j + 1
# #     print('\n')
# #     i = i + 1
# from django.core.mail.backends import console
#
# from src.pageobjectAPP.pageMaterialSet import login_Material_Set
# from src.pageobjectAPP.pageWocompound import *
# from src.public.FunctionSet import *
# from src.public.common.Login import app_login, username, password
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# sd = 'kw'
# js1 = "document.getElementById('"+sd+"').value='as123'"
# print(js1)
# driver.execute_script(js1)
# js2="return  document.getElementById('kw').value"
# cc = driver.execute_script(js2)
# print(cc)
# driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)
# sleep(5)
# app_login(username, password)
# login_Material_Set()
# # login_Compounding()
# sleep(1)
# locat = (By.XPATH,"//div[@role='row' and @row-index='8']")
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(locat))
#
# ele = driver.find_element(*locat)
# driver.execute_script()

import os
import random

def creat_file(fileName,fileSize, fileSuffix):
    """
    生成一个固定大小的文件
    :param fileName: 文件名
    :param filePath: 文件存放路径
    fileSuffix:文件后缀名
    :return: 无
    """
    filePath = r"D:\2021\'" + fileName + fileSuffix
# 生成固定大小的文件
    ds = 0
    with open (filePath, 'w', encoding='utf8') as f:
        while ds < fileSize:
            f.write(str(round(random.uniform(-100,100),2)))
            f.write('\n')
            ds = os.path.getsize(filePath)
    if os.name == 'main':
        # 1 MB = 1024 kB
        size = {'1M':1024,'10M':10*1024,'1G':1024*1024}
        for key, vlaue in size.items():
            creat_file(key, vlaue,'.txt')


creat_file('test',1,'.txt')
