from django.shortcuts import render, redirect
from django.template import loader
from django.http import request, HttpResponse
from .models import Student  
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .forms import InputForm , StudentForm 

# Create your views here.

def index(request):
    return render(request, 'show.html')



def list_view(request):
# dictionary for initial data with
# field names as keys
    context ={}
# add the dictionary during initialization
    context["dataset"] = Student.objects.all()

    return render(request, "list_view.html", context)


class StudentCreate(CreateView):
# specify the model for create view
    model = Student
# specify the fields to be displayed
    fields = ['f_name', 'I_name']

# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)


def home_view2(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        # save the form data to model
        return redirect('list_view') # redirect to /list page

    context ={}
    context['StudentForm'] = form # pass the form to the context
    return render(request,"home2.html",context)

