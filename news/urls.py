from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start, name="news_start"),
    path('/<int:pk>', views.NewsDetailView.as_view(), name="news-detail")
]