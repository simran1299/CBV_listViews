from django.shortcuts import render

# Create your views here.
from django.views.generic import View,ListView,DetailView,CreateView
from app.models import *

class home(View):
    def get(self,request):
        return render (request,'app/home.html')

class school_list(ListView):
    model=School
    context_object_name='schools'


class school_detail(DetailView):
    model=School
    context_object_name='school'

class student_detail(DetailView):
    model=Student
    context_object_name='student'


class school_create(CreateView):
    model=School
    fields='__all__'

class student_create(CreateView):
    model=Student
    fields='__all__'
