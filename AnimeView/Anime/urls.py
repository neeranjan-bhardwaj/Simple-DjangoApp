from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='Anime'),
    path('login/', views.user_login, name='User_login'),
    path('signin/',views.user_sigin,name='User_sigin'),
    path('anime',views.anime,name="anime"),
    path('test/',views.test,name="test")
]