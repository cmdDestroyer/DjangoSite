from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainPage.urls")),
    path('news', include("news.urls"))
]
