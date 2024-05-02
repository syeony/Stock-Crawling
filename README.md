# Stock-Crawling
네이버 증권 시가총액페이지에서 cospi와 copdak 크롤링해서 엑셀파일로 정리한 것입니다.



# 1. 기존 myenv폴더와 chromedriver.exe파일 삭제 후
vscode 터미널에 아래코드 입력
```
python -m venv myenv
.\myenv\Scripts\activate
pip install pandas, selenium, lxml
pip list # 확인용
```
만약, .\myenv\Scripts\activate 부분에서
```
+ CategoryInfo : 보안 오류: (:) [], PSSecurityException
```
라는 오류가 뜨면 파워쉘을 관리자 권한으로 실행한 후 Set-ExecutionPolicy Unrestricted 를 입력 후 A를 누르고 다시 VSC 화면에서 진행 ...


# 2. chromedriver
url창에 chrome://version 쳐서 내 크롬버전 확인하고

구글에 chromedriver 검색해서 내 버전에 맞는버전 설치하기

만약 chromedriver에 내 버전이 없다면 

https://velog.io/@syiee/Chrome-Web-Driver-%EC%B5%9C%EC%8B%A0-%EB%B2%84%EC%A0%84-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-119

여기서 다운받아서 폴더에 넣어주기 (그냥 드래그해서 넣어주면 된다)

# 3. 실행
위에 실행버튼만 눌러주면 된다

정상적으로 작동한다면 아래와 같이 결과가 나옴
![image](https://github.com/syeony/Stock-Crawling/assets/101008357/08e0f373-72ff-440c-b266-9e958d9e670f)

# 4. 활용
다운받아진 csv파일을 바탕화면으로 드래그하여 다른이름저장으로 엑셀파일로 저장 후 사용
