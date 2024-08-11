from django.shortcuts import render
import time
import random
from bs4 import BeautifulSoup
import requests
from . models import Urls
# Create your views here.
# def url_list_view(request):
#     url_list = ['https://healthyhubhabits.blogspot.com/', 'https://healthyhubhabits.blogspot.com/2023/07/health-by-habits-2023.html']
#     stay_duration = random.randint(10,20)  # Duration to stay on each URL page in seconds

#     for url in url_list:
#         context = {'url': url, 'stay_duration': stay_duration}
#         time.sleep(stay_duration)
#         return render(request, 'calling_url/show_all.html', context)
    
# def add_blog(request):
#     template_name = '#'
#     context = {}
#     if request.method == 'POST':
#         url_key = request.Post.get(key)

def url_list_view(request):
    url_list = "https://healthyhubhabits.blogspot.com/"
    response = requests.get(url_list)
    soup = BeautifulSoup(response.content, 'html.parser')
    breakpoint()
    # Find all anchor tags with class "label-name" and extract the href attribute [ALL URLS FROM BLOGS CATEGORY]
    url_list = [a['href'] for a in soup.find_all('a', class_='label-name')]
    print('*************************',url_list,'************************')
    
    # for i in url_list:
    #     response = requests.get(i)
    #     html_content = response.content
    #     soup = BeautifulSoup(html_content, 'html.parser')
    #     a_tags = soup.find_all('a')
    #     # Extract the URLs from the 'href' attribute of each 'a' tag
    #     url_list2 = [a['href'] for a in a_tags]
    # print('+++++++++++++++++',url_list2,'+++++++++++++++++++++++++++++')

    # url_list = ['https://healthyhubhabits.blogspot.com/', 'https://healthyhubhabits.blogspot.com/2023/07/health-by-habits-2023.html']
    stay_duration = random.randint(10,20)  # Duration to stay on each URL page in seconds
    scroll_duration = random.randint(1000,5000)  # Duration in milliseconds for the scrolling animation
    context = {'url_list': url_list, 'stay_duration': stay_duration, 'scroll_durtion': scroll_duration}
    return render(request, 'calling_url/show_all.html', context)
