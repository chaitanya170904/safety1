from django.urls import path
from . import views

urlpatterns = [
    path('check_tweet/', views.check_tweet, name='check_tweet'),

]