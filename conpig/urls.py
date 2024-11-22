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
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render
from bookmark import views

# movie_list = [
#     {'title':'파묘', 'director':'장재현'},
#     {'title':'웡카', 'director':'폴 킹'},
#     {'title': '듄: 파트2', 'director':'드니 빌뇌브'},
#     {'title': '시민덕희', 'director':'박영주'},
# ]
#
# def index(request):
#     return HttpResponse('<h1>Hello World!</h1>')
#
# def book_list(request):
#     book_text = ''
#
#     return render(request, template_name='book_list.html')
#
# def book(request, num):
#     return render(request, template_name='book_detail.html', context={'num':num})
#
# def language(request, lang):
#     return HttpResponse(f'<h1>{lang} 언어 페이지입니다.')
#
# def movies(request):
#     # movie_titles = [movie['title'] for movie in movie_list]
#     #
#     # response_text = ''
#     #
#     # for index, title in enumerate(movie_titles):
#     #     response_text += f'<a href="/movie/{index}">{title}</a><br>'
#     # return HttpResponse(response_text)
#     return render(request, template_name= "movies.html", context={'movie_list': movie_list})
#
# def movie_detail(request, index):
#     if index > len(movie_list) -1:
#         raise Http404
#
#     movie = movie_list[index]
#
#     response_text = {'movie': movie}
#     return render(request, template_name='movie.html', context=response_text)
urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', index),
    # path('book_list/', book_list),
    # path('book_list/<int:num>/', book),
    # path('language/<str:lang>/', language),
    # path('movie/', movies),
    # path('movie/<int:index>/', movie_detail),
    path('bookmark/', views.bookmark_list),
    path('bookmark/<int:num>/', views.bookmark_detail),
]
