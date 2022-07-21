#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Poll

from django.contrib import messages


def index(request):
    return render(request,'index.html')

@login_required(login_url='/account/login')
def user_list(request):
     
    
    polls = Poll.objects.order_by('pub_date') 
    # 입력 파라미터
    page = request.GET.get('page','1')
     
    # 페이징처리
    paginator = Paginator(polls, 4)
    polls = paginator.get_page(page)
    return render(request, 'user_list.html',{'polls':polls})     