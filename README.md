# Stock-Crawling
네이버 증권 시가총액페이지에서 크롤링해서 엑셀파일로 정리

python -m venv myenv
.\myenv\Scripts\activate
들어가서 위에 실행버튼만 눌러주면 된다



<에러해결법>
 
아래와 같이 뜨면 chromedriver버전 문제일 가능성 높음
![image](https://github.com/syeony/Stock-Crawling/assets/101008357/57abae03-f54d-4eb0-984b-4cdda5b27e5a)

먼저 url창에 chrome://version 쳐서 내 크롬버전 확인하고
구글에 chromedriver 검색해서 내 버전에 맞는버전 설치하기
만약 chromedriver에 내 버전이 없다면 
https://velog.io/@syiee/Chrome-Web-Driver-%EC%B5%9C%EC%8B%A0-%EB%B2%84%EC%A0%84-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-119
여기서 다운받아서 넣어주기

정상적으로 작동한다면 아래와 같이 결과가 나옴
![image](https://github.com/syeony/Stock-Crawling/assets/101008357/08e0f373-72ff-440c-b266-9e958d9e670f)
