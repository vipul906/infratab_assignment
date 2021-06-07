from django.urls import path
from ratemymovie import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
