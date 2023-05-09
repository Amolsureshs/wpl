from django.forms import ModelForm
from .models import Ques

class QuestionForm(ModelForm):
    class Meta:
        model=Ques
        fields='__all__'