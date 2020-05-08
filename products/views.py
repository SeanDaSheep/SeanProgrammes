from django.http import HttpResponse
from django.shortcuts import render
import random


def home(request):
    return render(request, 'products/home.html')


def generator(request):
    return render(request, 'products/generator.html')


def about(request):
    return render(request, 'products/about.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    try:
        length = int(request.GET.get('length'))
    except ValueError:
        length = 0
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'products/password.html', {'password': thepassword})

# def new(request):
#     return HttpResponse('New thingy')
