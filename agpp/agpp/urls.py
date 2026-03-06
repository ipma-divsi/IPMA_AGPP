
from django.contrib import admin
from django.urls import path
from ipma_agpp import views
from ipma_agpp.views import CustomLoginView
from ipma_agpp.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view()),
    path('home/',views.home, name='home'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('TI/', views.TI_dashboard, name ='TI')
]