from django.urls import path

from . import views

app_name = 'tinyapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', views.messages, name='messages'),
    path('messages/new/', views.new_message, name='new_message'),
    path('about/', views.about, name='about'),
]
