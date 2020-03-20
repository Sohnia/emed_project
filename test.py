# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 9:37
# @Author  : Yyf
# @FileName: test.py
# @Software: PyCharm
import nltk
from pubmed.pubmed_extract import get_pubmed_info
from question_answer.conclution import Qurey_answer

def get_info(id) -> list:
    pre_data = get_pubmed_info(id)
    if type(pre_data[2]) == str:
        abr_content = pre_data[2]
        abr_content_list = nltk.sent_tokenize(abr_content)
        q_r = Qurey_answer(abr_content)
        patience_design = q_r.search_patient()
        result_conclusion = abr_content_list[-1]+abr_content_list[-2]
    else:
        dict = pre_data[2]
        con_list = []
        for i in dict.items():
            con_list.append(i[1])
        patience_design = con_list[0]+con_list[1]
        result_conclusion = con_list[-1]+con_list[-2]
    res_list = [pre_data[0],pre_data[1],patience_design,result_conclusion]
    return res_list

res_list = get_info('31384410')
print(res_list)