from django.urls import path
from . import views

urlpatterns=[
    path('anime/', views.anime, name='Anime'),
    path('login/', views.user_login, name='User_login'),
    path('signin/',views.user_sigin,name='User_sigin')
]