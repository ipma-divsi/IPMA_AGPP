from django.shortcuts import render
from .models import User, User_passes, Aplicacoes, Registo_de_aplicacoes, Equipamento, Registo_equipamento, Logs

# Create your views here.
def register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cargo = request.POST.get('cargo')
        
            # Criar um novo usuário
            user = User(user=username, email=email, password=password, cargo=cargo)
            user.save()
            return render(request, 'ipma_agpp/login.html')
        else:
            return render(request, 'ipma_agpp/register.html')
    except Exception as e:
        
        print(f"An error occurred: {e}")
        
        return render(request, 'ipma_agpp/register.html')


def login(request):
    return render(request, 'ipma_agpp/login.html')


