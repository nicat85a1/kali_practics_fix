from django.contrib import admin
from django.urls import path
from post.views import *

app_name = 'post'

urlpatterns = [
    path('',post_index,name="index"),
    path('<int:id>/', post_detail,name="detail"),
    path('create/',post_create,name="create"),
    path('<int:id>/update/',post_update,name="update"),
    path('<int:id>/delete',post_delete,name="delete"),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)