from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import B_BoardModel
from django.urls import reverse_lazy

# Create your views here.


class B_BoardList(ListView):
    template_name = 'list.html'
    model = B_BoardModel


class B_BoardDetail(DetailView):
    template_name = 'detail.html'
    model = B_BoardModel


class B_BoardCreate(CreateView):
    template_name = 'create.html'
    model = B_BoardModel
    fields = ('title', 'comment', 'good')
    success_url = reverse_lazy('list')