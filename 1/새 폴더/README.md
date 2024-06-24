# 이번 pjt 후기
데이터분석에 관심이 있어서 나름 재미있었습니다~
어려운 부분은 라이브 강의에서 다 해결해주셔서 어렵지 않았습니다

그 외에 크롬창을 백그라운드에서만 열게하는 코드를 추가할수 있다는 걸 알았습니다
```python

def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 크롬 창을 숨기는 옵션 추가

    # 크롬 드라이버 생성 시 옵션 적용
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
```

## Problem A 
1. 막힌 부분
    - 없습니다

2. 시사점
    - 장고 온실에서 많이 반복했던 부분입니다

## Problem B
1. 막힌 부분
    - 모델폼이 아닌 모델로 구현해보려 했는데 어딘가 이상해서 그냥 모델폼으로 구현했습니다ㅠ
2. 시사점
    - 모델폼을 쓴다면 위젯을 더 능숙하게 쓸수 있으면 좋았을것 같습니다

## Problem C 
1. 막힌 부분
    - 크롤링에서 받아온 결과에서 숫자만 꺼내는데 시간이 약간 걸렸습니다. 파이썬 문법으로 해결은 가능했습니다
    
2. 시사점
    - 코드를 더 깔끔하게 짤수는 없었을까 싶어서 아쉽습니다

## Problem E
1. 막힌 부분
    - x

2. 시사점
    - 앞부분과 내용이 동일해서 어렵지 않았습니다. 마찬가지로 코드를 더 깔끔하게 짤 수 있다면 좋을 것 같습니다.
