from multiprocessing import context
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': 'Estudo, Aplicação Web, Tutorial Django!!!'}
    return render(request, 'app_rango/index.html', context=context_dict)
