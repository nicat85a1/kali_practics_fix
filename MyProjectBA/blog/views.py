from django.shortcuts import render,HttpResponse

# Create your views here.

def home_view(request):
    return render(request, "index.html",)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def blog(request):
    if request.user.is_authenticated:
        context = {

            'isim':'Nicat',
            'soyisim':'Kasumov'

        }
    else:
        context = {

            'isim':'Misafir',
            'soyisim':'cocuk'

        }
    #return render(request, 'home.html',{'isim':'Nicat'})
    return render(request, 'home.html',context)

def contact(request):
    return render(request, 'contact.html')