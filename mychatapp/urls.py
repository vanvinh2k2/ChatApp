from django.urls import path 
from .views import index, detail, sent_chat


urlpatterns = [
    path('', index, name="index"),
    path('friends/<str:pk>/', detail, name="detail"),
    path('send_msg/<str:pk>/', sent_chat, name="send_msg"),
]
