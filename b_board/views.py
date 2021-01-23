from django.shortcuts import render
from django.views.generic import ListView
from .models import B_BoardModel

# Create your views here.

class B_BoardList(ListView):
    template_name = 'list.html'
    model = B_BoardModel