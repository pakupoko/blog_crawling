# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:42:14 2019

@author: tjlee
"""


import os
import datetime

def save_csv(df,kw):
    
    #경로 찾기, 세이브 파일 보관 폴더 만들기
    BASE_DIR = os.getcwd()
    SAVE_DB_DIR = os.path.join(BASE_DIR, "crawling_DB")
    
    if not os.path.exists(SAVE_DB_DIR):
        os.makedirs(SAVE_DB_DIR)
    
    #텍스트 파일 만들기
##   temp_name = f"post_crawling_{kw}_{str(datetime.date.today())}.csv"
    temp_name = f"post_crawling_{kw}_{str(datetime.date.today())}.xlsx"
    txt_name = os.path.join(SAVE_DB_DIR, temp_name)
    
##   df.to_csv(txt_name,mode="w", encoding="cp949")
    df.to_excel(txt_name, sheet_name='sheet1')
    
    print("저장 완료. 프로그램을 종료합니다.")
    
    