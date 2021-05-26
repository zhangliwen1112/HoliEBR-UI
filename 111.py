# -*- coding: utf-8 -*- 
# @Time : 2021/2/5 14:46 
# @Author : 张丽雯 
# @File : 111.py 
# @中文描述 :

# !/usr/bin/python3
# 编写一个函数来查找字符串组中的最长公共前缀，如果不存在公共前缀，返回空字符串。，例如输入：['flower','flow',flight'],输出：fl; 输入: ['dog','racecar','car']，返回''

def get_common_str(list_a):
    '''输入列表a，返回公共子串
    输入: ["flower","flow","flight"]
    输出: "fl"
    输入: ["dog","racecar","car"]输出: ""
    '''
    if len(list_a) == 0:
        return ''
    common_str = ''  # 公共字符串

    # 先找出最短的字符串
    min_str = min(list_a, key=lambda x: len(x))
    #print(min_str)  # 最短的字符串flow
    for i in range(len(min_str)):
        flag = False  # 退出外部循环标志
        for j in list_a:
            if min_str[i] != j[i]:
                common_str = min_str[:i]
                flag = True
                break
        if flag:
            break
    return common_str

if __name__ == '__main__':
    a = ["flower", "flow", "flight"]
    print(get_common_str(a))
    b = ["dog", "racecar", "car"]
    print(get_common_str(b))
