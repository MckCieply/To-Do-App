from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *

def index(request):
    tasks = Task.objects.all()

    constext = {'tasks': tasks}
    return render(request, 'tasks/list.html', constext)