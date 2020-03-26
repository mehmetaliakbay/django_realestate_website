from django.shortcuts import render

# Create your views here.
from .models import *


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'index.html', context)