from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def Portada(request):

    return render(request,"registration/portada.html")

class SignupView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy("login")
    template_name="registration/singup.html"