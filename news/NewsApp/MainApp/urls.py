from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<topic>/', views.news_by_topic, name='news_by_topic'),  # Capture topic
]
