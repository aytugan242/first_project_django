from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time.strftime('%H:%M:%S')}'
    return HttpResponse(msg)

def workdir_view(request):
    current_dir = os.getcwd()
    files_list = os.listdir(current_dir)
    msg = f'Файлы в рабочей директории: '
    for file in files_list:
        msg += f'{file}, '
    return HttpResponse(msg)
