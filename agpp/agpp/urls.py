from django.contrib import admin
from django.urls import path
from ipma_agpp import views



app_name = "ipma_agpp"
urlpatterns = [
    path('admin/', admin.site.urls),


    path('', views.register, name='home'),
    path("register/", views.register, name="register"),
    
    path("login/", views.login, name="login"),

]