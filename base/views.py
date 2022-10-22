from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import  Home


def home(home):

    return HttpResponse('PAGINA HOME')


class HomePage(ListView):
    template_name = 'base/home.html'
    model = Home




