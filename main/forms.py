from django import forms
from .models import Question, Answer 


class NewQuestionForm(forms.ModelForm):
## 해당 부분에 form에서 입력 받을 속성을 결정합니다. models.py와 동일하게 설정하면 됩니다. ##
    subject = forms.CharField(
        max_length=200,
        label='제목')
    content = forms.CharField(
        widget=forms.Textarea(),
        label='내용'
    )

## 어떤 모델을 사용하고 모델에서 사용할 속성을 지정 합니다 ##
    class Meta:
        model = Question
        fields = ['subject', 'content']

class AnswerForm(forms.ModelForm):
    content = forms.Textarea()

    class Meta:
        model = Answer
        fields = ['content',]
