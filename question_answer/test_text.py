# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 9:46
# @Author  : Yyf
# @FileName: test_text.py
# @Software: PyCharm
import re
from pdf_to_txt import get_content
from question_answer.conclution import Qurey_answer
import chardet
text = get_content("../stactic/28744823.pdf")
q_a = Qurey_answer(text)

t_q_a=q_a.search_num()
new = q_a.rectify_code(t_q_a)
print(new)
# res = []
# for i in t_q_a:
#     if re.match('[\w]',i):
#         res.append(i)
#     else:
#         res.append(' ')
# print(''.join(res))
