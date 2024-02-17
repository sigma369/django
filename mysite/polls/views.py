# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

def index(request):
    question_qury_set = Question.objects.order_by('pub_date')[0:5]
    #question_list = [q.question_text for q in question_object]
    
    context = {'latest_question_list': question_qury_set}

    return  render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question,
               'choices': Choice.objects.filter(question=question)
               }
    return render(request, 'polls/detail.html', context)
    # try:
    #     #question = Question.objects.filter(id=question_id).first()
    #     question = Question.objects.get(id=question_id)
        
    # except:
    #     raise Http404('Question does not exist')
    # else:
    #     context = {"question": question}
    #     return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = f'you are looking at the results of question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f'you are voting on question {question_id}')



