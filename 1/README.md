# 웹 크롤링

구글 검색 결과 크롤링 과정에서 주의할점

1. id가 새로고침시마다 변하므로,
    *class와 태그* 기준으로 정보 추출해야함

2. 검색결과 페이지들의 제목은 공통적으로
    결과를 감싸는 div 에는 “g” 클래스
    제목에는 “LC20lb MBeuO DKV0Md” 클래스\

3.크롬창을 백그라운드에서만 열게하는 코드

```python
def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 크롬 창을 숨기는 옵션 추가

    # 크롬 드라이버 생성 시 옵션 적용
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
