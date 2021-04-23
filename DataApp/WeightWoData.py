# -*- coding: utf-8 -*- 
# @Time : 2021/4/7 16:56 
# @Author : 张丽雯 
# @File : WeightWoData.py 
# @中文描述 :  称量工单数据

# ------------------------------------------------筛选工单数据---------------------------------------------------
WO1 = "WO00000293"
WO2 = "WO00000032"
# -------------------------------------------------------------------------------------------------------------
# ------------------------------------------------净重称量数据---------------------------------------------------
n1 = '0'
n2 = '3'
tarevalue1 = '0.015'
tarevalue2 = '1'
tarevalue3 = '0.001'
selectmode1 = "结束称量"
selectmode2 = "取消称量"
selectmode3 = "相同容器"
over_net = [(n2,tarevalue1,selectmode1)]
cancel_net = [(n2,tarevalue2,selectmode2)]
same_net = [(n2,tarevalue3,selectmode3)]
# --------------------------------------------------------------------------------------------------------------

# ------------------------------------------------人工输入称量数据-------------------------------------------------
n3 = '3'
netvalue1 = '0.02'
netvalue2 = '1'
netvalue3 = '0.001'
manual_list = [(n3,netvalue1,tarevalue1),(n3,netvalue1,tarevalue2),(n3,netvalue1,tarevalue3)]
# --------------------------------------------------------------------------------------------------------------

# ------------------------------------------------计数称量数据----------------------------------------------------
count_list = [(n1,tarevalue1),(n1,tarevalue2),(n1,tarevalue3)]
# --------------------------------------------------------------------------------------------------------------