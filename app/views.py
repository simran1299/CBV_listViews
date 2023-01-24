from django.shortcuts import render

# Create your views here.
from django.views.generic import View,ListView
from app.models import *

class home(View):
    def get(self,request):
        return render (request,'app/home.html')

class school_list(ListView):
    model=School
    context_object_name='schools'