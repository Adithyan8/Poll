from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
    FormView
)
from .models import (
    Question,
    OptionVote
    )
from .forms import QuestionForm

class Qlist(ListView):
    model = Question
    template_name = "queans/qlist.html"
    context_object_name = "que"

class Qdetail(DetailView):
    model = Question
    template_name = "queans/qdetail.html"

    """ def get_queryset(self):
        return OptionVote.objects.filter(pollq=Question.objects.filter) """
    """ def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        #context['optvot']=OptionVote.objects.first()
        return context """

class Qcreate(CreateView):
    context_object_name="form"
    #form_class=QuestionForm
    model=Question
    fields=['pollq']
    template_name="queans/qform.html"
 

class Qupdate(UpdateView):
    model=Question
    context_object_name="form"
    template_name="queans/qupdate.html"
    fields=['pollq']

class Qdelete(DeleteView):
    model=Question
    context_object_name="form"
    template_name="queans/qdelete.html"
    success_url='/'