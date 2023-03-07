from django.shortcuts import render
from .models import Content
# Create your views here.

def index(request):
    content = Content.objects.all()
    return render(request, 'index.html', {'content': content})

def detail(request, id):
    contentID = Content.objects.get(id=id)
    return render(request, 'detail.html', {'contentID': contentID})

def cv(request):
    return render(request, 'cv.html')