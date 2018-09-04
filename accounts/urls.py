from django.urls import path, include
from django.contrib import auth
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    path('', accounts_views.dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('cadastre-se/', accounts_views.register, name='register'),
    path('nova-senha/', accounts_views.password_reset, name='password_reset'),
    path('confirmar-nova-senha/<key>', accounts_views.password_reset_confirm, name='password_reset_confirm'),
    path('editar/', accounts_views.edit, name='edit'),
    path('editar-senha/', accounts_views.edit_password, name='edit_password')
]
