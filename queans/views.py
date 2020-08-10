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
from .models import Question
from django.contrib.auth.mixins import LoginRequiredMixin

class Qlist(ListView):
    model = Question
    template_name = "queans/qlist.html"
    context_object_name = "que"
    ordering = ["-date_posted"]

class Qdetail(DetailView):
    model = Question
    template_name = "queans/qdetail.html"

    """ def get_queryset(self):
        return OptionVote.objects.filter(pollq=Question.objects.filter) """
    """ def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        #context['optvot']=OptionVote.objects.first()
        return context """

class Qcreate(LoginRequiredMixin,CreateView):
    context_object_name="form"
    model=Question
    fields=['pollq','option1','option2','option3',]
    template_name="queans/qform.html"

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class Qupdate(LoginRequiredMixin,UpdateView):
    model=Question
    context_object_name="form"
    template_name="queans/qupdate.html"
    fields=['pollq','option1','option2','option3',]

class Qdelete(LoginRequiredMixin,DeleteView):
    model=Question
    context_object_name="form"
    template_name="queans/qdelete.html"
    success_url='/'

def Qvote(request,id):
    poll = Question.objects.get(id=id)
    if request.method=='POST' :
        selected_option = request.POST['option']
        if "option1" == selected_option :
            poll.option1 += 1
        elif "option2" == selected_option :
            poll.option2 +=1
        elif "option3" == selected_option :
            poll.option3 +=1
    
    return render(request,'queans/qvote.html',{'poll':poll})
