from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def blog(request):
    data = "hello word"
    data2 = "hello word2"

    context = {

        'data':data,
        'data2':data2,

    }
    return render(request, 'blog.html',context)

def contact(request):
    return render(request, 'contact.html')