from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.home), # /HOME/
    path('sobre/', views.my_sobre), # /sobre/
    path('contato/', views.contato), # /contato/
]