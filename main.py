# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:01:10 2019

@author: tjlee
"""

#input으로 검색 키워드를 받아, 블로그 내용을 크롤링 하고 DF로 정리, CSV를 만드는 프로그램
#main.py : input 검색 키워드 받는 모듈, 크롤링, DF정리, CSV 관련 함수로 매개값 전달하는 모듈
#crawling.py : 크롤링, DF정리 하는 모듈
#save_csv.py : 세이브를 하는 모듈, exe 파일이 존재하는 해당 폴더에 csv를 만들 것

from crawling import crawling
from save_csv import save_csv

#키워드 받기 input
kw=input("키워드를 입력하세요 : ")
#crawling.py로 키워드 전달, DF 리턴 받을 것
df=crawling(kw)
print(df)
#save_csv.py로 DF,kw 전달, 리턴 값 없음, 거기서 세이브 하고 프로그램 종료
while True:
    try:
        num=int(input("저장하시겠습니까?(1-저장, 2-종료) : "))
        print(num)
    
        if not num in [1,2]:
            print("잘못된 명령입니다. 다시 입력해주세요.")
            continue
        
        elif num == 1 :
            save_csv(df,kw)
            break    
        else:
            print("프로그램을 종료합니다.")
            break
        
    except ValueError:
        print("잘못된 명령입니다. 다시 입력해주세요.")
        continue
            
        