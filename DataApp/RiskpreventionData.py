# coding=utf-8

"""
Created on 2020/10/15
@author: lianxiujuan
@desc：危险防范数据
"""
# ----------------------------------------正常场景--------------------------------------
addcodedata = "aaaa"
addcode = 'code1'
addcdescdata = "aaaa"
addedescdata = "aaaa"
editcdescdata = "bbbb"
editedescdata = "bbbb"
# -------------------------------------------------------------------------------------

# --------------------------------------编码异常场景----------------------------------------
code1 = " "  # 编码为空
code2 = "3222222222222222222222222222222"  # 编码超多30字符，如31字符
code3 = "code&1"  # 编码含有特殊字符
code4 = "_1234"  # 特殊字符开头
code5 = addcodedata  # 编码重复
code_abnormal_list = [(code1, addcdescdata, addedescdata),
                      (code2, addcdescdata, addedescdata),
                      (code3, addcdescdata, addedescdata),
                      (code4, addcdescdata, addedescdata),
                      (code5, addcdescdata, addedescdata)
                      ]
# --------------------------------------------------------------------------------------

# --------------------------------------中文描述异常场景----------------------------------------
cdesc1 = " "  # 中文描述为空
cdesc2 = "中文描述最大字符测试401，'请按照格式要求填写数据'，'请按照格式要求填写数据''请按照格式要求填写数据'，'请按照格式要求填写数据'、中文描述最大字符测试401" \
         "，'请按照格式要求填写数据'，'请按照格式要求填写数据''请按照格式要求填写数据'，'请按照格式要求填写数据'、中文描述最大字符测试401" \
         "，'请按照格式要求填写数据'，'请按照格式要求填写数据''请按照格式要求填写数据'，'请按照格式要求填写数据'、中文描述最大字符测试401" \
         "，'请按照格式要求填写数据'，'请按照格式要求填写数据''请按照格式要求填写数据'，'请按照格式要求填写数据'、中文描述最大字符测试401" \
         "，'请按照格式要求填写数据'，'请按照格式要求填写数据''请按照格式要求填写数据'，'请按照格式要求填写数据'、中文描述最大字符测试401，'请按照格式要求填写数据'，'请按照格式要求填写数据''123" \
         "三等奖地方，大富大贵1"  # 中文描述超多400字符，如401字符

cdesc_add_abnormal_list = [(addcode, cdesc1, addedescdata),
                           (addcode, cdesc2, addedescdata)
                           ]
cdesc_edit_abnormal_list = [(cdesc1, addedescdata),
                            (cdesc2, addedescdata)
                            ]
# ---------------------------------------------------------------------------------------

# --------------------------------------英文描述异常场景----------------------------------------
edesc1 = " "  # 英文描述为空
edesc2 = "danger，mde3222222222222222222222222222222,dfdjhdanger，mde3222222222222222222222222222222," \
         "dfdjhdanger，mde3222222222222222222222222222222,dfdjhdanger，mde3222222222222222222222222222222," \
         "dfdjhdanger，mde3222222222222222222222222222222,dfdjhdanger，mde3222222222222222222222222222222," \
         "dfdjhdanger，mde3222222222222222222222222222222,dfdjhdanger，mde3222222222222222222222222222222," \
         "dfdjhdanger，mde3222222222222222222"  # 英文描述超多400字符，如401字符

edesc_add_abnormal_list = [(addcode, addcdescdata, edesc1),
                           (addcode, addcdescdata, edesc2)
                           ]

edesc_edit_abnormal_list = [(addcdescdata, edesc1),
                            (addcdescdata, edesc2)
                            ]
# --------------------------------------------------------------------------------------
