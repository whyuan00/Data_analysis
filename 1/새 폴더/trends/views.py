from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm
import matplotlib.pyplot as plt
# Create your views here.

from bs4 import BeautifulSoup
from selenium import webdriver

def keyword(request):
    keywords = Keyword.objects.all()
    if request.method =='POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            #redirect는 appname
            return redirect('trends:keyword')
    # get 일때 렌더링
    else:
        form = KeywordForm()
    context = {
            'form':form,
            'keywords':keywords,
    }
    return render(request,'trends/keyword.html',context)
    # post 일때 저장 



def keyword_detail(request,pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


def get_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬브라우저 열어서 동적인 내용 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스 받아오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select_one('#result-stats')
    # print(result)
    return result.text
    '''
    results = []
    #게시물의 공통점 : div 태그 +  g클래스
    g_list = soup.select('div.g')
    for g in g_list:
        # 요소 안에서 특정 클래스 가진 요소 선택
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")
        if title:
            # print('제목=',title.text)
            results.append(title.text)
    return results
    '''


def crawling(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        # print(keyword.keyword)
        result = get_data(keyword.keyword)
        result_stat = []
        for i in list(result):
            if i.isdigit():
                result_stat.append(i)
            elif i == '(':
                break 
        if len(result_stat)>0:
            resultStat = int(''.join(result_stat))
    #        # 기존에 존재하는 키워드인 경우
            existing_trend = Trend.objects.filter(name=keyword.keyword).first()
            if existing_trend:
                existing_trend.result = resultStat
                existing_trend.save()
            else:
                trend = Trend.objects.create(name=keyword.keyword, result=resultStat, search_period='all') 

        # # 트랜드로 저장
        # if keyword.keyword not in trends:
        #     trend, created_trend = Trend.objects.get_or_create(name=keyword.keyword, result = resultStat, search_period = 'all') 
    trends = Trend.objects.all()
    context = {
        'trends':trends,
    }
    return render(request, 'trends/crawling.html',context)

    # titles = get_data(keyword)
    # for title in titles:
        #1. article 저장
        # article, created_article = Article.objects.get_or_create(title=title)
        #2. 키워드 저장
        # 단 이미 저장된거면 pass 
        # query_obj, created_query = Query.objects.get_or_create(article=article, keyword=keyword)

from io import BytesIO
import base64

def crawling_histogram(request):
    plt.figure(figsize=(12, 8))
    plt.clf()  # 이전 그래프 지우기
    data = {}
    trends = Trend.objects.all()
    for trend in trends:
        data[trend.name]=trend.result
    plt.bar(data.keys(), data.values(),color='blue',edgecolor='black')
    plt.grid()
    plt.title('Technology Trend Analysis')
    plt.xlabel('Result')
    plt.ylabel('Keywords')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()

    context = {
            'image': f'data:image/png;base64,{img_base64}',
        }

    return render(request,'trends/histogram.html',context)




def get_yeardata(keyword):
    url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'
    
    # 크롬브라우저 열어서 동적인 내용 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스 받아오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select_one('#result-stats')
    # print(result)
    return result.text

def crawling_advanced(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        # print(keyword.keyword)
        result = get_yeardata(keyword.keyword)
        result_stat = []
        for i in list(result):
            if i.isdigit():
                result_stat.append(i)
            elif i == '(':
                break 
        if len(result_stat)>0:
            resultStat = int(''.join(result_stat))
    #        # 기존에 존재하는 키워드인 경우
            existing_trend = Trend.objects.filter(name=keyword.keyword, search_period='year').first()
            if existing_trend:
                existing_trend.result = resultStat
                existing_trend.save()
            else:
                trend = Trend.objects.create(name=keyword.keyword, result=resultStat, search_period='year') 
    
    
    plt.figure(figsize=(12, 8))
    plt.clf()  # 이전 그래프 지우기
    data = {}
    trends = Trend.objects.filter(search_period='year')
    for trend in trends:
        data[trend.name]=trend.result
    plt.bar(data.keys(), data.values(),color='blue',edgecolor='black')
    plt.grid()
    plt.title('Technology Trend Analysis')
    plt.xlabel('Result')
    plt.ylabel('Keywords')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()

    context = {
            'image': f'data:image/png;base64,{img_base64}',
        }

    return render(request,'trends/histogram.html',context)