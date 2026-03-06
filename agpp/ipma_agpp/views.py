from django.shortcuts import redirect
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User, auth
from .models import User, User_passes, Aplicacoes, Registo_de_aplicacoes, Equipamento, Registo_equipamento, Logs
from .forms import RegisterForm
# Create your views here.
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "ipma_agpp/register.html", {"form": form})

def login(request):
    
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "ipma_agpp/login.html", {"error": "Invalid username or password."})