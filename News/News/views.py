from django.http import HttpResponse
from django.shortcuts import render, redirect
from disp_news.models import daily_news

def home(request):
    newsdata=daily_news.objects.all()
    data={
        'news_articles':newsdata
    }
    return render(request,'disp_news.html', data)

def single_disp(request, slug):
    single_news=daily_news.objects.get(news_slug=slug)
    data={
        'single_news':single_news
    }
    return render(request, "single_news.html", data)
