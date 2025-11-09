from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='home'),
    path('home/<int:id>', views.Anime, name='Anime'),
    path('test/',views.insert,name='Test')
]