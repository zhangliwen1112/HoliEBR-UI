# -*-coding:GBK -*-
# --------------------------------------------��������-----------------------------------------------------
# ������������
add_name = "formulaname001"
add_num = '1000'
r_unit = 'mg'
add_weight = "200"
w_unit = 'g'

# �༭����
edit_name = '�޸Ĵ���'
edit_num = '2000.123'
edit_weight = '500.55'
edit_r_unit = 'kg'
edit_w_unit = 'kg'

# �����������ϵ�λ
m_unit = 'kg'
# -----------------------------------------------------------------------------------------------------------

# ----------------------------------------�쳣����---���������쳣----------------------------------------------
name1 = "@123"  # �������ַ���ͷ
name2 = "F&a"   # ���������ַ�
name3 = "ASDchufang123_dfd45/dfdf����ASDchufang123_dfd45/dfdf����ASDchufang123_dfd45/dfdf����dfd45/dfdf����123fgfgf101"  # ����100�ַ���101�ַ�
name4 = " "     # ���ַ�
abnormal_name = [(name1, add_num, r_unit, add_weight, w_unit),
                 (name2, add_num, r_unit, add_weight, w_unit),
                 (name3, add_num, r_unit, add_weight, w_unit),
                 (name4, add_num, r_unit, add_weight, w_unit)
                 ]
# -----------------------------------------------------------------------------------------------------------

# ----------------------------------------�쳣����---�ο������쳣----------------------------------------------
num1 = "1.1234"  # С��λ������3λ
num2 = "a"  # ������
num3 = "10000000000"  # �������ֵ
abnormal_num = [(add_name, num1, r_unit, add_weight, w_unit),
                (add_name, num2, r_unit, add_weight, w_unit),
                (add_name, num3, r_unit, add_weight, w_unit)
                ]
# -----------------------------------------------------------------------------------------------------------

# ----------------------------------------�쳣����---�ȼ۳����쳣----------------------------------------------
weight1 = "1.1234"  # С��λ������3λ
weight2 = "a"  # ������
weight3 = "10000000000"  # �������ֵ
abnormal_weight = [(add_name, add_num, r_unit, weight1, w_unit),
                   (add_name, add_num, r_unit, weight2, w_unit),
                   (add_name, add_num, r_unit, weight3, w_unit)
                   ]
# -----------------------------------------------------------------------------------------------------------