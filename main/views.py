#from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect ## 추가된 부분

def home(request): 
   
    return render(request, 'home.html')