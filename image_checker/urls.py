from django.urls import path
from . import views

urlpatterns = [
    path('analyze_image/', views.ImageAnalyzerAPI.as_view(), name='analyze_image'),
]