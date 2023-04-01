# 0. 작업환경 만들기
#먼저 NaverFinance 터미널로 새로 들어간다.
#python -m venv myenv
#.\myenv\Scripts\activate
#pip install pandas, selenium, lxml
#pip list
#python
#exit() # python 빠져나오기

# 이 코드에서 건드릴것 : sosok 과 f_name

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.maximize_window() # 창 최대화 

# 1. 페이지 이동
# sosok=0 :코스피 / sosok=1 :코스닥
url='https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page='
browser.get(url)

# 2. 조회 항목 초기화(체크되어있는 항목 해제)
checkboxes=browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): # 체크된 상태라면?
        checkbox.click() #클릭(체크해제)

# 3. 조회 항목 설정(원하는 항목)
items_to_select=['시가','매출액증가율','영업이익증가율','PER','ROE','PBR']
for checkbox in checkboxes:
    parent=checkbox.find_element(By.XPATH,'..')
    label=parent.find_element(By.TAG_NAME, 'label')
    # print(label.text) # 이름 확인
    if label.text in items_to_select: #선택항목
        checkbox.click() #체크

# 4. 적용하기 버튼 클릭
btn_apply=browser.find_element(By.XPATH,'//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 50): # 1 이상 50 미만 페이지 반복
    # 사전 작업 : 페이지 이동
    browser.get(url+str(idx)) # page넘어감

    # 5. 데이터 추출
    df=pd.read_html(browser.page_source)[1] #df.head(10)으로 10줄만 확인가능
    df.dropna(axis='index',how='all',inplace=True)
    df.dropna(axis='columns',how='all',inplace=True)
    if len(df)==0: # 더이상 가져올 데이터가 없다면 탈출!
        break

    # 6. 파일 저장
    # 1페이지에만 header를 넣고 2페이지부터는 삭제
    f_name='cosdak.csv'
    if os.path.exists(f_name): # 파일이 있다면? 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else: # 파일이 없다면? 헤더 포함
        df.to_csv(f_name, encoding='utf-8-sig', index=False)

    print(f'{idx} 페이지 완료')

browser.quit() # 크롬 브라우저 종료