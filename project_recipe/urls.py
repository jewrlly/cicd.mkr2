from django.contrib import admin
from django.urls import path

from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]