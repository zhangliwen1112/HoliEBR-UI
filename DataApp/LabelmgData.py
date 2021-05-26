#coding=utf-8

"""
Created on 2020/11/16
@author: lianxiujuan
@desc：标签管理数据
"""
# -------------------------------------------标签-区域-正常测试数据-------------------------------------------
areacode = "area"
areaname = "区域"
areadesc = "区域描述"
areazpl = "区域zpl"

sectorcode = "sector"
sectorname = "区段"
sectordesc = "区段描述"
sectorzpl = "区段zpl"

locationcode = "jfdks"
locationname = "位置"
locationdesc = "位置描述"
locationzpl = "位置zpl"

reserviorcode = "reservior"
reserviorname = "库区"
reserviordesc = "库区描述"
reserviorzpl = "库区zpl"

slocationcode = "stolocation"
slocationname = "库位"
slocationdesc = "库位描述"
slocationzpl = "库位zpl"

containercode = "roeiwu"
containername = "容器"
containerdesc = "容器描述"
containerzpl = "容器zpl"

palletcode = "pallet"
palletname = "托盘"
palletdesc = "托盘描述"
palletzpl = "托盘zpl"

opalletcode = "outputpallet"
opalletname = "产出托盘"
opalletdesc = "产出托盘描述"
opalletzpl = "产出托盘zpl"

ocontainercode = "outputcontainer"
ocontainername = "产出容器"
ocontainerdesc = "产出容器描述"
ocontainerzpl = "产出容器zpl"

precontainercode = "precontainer"
precontainername = "预产出容器"
precontainerdesc = "预产出容器描述"
precontainerzpl = "预产出容器zpl"

micontainercode = "micontainer"
micontainername = "MI产出容器"
micontainerdesc = "MI产出容器描述"
micontainerzpl = "Mi产出容器zpl"

rcontainercode = "receivecontainer"
rcontainername = "ldfjldsfjd"
rcontainerdesc = "接收容器描述"
rcontainerzpl = "接收容器zpl"

rpalletcode = "receivepallet"
rpalletname = "接收托盘"
rpalletdesc = "接收托盘描述"
rpalletzpl = "接收托盘zpl"

weighcode = "weigh"
weighname = "lfjds"
weighdesc = "称量描述"
weighzpl = "称量zpl"

wpalletcode = "weighpallet"
wpalletname = "lkfjdsl"
wpalletdesc = "称量托盘描述"
wpalletzpl = "称量托盘zpl"

devicecode = "fsdfkldsj"
devicename = "设备"
devicedesc = "设备描述"
devicezpl = "设备zpl"

editname = "_编辑名称"
editdesc = "_编辑描述"
editzpl = "_编辑zpl"
# ---------------------------------------------------------------------------------------------------------
# -------------------------------------------标签-异常测试数据------------------------------------------------
code1 = "code01"
name1 = "name01"
desc1 = "desc01"
zpl1 = "zpl01"
code2 = "code02"
name2 = "name02"
desc2 = "desc02"
zpl2 = "zpl02"

# 编码异常
code_ab1 = ''  # 为空
code_ab2 = '#'  # 有特殊字符
code_ab3 = code1 # 重复
code_abnormal_01 = [(code_ab1,name2,desc2,zpl2)]
code_abnormal_02 = [(code_ab2,name2,desc2,zpl2)]
code_abnormal_03 = [(code_ab3,name2,desc2,zpl2)]


# 名称异常
name_ab1 = ''  # 为空
name_ab2 = name1
name_abnormal_01 = [(code2,name_ab1,desc2,zpl2)]
name_abnormal_02 = [(code2,name_ab2,desc2,zpl2)]
# ZPL 异常
zpl_ab1 = ''  # 为空
zpl_abnormal = [(code2,name2,desc2,zpl_ab1)]
# ---------------------------------------------------------------------------------------------------------
