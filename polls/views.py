from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:15]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_question = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message': "You didn't select a choice"})
    else:
        selected_question.votes += 1
        selected_question.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def createPage(request):

    return render(request=request, template_name='polls/create.html', context={})

@login_required
def create(request):

    if request.POST:
        name = request.POST.get('text_name')
        date = timezone.now()
        q = Question(question_text=name, pub_date=date)
        q.save()
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return HttpResponse('You failed.')

class CreateChoicePage(generic.ListView):
    model = Question
    template_name = 'polls/choices.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.all()



class deleteView(generic.DeleteView):

    template_name='polls/confirm_delete.html'
    model = Question
    success_url = '/polls/'


#def create_choice_page(request):
    #return render(request, template_name='polls/choice_form')
@login_required
def create_choice(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choices = question.choice_set.all()

    if request.POST:
        choice = request.POST.get('choice_name')
        question.choice_set.create(choice_text=choice, votes=0)
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, template_name='polls/choices_create.html', context={'choices': choices})

def newIndex(request):
    return render(request, template_name='dashboard/index.html')