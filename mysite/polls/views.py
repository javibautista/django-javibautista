from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.shortcuts import render

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def corregir(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	opciones = question.choice_set.all()
	elegidas= question.choice_set.filter(pk__in=request.POST.getlist('choice'))
	c={} 
	for opcion in opciones:   
		if opcion.correcto :
			c[opcion]= opcion in elegidas
		else:
			c[opcion] = opcion not in elegidas
	return render(request,'polls/results.html',{'question': question, 'c': c})

