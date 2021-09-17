from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class Register(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = 'user/login.html'

