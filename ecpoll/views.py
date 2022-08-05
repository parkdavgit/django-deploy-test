from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Poll, Choice, Vote

from .forms import PollAddForm,EditPollForm,ChoiceAddForm
from django.contrib import messages
 

def index(request): 
    return render(request, 'index.html')


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
def user_search(request):

    user_name = request.POST.get('user_name', '').strip()
    
    polls = Poll.objects.filter(text=user_name)
     
    page = request.GET.get('page','1')
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



def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if not poll.active:
        return render(request, 'poll_result.html', {'poll': poll})
    loop_count = poll.choice_set.count()
    context = {
        'poll': poll,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'poll_detail.html', context)



@login_required
def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    choice_id = request.POST.get('choice')
    if not poll.user_can_vote(request.user):
        messages.error(
            request, "You already voted this poll!", extra_tags='alert alert-warning alert-dismissible fade show')
        return redirect("user_list")

    if choice_id:
        choice = Choice.objects.get(id=choice_id)
        vote = Vote(user=request.user, poll=poll, choice=choice)
        vote.save()
        print(vote)
        return render(request, 'poll_result.html', {'poll': poll})
    else:
        messages.error(
            request, "No choice selected!", extra_tags='alert alert-warning alert-dismissible fade show')
        return redirect("detail", poll_id)
    return render(request, 'poll_result.html', {'poll': poll})     

@login_required
def endpoll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.user != poll.owner:
        return redirect('home')

    if poll.active is True:
        poll.active = False
        poll.save()
        return render(request, 'poll_result.html', {'poll': poll})
    else:
        return render(request, 'poll_result.html', {'poll': poll})  


@login_required
def polls_edit(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.user != poll.owner:
        return redirect('index')

    if request.method == 'POST':
        form = EditPollForm(request.POST, instance=poll)
        if form.is_valid:
            form.save()
            messages.success(request, "Poll Updated successfully.",
                             extra_tags='alert alert-success alert-dismissible fade show')
            return redirect("user_list")

    else:
        form = EditPollForm(instance=poll)

    return render(request, "poll_edit.html", {'form': form, 'poll': poll})         
