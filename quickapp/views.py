from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def Gallery(request):
    return render(request,'Gallery.html')
