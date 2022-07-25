#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Poll, Choice
from .forms import PollAddForm 
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

@login_required()
def polls_add(request):
    if request.user.has_perm('ecpoll.add_poll'):#super user appname and url
        if request.method == 'POST':
            form = PollAddForm(request.POST)
            if form.is_valid:
                poll = form.save(commit=False)
                poll.owner = request.user
                poll.save()
                new_choice1 = Choice(
                    poll=poll, choice_text=form.cleaned_data['choice1']).save()
                new_choice2 = Choice(
                    poll=poll, choice_text=form.cleaned_data['choice2']).save()

                messages.success(
                    request, "Poll & Choices added successfully.", extra_tags='alert alert-success alert-dismissible fade show')

                return redirect('user_list')
        else:
            form = PollAddForm()
        context = {
            'form': form,
        }
        return render(request, 'add_poll.html', context)
    else:
        return HttpResponse("Sorry but you don't have permission to do that!") 



