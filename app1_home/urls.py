from django.contrib import admin
from django.urls import path, re_path
from app1_home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.welcome,name = 'welcome'),
]
