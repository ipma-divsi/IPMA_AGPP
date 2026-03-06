from django.shortcuts import redirect
from django.shortcuts import render
from .models import Clients, User_passes, Aplicacoes, Registo_de_aplicacoes, Equipamento, Registo_equipamento, Logs

# Create your views here.
def register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cargo = request.POST.get('cargo')
        
            # Criar um novo usuário
            # Clients.objects.create(username=username, email=email, password=password, cargo=cargo)
            Clients.objects.create(username="username", email="email@email.com", password="1234", cargo="cargo")
            return render(request, 'ipma_agpp/login.html')
        else:
            return render(request, 'ipma_agpp/register.html')
    except Exception as e:
        
        print(f"An error occurred: {e}")
        
        return render(request, 'ipma_agpp/register.html')


def login(request):
    return render(request, 'ipma_agpp/login.html')

