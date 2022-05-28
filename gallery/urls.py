from django.urls import re_path as url,include
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
]