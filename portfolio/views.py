from django.shortcuts import render
from .models import Slider
# Create your views here.
def index(request):
    pics=Slider.objects.all()
    return  render(request,'index.html',{'pics':pics})