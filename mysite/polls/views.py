# from django.shortcuts import render

# Create your views here.
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views.generic import ListView, DetailView

from .models import Question, Choice

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[0:5]


# def index(request):
#     question_qury_set = Question.objects.order_by('pub_date')[0:5]
#     #question_list = [q.question_text for q in question_object]
    
#     context = {'latest_question_list': question_qury_set}

#     return  render(request, 'polls/index.html', context)

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
         context = super().get_context_data(**kwargs)
         context['choices'] = Choice.objects.filter(question=context['question'])
         print(context)
         return context

# def detail(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     context = {'question': question,
#                'choices': Choice.objects.filter(question=question)
#                }
#     return render(request, 'polls/detail.html', context)
    
    
    # try:
    #     #question = Question.objects.filter(id=question_id).first()
    #     question = Question.objects.get(id=question_id)
        
    # except:
    #     raise Http404('Question does not exist')
    # else:
    #     context = {"question": question}
    #     return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question':question,
        'choices':Choice.objects.filter(question=question)
    }
    return render(request, 'polls/results.html', context)




def vote(request, question_id):
    print(request.POST)
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = Choice.objects.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'choices': Choice.objects.filter(question=question),
            'error_message': 'You didnot selected a choice!',

        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # selected_choice.votes += 1
        # selected_choice.save()
    
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,)))

def owner(request):
    return HttpResponse("Hello, world. 8abd9143 is the polls index.")



