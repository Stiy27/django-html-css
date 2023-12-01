
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={'name':'Ashley Riot',}) # global ou recipes são namspaces


def my_sobre(request):
    return HttpResponse('<h1>Página sobre mim!</h1>\
                         <ul><li><a href="/#/">Home</a></li>\
                         <li><a href="/contato/">Contato</a></li></ul>')

def contato(request):
    return HttpResponse('<h1>Meu contato!</h1>\
                         <ul><li><a href="/#/">Home</a></li>\
                         <li><a href="/sobre/">Sobre</a></li></ul>')


