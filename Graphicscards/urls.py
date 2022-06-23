import django
django.setup()
from django.urls import include, re_path, path
from . import views



urlpatterns = [
    re_path('', views.start),
    re_path('find_graphics_cards', views.find_graphics_cards, name="find_graphics_cards"),
]