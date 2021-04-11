"""cap1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path

from ab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.전체),
    path('전체.html/', views.전체),
    path('정치.html/', views.정치),
    path('사회.html/', views.사회),
    path('경제.html/', views.경제),
    path('생활문화.html/', views.생활문화),
    path('세계.html/', views.세계),
    path('IT과학.html/', views.IT과학),
    

]
