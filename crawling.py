# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:27:30 2019

@author: tjlee
"""


import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def crawling(kw):

    #변수 초기화 
    df_crawling=pd.DataFrame()
    for i in range(1,11):
        
        #Url 설정, 변수 초기화 
        NAVER_SEARCH_URL = "https://search.naver.com/search.naver"
        query=kw
        
        params = {
            "where" : "post",
            "query" : query,
            "start" : i*10+1
            }
        #url, 데이터 추출
        resp=requests.get(NAVER_SEARCH_URL, params=params)
        soup=BeautifulSoup(resp.content, 'html.parser')
        
        ul_contents=soup.find('ul', class_='type01')
        
        #데이터 전처리(공백 제거)
        new_ul=[]
        for content in ul_contents :
            if not str(content).strip():
                continue
            new_ul.append(content)
        
        #데이터 추출 
        temp_dict={}
        
        temp_list_link=[]
        temp_list_title=[]
        temp_list_content=[]
        temp_list_date=[]
        
        for li in new_ul:
            a_tag=li.find('dl').find('dt').find('a')
            content_tag=li.find('dl')
            
            temp_list_link.append(a_tag['href'])
            temp_list_title.append(a_tag.text)
            temp_list_content.append(content_tag.find('dd', class_='sh_blog_passage').text)
            temp_list_date.append(content_tag.find('dd').text.strip('. '))
        
        #임시 딕셔너리 내 각 키 값에 맞는 데이터 리스트 삽입 
        temp_dict['link']=temp_list_link
        temp_dict['title']=temp_list_title
        temp_dict['content']=temp_list_content
        temp_dict['date']=temp_list_date
        
        #데이터 프레임으로 전환, 누적
        if i==1 :
            df_crawling=pd.DataFrame(temp_dict) 
           
        else:
            df_crawling=df_crawling.append(pd.DataFrame(temp_dict), ignore_index=True)
            
    #데이터프레임 리턴 
    return df_crawling
    
    
#테스트 공간 : 프로그램 완성 시 여기 있는 코드는 모두 주석처리하거나 지울 것!
