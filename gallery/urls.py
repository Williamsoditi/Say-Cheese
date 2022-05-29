from django.urls import re_path as url,include
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^pictures/',views.pictures,name ='pictures'),
    url(r'^search/', views.search_results, name='search_results'),
]