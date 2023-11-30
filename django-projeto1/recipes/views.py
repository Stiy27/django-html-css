#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Minha primeira HttpResponse!</h1>\
                         <ul><li><a href="/sobre/">Sobre</a></li>\
                         <li><a href="/contato/">Contato</a></li></ul>')

def my_sobre(request):
    return HttpResponse('<h1>Página sobre mim!</h1>\
                         <ul><li><a href="/#/">Home</a></li>\
                         <li><a href="/contato/">Contato</a></li></ul>')

def contato(request):
    return HttpResponse('<h1>Meu contato!</h1>\
                         <ul><li><a href="/#/">Home</a></li>\
                         <li><a href="/sobre/">Sobre</a></li></ul>')


