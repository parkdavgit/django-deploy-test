from django.shortcuts import get_object_or_404, render, redirect ## 추가된 부분
from .models import Question ## 추가된 부분
from django.utils import timezone
from .forms import NewQuestionForm, AnswerForm 
from django.core.paginator import Paginator 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request): 
    question_list = Question.objects.order_by('-create_at') 
    # 입력 파라미터
    page = request.GET.get('page','1')
     
    # 페이징처리
    paginator = Paginator(question_list, 7)
    page_obj = paginator.get_page(page)
    return render(request, 'index.html',{'question_list':page_obj})

def question_create(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_at = timezone.now()

            question.author = request.user         ### 추가 ####

            question.save()
            return redirect('index')
    else:
        form = NewQuestionForm()
    return render(request, 'question_create.html', {'form':form})