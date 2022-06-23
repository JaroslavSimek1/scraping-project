from django.contrib import admin
from django.urls import re_path, include, path
from Graphicscards import views

urlpatterns = [
    re_path('admin', admin.site.urls),
    re_path('find_graphics_cards', views.find_graphics_cards),
    re_path('from_expensive', views.from_expensive),
    re_path('from_cheap', views.from_cheap),
    re_path('', views.start),
]
