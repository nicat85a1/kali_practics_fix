from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from django.http import FileResponse
import os
from django.conf import settings
# Create your views here.

def index(request):
    return render(request,"index.html",)