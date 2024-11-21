"""
URL configuration for conpig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
# from django.shortcuts import render

movie_list = [
    {'title':'파묘', 'director':'장재현'},
    {'title':'웡카', 'director':'폴 킹'},
    {'title': '듄: 파트2', 'director':'드니 빌뇌브'},
    {'title': '시민덕희', 'director':'박영주'},
]

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')

def book_list(request):
    book_text = ''

    for i in range(0, 10):
        book_text += f'book {i}<br>'

    return HttpResponse(book_text)

def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.')

def movies(request):
    movie_titles = [movie['title'] for movie in movie_list]

    response_text = ''

    for index, title in enumerate(movie_titles):
        response_text += f'<a href="/movie/{index}">{title}</a><br>'
    return HttpResponse(response_text)
    # return render(request, template_name= "movies.html", context={'movie_list': movie_list})

def movie_detail(request, index):
    if index > len(movie_list) -1:
        raise Http404
    movie = movie_list[index]

    response_text = f'<h1>{movie["title"]}</h1> <p>감독: {movie["director"]}</p>'
    return HttpResponse(response_text)
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', language),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
]
