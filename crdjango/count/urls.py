from django.urls import path
from . import views

urlpatterns = [
    path('', views.count_w, name='count_w'),
    path('word', views.count_w, name='count_w'),
    path('character', views.count_c, name='count_c')
    ]