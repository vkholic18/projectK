from django.urls import path
from .views import home,success,about,services,contact,admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('success',success,name='success'),
    path('about',about,name='about'),
    path('services',services,name='services'),
    path('contact',contact,name='contact'),
    path('admin_dashboard',admin,name='admin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]