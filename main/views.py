#from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect ## 추가된 부분
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

def index(request): 
    return render(request, 'index.html')
