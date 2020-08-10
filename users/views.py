from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import Creator
from .forms import UserRegistrationForm

""" class Register(CreateView):
    model = Creator
    template_name="users/register.html"
    context_object_name="form" """

def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserRegistrationForm()
    
    context={
        'form':form
    }

    return render(request,'users/register.html',context)

