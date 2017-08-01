from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    context_dict={'boldmessage':'I am bold font from the context' }
    return render(request,'farm/index.html',context_dict)

def about(request):
    return render(request,'farm/about.html')