from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def Gallery(request):
    return render(request,'Gallery.html')

def about(request):
    return render(request,'about.html')

def form(request):
    return render(request,'form.html')

def product(request):
    return render(request,'products.html')

def service(request):
    return render(request,'services.html')