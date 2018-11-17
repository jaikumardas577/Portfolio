from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView
import random


# Create your views here.
def index_view(request):
	template='index.html'
	return render(request,template)