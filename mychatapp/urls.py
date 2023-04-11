from django.urls import path 
from .views import index, detail


urlpatterns = [
    path('', index, name="index"),
    path('friends/<str:pk>/', detail, name="detail"),
]
