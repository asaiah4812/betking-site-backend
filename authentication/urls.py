from django.urls import path
from . import views

app_name="auth"

urlpatterns = [
    path('', views.login, name='home'),
    path('SignUp/', views.signup_user, name='signup'),
    path('Login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]