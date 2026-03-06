
from django.contrib.auth.views import LoginView
from .forms import Login
from django.shortcuts import redirect
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'ipma_agpp/login.html'  # O nome do modelo que será usado para renderizar a tela de login
    authentication_form = Login


def home(request): 
    user = request.user 
    if user.groups.filter(name='TI').exists(): 
       
        return redirect('/TI/')
    print ('ola') 
    return redirect('/TI/')

def TI_dashboard(request):
    return render(request, 'ipma_agpp/TI.html')
