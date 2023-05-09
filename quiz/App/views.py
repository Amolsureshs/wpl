from django.shortcuts import render,redirect
from .forms import QuestionForm
from .models import Ques
# Create your views here.
def home(request):
    question=Ques.objects.all()
    print(request)
    score=0
    correct=0
    counter=0
    timer=0
    total=0
    if(request.method=='POST'):
        for q in question:
            print(request.POST.get(q.Question)," and Answer is ",q.ans)
            if(request.POST.get(q.Question)==q.ans):    
                correct=correct+1
                score+=10
            counter=counter+1
        total=score/(counter*10)*100

        context={
            "score":score,
            "timer":request.POST.get('timer'),
            "total":total,
            "correct":correct
        }
        return render(request,'score.html',context)

    context={'question':question}
    return render(request,'index.html',context)
def addQuestion(request):
    form=QuestionForm()
    if(request.method=='POST'):
        form=QuestionForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("home")
        else:
            print(form)
            return redirect('Add')
    context={'form':form}
    return render(request,'addQuestion.html',context)